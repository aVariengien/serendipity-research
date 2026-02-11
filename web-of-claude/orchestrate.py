#!/usr/bin/env python3
"""
Web of Claude - Multi-Agent Conversation Orchestrator

Orchestrates conversations between Claude Code instances, where each instance
represents a "persona" based on a folder of content (e.g., Substack posts).
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

# Try to import rich for nice progress bars
try:
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn, TimeElapsedColumn
    from rich.live import Live
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# Progress tracking
class ProgressTracker:
    """Track and display progress of multiple conversations using rich."""
    
    def __init__(self, use_rich: bool = True):
        self.conversations: dict[str, dict] = {}
        self._lock = asyncio.Lock()
        self._use_rich = use_rich and RICH_AVAILABLE
        self._progress = None
        self._task_ids = {}
        
        if self._use_rich:
            self._console = Console()
            self._progress = Progress(
                SpinnerColumn(),
                TextColumn("[bold blue]{task.fields[pair_name]}"),
                BarColumn(bar_width=30),
                TaskProgressColumn(),
                TextColumn("{task.fields[status]}"),
                TimeElapsedColumn(),
                console=self._console,
                expand=False,
            )
    
    def start(self):
        """Start the progress display."""
        if self._use_rich and self._progress:
            self._progress.start()
    
    def stop(self):
        """Stop the progress display."""
        if self._use_rich and self._progress:
            self._progress.stop()
    
    async def register(self, pair_name: str, total_turns: int):
        async with self._lock:
            # Each conversation has: turns * 2 (person A + B) + 1 (synthesis)
            total_steps = total_turns * 2 + 1
            short_name = pair_name.replace("substack_posts_", "").replace("_vs_", " vs ")
            
            self.conversations[pair_name] = {
                "current_step": 0,
                "total_steps": total_steps,
                "total_turns": total_turns,
                "status": "Starting...",
            }
            
            if self._use_rich and self._progress:
                task_id = self._progress.add_task(
                    pair_name,
                    total=total_steps,
                    pair_name=short_name,
                    status="Starting...",
                )
                self._task_ids[pair_name] = task_id
            else:
                print(f"[{short_name}] Starting conversation ({total_turns} turns)", flush=True)
    
    async def update(self, pair_name: str, turn: int = None, phase: str = None, speaker: str = None, step_increment: bool = False):
        async with self._lock:
            if pair_name not in self.conversations:
                return
                
            conv = self.conversations[pair_name]
            short_name = pair_name.replace("substack_posts_", "").replace("_vs_", " vs ")
            
            # Update step and status
            if phase == "synthesis":
                conv["current_step"] = conv["total_turns"] * 2
                status = "Synthesizing..."
            elif step_increment:
                conv["current_step"] = conv.get("current_step", 0) + 1
                if speaker:
                    status = f"Turn {turn}/{conv['total_turns']} - {speaker}..."
                else:
                    status = f"Turn {turn}/{conv['total_turns']}"
            elif turn is not None:
                if speaker:
                    status = f"Turn {turn}/{conv['total_turns']} - {speaker}..."
                else:
                    status = f"Turn {turn}/{conv['total_turns']}"
            else:
                status = conv.get("status", "Working...")
            
            conv["status"] = status
            
            if self._use_rich and self._progress and pair_name in self._task_ids:
                self._progress.update(
                    self._task_ids[pair_name],
                    completed=conv["current_step"],
                    status=status,
                )
            elif not self._use_rich:
                print(f"[{short_name}] {status}", flush=True)
    
    async def complete(self, pair_name: str, success: bool = True):
        async with self._lock:
            if pair_name not in self.conversations:
                return
                
            conv = self.conversations[pair_name]
            short_name = pair_name.replace("substack_posts_", "").replace("_vs_", " vs ")
            status = "✓ Complete" if success else "✗ Failed"
            conv["status"] = status
            
            if self._use_rich and self._progress and pair_name in self._task_ids:
                self._progress.update(
                    self._task_ids[pair_name],
                    completed=conv["total_steps"],
                    status=status,
                )
            else:
                print(f"[{short_name}] {status}", flush=True)


# Global progress tracker (initialized in main)
progress: Optional[ProgressTracker] = None


async def run_claude(
    prompt: str,
    add_dirs: list[Path],
    system_prompt: str,
    working_dir: Path,
    timeout: Optional[int] = None,
    verbose: bool = False,
    log_file: Optional[Path] = None,
) -> str:
    """
    Execute claude -p and return the response.
    
    Args:
        prompt: The user prompt to send to Claude
        add_dirs: List of directories to give Claude access to
        system_prompt: System prompt for this Claude instance
        working_dir: Working directory for the Claude process
        timeout: Maximum time to wait for response (seconds), None for no timeout
        verbose: If True, print debug information
        log_file: Path to write full JSON trace to (captures all tool calls)
    
    Returns:
        Claude's response as a string
    """
    cmd = ["claude", "-p"]
    
    # Add directories
    for dir_path in add_dirs:
        cmd.extend(["--add-dir", str(dir_path)])
    
    # Add system prompt
    if system_prompt:
        cmd.extend(["--system-prompt", system_prompt])
    
    # Use JSON output format if we want to capture the full trace
    if log_file:
        cmd.extend(["--output-format", "json"])
    cmd.extend(["--model", "sonnet"])
    
    # Pass prompt via stdin to avoid command-line length limits
    # The prompt argument to claude -p can also be read from stdin
    
    if verbose:
        print(f"\n    Running: {' '.join(cmd[:6])}...", flush=True)
    
    # Run the command with stdin
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=working_dir,
    )
    
    try:
        if timeout:
            stdout, stderr = await asyncio.wait_for(
                process.communicate(input=prompt.encode()),
                timeout=timeout,
            )
        else:
            # No timeout
            stdout, stderr = await process.communicate(input=prompt.encode())
    except asyncio.TimeoutError:
        process.kill()
        await process.wait()
        raise TimeoutError(f"Claude process timed out after {timeout}s")
    
    if process.returncode != 0:
        error_msg = stderr.decode() if stderr else "Unknown error"
        raise RuntimeError(f"Claude process failed (exit {process.returncode}): {error_msg}")
    
    output = stdout.decode()
    
    # If we're capturing logs, parse JSON and extract the text response
    if log_file:
        # Save the full JSON trace
        log_file.write_text(output)
        
        # Parse JSON to extract the final text response
        try:
            data = json.loads(output)
            # The result field contains the final text
            if "result" in data:
                return data["result"].strip()
            # Fallback: look in messages
            if "messages" in data:
                text_parts = []
                for msg in data["messages"]:
                    if msg.get("role") == "assistant":
                        for content in msg.get("content", []):
                            if isinstance(content, dict) and content.get("type") == "text":
                                text_parts.append(content.get("text", ""))
                            elif isinstance(content, str):
                                text_parts.append(content)
                return "\n".join(text_parts).strip()
        except json.JSONDecodeError:
            pass
        
        return output.strip()
    
    return output.strip()


async def run_conversation_pair(
    person_a: str,
    person_b: str,
    base_folder: Path,
    output_dir: Path,
    orchestration_prompt: str,
    personal_prompt_template: str,
    synthesis_prompt_template: str,
    num_turns: int,
    semaphore: asyncio.Semaphore,
    timeout: Optional[int] = None,
    verbose: bool = False,
) -> Path:
    """
    Run a full conversation between two personas.
    
    Args:
        person_a: Name/folder of first person
        person_b: Name/folder of second person
        base_folder: Path to folder containing person subfolders
        output_dir: Where to save conversation and synthesis
        orchestration_prompt: The guiding prompt for the discussion
        personal_prompt_template: Template with {person} placeholder
        num_turns: Number of conversation rounds
        semaphore: Semaphore for controlling parallelism
    
    Returns:
        Path to the synthesis file
    """
    async with semaphore:
        # Determine folder paths (use absolute paths so they work from any cwd)
        folder_a = (base_folder / person_a).resolve()
        folder_b = (base_folder / person_b).resolve()
        
        if not folder_a.exists():
            raise FileNotFoundError(f"Folder not found: {folder_a}")
        if not folder_b.exists():
            raise FileNotFoundError(f"Folder not found: {folder_b}")
        
        # Create output directory for this pair
        pair_name = f"{person_a}_vs_{person_b}"
        pair_output = output_dir / pair_name
        pair_output.mkdir(parents=True, exist_ok=True)
        
        # Create logs directory for agent traces
        logs_dir = pair_output / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize conversation file
        conversation_file = pair_output / "conversation.md"
        
        # Extract clean names (remove substack_posts_ prefix if present)
        clean_name_a = person_a.replace("substack_posts_", "")
        clean_name_b = person_b.replace("substack_posts_", "")
        
        # Write initial context
        initial_content = f"""# Conversation: {clean_name_a} vs {clean_name_b}

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M")}

## Topic
{orchestration_prompt}

---

## Conversation

"""
        conversation_file.write_text(initial_content)
        
        # Register with progress tracker
        await progress.register(pair_name, num_turns)
        
        # Format personal prompts
        personal_prompt_a = personal_prompt_template.format(
            person=clean_name_a,
            folder=str(folder_a),
        )
        personal_prompt_b = personal_prompt_template.format(
            person=clean_name_b,
            folder=str(folder_b),
        )
        
        # Run conversation turns
        for turn in range(num_turns):
            await progress.update(pair_name, turn=turn + 1, phase="conversation")
            
            # Read current conversation
            current_conversation = conversation_file.read_text()
            
            # Person A's turn
            prompt_a = f"""You are participating in a structured dialogue with {clean_name_b}.

Here is the conversation so far:

{current_conversation}

---

Now add your response as {clean_name_a}. Draw from your writings and perspective. Be thoughtful and engaging.
Keep your response focused and under 500 words.

The discussion topic is: {orchestration_prompt}"""
            
            try:
                await progress.update(pair_name, turn=turn + 1, speaker=clean_name_a)
                log_file_a = logs_dir / f"{clean_name_a}_turn_{turn + 1}.json"
                response_a = await run_claude(
                    prompt=prompt_a,
                    add_dirs=[folder_a],
                    system_prompt=personal_prompt_a,
                    working_dir=pair_output,
                    timeout=timeout,
                    verbose=verbose,
                    log_file=log_file_a,
                )
                
                # Append to conversation
                with open(conversation_file, "a") as f:
                    f.write(f"### {clean_name_a}\n\n{response_a}\n\n---\n\n")
                
                # Update progress after successful response
                await progress.update(pair_name, turn=turn + 1, step_increment=True)
                
            except Exception as e:
                if verbose:
                    print(f"\n[{pair_name}] Error on {clean_name_a}'s turn: {e}", flush=True)
                with open(conversation_file, "a") as f:
                    f.write(f"### {clean_name_a}\n\n*[Error: {e}]*\n\n---\n\n")
                await progress.update(pair_name, turn=turn + 1, step_increment=True)
            
            # Read updated conversation
            current_conversation = conversation_file.read_text()
            
            # Person B's turn
            prompt_b = f"""You are participating in a structured dialogue with {clean_name_a}.

Here is the conversation so far:

{current_conversation}

---

Now add your response as {clean_name_b}. Draw from your writings and perspective. Be thoughtful and engaging.
Keep your response focused and under 500 words.

The discussion topic is: {orchestration_prompt}"""
            
            try:
                await progress.update(pair_name, turn=turn + 1, speaker=clean_name_b)
                log_file_b = logs_dir / f"{clean_name_b}_turn_{turn + 1}.json"
                response_b = await run_claude(
                    prompt=prompt_b,
                    add_dirs=[folder_b],
                    system_prompt=personal_prompt_b,
                    working_dir=pair_output,
                    timeout=timeout,
                    verbose=verbose,
                    log_file=log_file_b,
                )
                
                # Append to conversation
                with open(conversation_file, "a") as f:
                    f.write(f"### {clean_name_b}\n\n{response_b}\n\n---\n\n")
                
                # Update progress after successful response
                await progress.update(pair_name, turn=turn + 1, step_increment=True)
                
            except Exception as e:
                if verbose:
                    print(f"\n[{pair_name}] Error on {clean_name_b}'s turn: {e}", flush=True)
                await progress.update(pair_name, turn=turn + 1, step_increment=True)
                with open(conversation_file, "a") as f:
                    f.write(f"### {clean_name_b}\n\n*[Error: {e}]*\n\n---\n\n")
        
        # Generate synthesis
        await progress.update(pair_name, phase="synthesis", speaker=None)
        
        final_conversation = conversation_file.read_text()
        
        # Format synthesis prompt with available placeholders
        formatted_synthesis_prompt = synthesis_prompt_template.format(
            person_a=clean_name_a,
            person_b=clean_name_b,
            conversation=final_conversation,
        ) if any(p in synthesis_prompt_template for p in ['{person_a}', '{person_b}', '{conversation}']) else synthesis_prompt_template
        
        synthesis_prompt = f"""You have just observed a dialogue between {clean_name_a} and {clean_name_b}.

Here is the full conversation:

{final_conversation}

---

{formatted_synthesis_prompt}"""

        try:
            log_file_synthesis = logs_dir / "synthesis.json"
            synthesis = await run_claude(
                prompt=synthesis_prompt,
                add_dirs=[folder_a, folder_b],
                system_prompt="You are a thoughtful analyst synthesizing a dialogue between two thinkers.",
                working_dir=pair_output,
                timeout=timeout,
                verbose=verbose,
                log_file=log_file_synthesis,
            )
            
            synthesis_file = pair_output / "synthesis.md"
            synthesis_content = f"""# Synthesis: {clean_name_a} vs {clean_name_b}

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Topic**: {orchestration_prompt}

---

{synthesis}
"""
            synthesis_file.write_text(synthesis_content)
            await progress.complete(pair_name, success=True)
            
        except Exception as e:
            if verbose:
                print(f"\n[{pair_name}] Error generating synthesis: {e}", flush=True)
            synthesis_file = pair_output / "synthesis.md"
            synthesis_file.write_text(f"# Synthesis Error\n\nFailed to generate synthesis: {e}")
            await progress.complete(pair_name, success=False)
        
        return synthesis_file


async def run_synthesis_only(
    person_a: str,
    person_b: str,
    base_folder: Path,
    output_dir: Path,
    orchestration_prompt: str,
    synthesis_prompt_template: str,
    semaphore: asyncio.Semaphore,
    timeout: Optional[int] = None,
    verbose: bool = False,
) -> Path:
    """
    Run only the synthesis step on an existing conversation.
    
    Args:
        person_a: Name/folder of first person
        person_b: Name/folder of second person
        base_folder: Path to folder containing person subfolders
        output_dir: Where conversation logs are stored
        orchestration_prompt: The original topic
        synthesis_prompt_template: Template for synthesis
        semaphore: Semaphore for controlling parallelism
        timeout: Timeout for Claude call
        verbose: Enable verbose output
    
    Returns:
        Path to the synthesis file
    """
    async with semaphore:
        # Determine folder paths (use absolute paths)
        folder_a = (base_folder / person_a).resolve()
        folder_b = (base_folder / person_b).resolve()
        
        # Find the conversation directory
        pair_name = f"{person_a}_vs_{person_b}"
        pair_output = output_dir / pair_name
        
        if not pair_output.exists():
            raise FileNotFoundError(f"Conversation folder not found: {pair_output}")
        
        conversation_file = pair_output / "conversation.md"
        if not conversation_file.exists():
            raise FileNotFoundError(f"Conversation file not found: {conversation_file}")
        
        # Create logs directory
        logs_dir = pair_output / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        
        # Extract clean names
        clean_name_a = person_a.replace("substack_posts_", "")
        clean_name_b = person_b.replace("substack_posts_", "")
        
        # Register with progress tracker
        await progress.register(pair_name, 1)  # Just 1 step for synthesis
        await progress.update(pair_name, phase="synthesis")
        
        # Read the conversation
        final_conversation = conversation_file.read_text()
        
        # Format synthesis prompt
        formatted_synthesis_prompt = synthesis_prompt_template.format(
            person_a=clean_name_a,
            person_b=clean_name_b,
            conversation=final_conversation,
        ) if any(p in synthesis_prompt_template for p in ['{person_a}', '{person_b}', '{conversation}']) else synthesis_prompt_template
        
        synthesis_prompt = f"""You have just observed a dialogue between {clean_name_a} and {clean_name_b}.

Here is the full conversation:

{final_conversation}

---

{formatted_synthesis_prompt}"""

        try:
            log_file_synthesis = logs_dir / "synthesis.json"
            synthesis = await run_claude(
                prompt=synthesis_prompt,
                add_dirs=[folder_a, folder_b] if folder_a.exists() and folder_b.exists() else [],
                system_prompt="You are a thoughtful analyst synthesizing a dialogue between two thinkers.",
                working_dir=pair_output,
                timeout=timeout,
                verbose=verbose,
                log_file=log_file_synthesis,
            )
            
            synthesis_file = pair_output / "synthesis.md"
            synthesis_content = f"""# Synthesis: {clean_name_a} vs {clean_name_b}

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M")}
**Topic**: {orchestration_prompt}

---

{synthesis}
"""
            synthesis_file.write_text(synthesis_content)
            await progress.complete(pair_name, success=True)
            
        except Exception as e:
            if verbose:
                print(f"\n[{pair_name}] Error generating synthesis: {e}", flush=True)
            synthesis_file = pair_output / "synthesis.md"
            synthesis_file.write_text(f"# Synthesis Error\n\nFailed to generate synthesis: {e}")
            await progress.complete(pair_name, success=False)
        
        return synthesis_file


async def main():
    parser = argparse.ArgumentParser(
        description="Orchestrate conversations between Claude instances representing different personas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python orchestrate.py \\
    --folder ./note_folders \\
    --pairs '[["substack_posts_simonw", "substack_posts_thezvi"]]' \\
    --orchestration-prompt "Discuss the future of AI agents" \\
    --turns 3 \\
    --max-parallel 2

The pairs should be a JSON array of arrays, where each inner array contains
exactly two folder names from the base folder.
        """
    )
    
    parser.add_argument(
        "--folder", "-f",
        type=Path,
        default=None,
        help="Path to folder containing person subfolders"
    )
    
    parser.add_argument(
        "--pairs", "-p",
        type=str,
        default=None,
        help='JSON list of pairs, e.g. \'[["person_a", "person_b"]]\''
    )
    
    parser.add_argument(
        "--orchestration-prompt", "-o",
        type=str,
        default=None,
        help="The guiding prompt for what to discuss/synthesize"
    )
    
    parser.add_argument(
        "--personal-prompt", "-pp",
        type=str,
        default=None,
        help="Template with {person} and {folder} placeholders"
    )
    
    parser.add_argument(
        "--synthesis-prompt", "-sp",
        type=str,
        default=None,
        help="Template for the synthesis prompt. Use {person_a}, {person_b}, {conversation} placeholders."
    )
    
    parser.add_argument(
        "--turns", "-t",
        type=int,
        default=None,
        help="Number of conversation rounds (default: 5)"
    )
    
    parser.add_argument(
        "--max-parallel", "-m",
        type=int,
        default=None,
        help="Max concurrent pair conversations (default: 3)"
    )
    
    parser.add_argument(
        "--output-dir", "-d",
        type=Path,
        default=None,
        help="Where to save conversation logs and synthesis (default: ./conversations)"
    )
    
    parser.add_argument(
        "--config", "-c",
        type=Path,
        help="Load settings from a JSON config file (CLI args override config)"
    )
    
    parser.add_argument(
        "--timeout",
        type=int,
        default=None,
        help="Timeout for each Claude call in seconds (default: no timeout)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output"
    )
    
    parser.add_argument(
        "--synthesis-only",
        action="store_true",
        help="Only run synthesis on existing conversations (skip conversation turns)"
    )
    
    args = parser.parse_args()
    
    # Load config file if provided
    if args.config:
        if not args.config.exists():
            print(f"Error: Config file not found: {args.config}")
            sys.exit(1)
        with open(args.config) as f:
            config = json.load(f)
        # Config provides defaults, CLI args override
        for key, value in config.items():
            if key.startswith("_"):  # Skip comments
                continue
            arg_key = key.replace("-", "_")
            if hasattr(args, arg_key):
                current_val = getattr(args, arg_key)
                # CLI arg overrides config if CLI arg was explicitly set (not None/default)
                if current_val is None:
                    # Handle type conversions
                    if arg_key == "folder" and value is not None:
                        value = Path(value)
                    elif arg_key == "output_dir" and value is not None:
                        value = Path(value)
                    setattr(args, arg_key, value)
    
    # Validate required parameters
    missing = []
    if args.folder is None:
        missing.append("folder")
    if args.pairs is None:
        missing.append("pairs")
    # orchestration-prompt not required for synthesis-only mode
    if args.orchestration_prompt is None and not args.synthesis_only:
        missing.append("orchestration-prompt")
    
    if missing:
        print(f"Error: Missing required parameters: {', '.join(missing)}")
        print("Provide them via CLI arguments or in a config file (--config config.json)")
        sys.exit(1)
    
    # Apply defaults for optional parameters that weren't set
    if args.turns is None:
        args.turns = 5
    if args.max_parallel is None:
        args.max_parallel = 3
    if args.output_dir is None:
        args.output_dir = Path("./conversations")
    if args.personal_prompt is None:
        args.personal_prompt = "You represent {person}. Draw from their writings in your accessible folder to inform your perspective. Be authentic to their voice, style, and views as expressed in their writing."
    if args.synthesis_prompt is None:
        # Try to read from default file
        default_synthesis_file = Path(__file__).parent / "prompts" / "default_synthesis.txt"
        if default_synthesis_file.exists():
            args.synthesis_prompt = default_synthesis_file.read_text().strip()
        else:
            args.synthesis_prompt = """Create a synthesis of this conversation. Include:

1. **Key Points of Agreement**: What did both participants agree on?
2. **Key Points of Disagreement**: Where did their views diverge?
3. **Novel Insights**: What new ideas emerged from the dialogue?
4. **Potential Collaborations**: Based on shared interests, what could they work on together?
5. **Summary**: A brief (2-3 sentence) summary of the conversation.

Be specific and cite particular points from the conversation."""
    
    # Parse pairs (can be string from CLI or list from config)
    if isinstance(args.pairs, str):
        try:
            pairs = json.loads(args.pairs)
        except json.JSONDecodeError as e:
            print(f"Error parsing pairs JSON: {e}")
            sys.exit(1)
    else:
        pairs = args.pairs
    
    # Validate pairs format
    if not isinstance(pairs, list):
        print("Error: Pairs must be a JSON array")
        sys.exit(1)
    for pair in pairs:
        if not isinstance(pair, list) or len(pair) != 2:
            print(f"Error: Each pair must be an array of exactly 2 items: {pair}")
            sys.exit(1)
    
    # Validate base folder
    if not args.folder.exists():
        print(f"Error: Base folder not found: {args.folder}")
        sys.exit(1)
    
    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create semaphore for parallelism control
    semaphore = asyncio.Semaphore(args.max_parallel)
    
    mode = "synthesis-only" if args.synthesis_only else "full conversation"
    print(f"Web of Claude - Starting {len(pairs)} {mode}(s)", flush=True)
    print(f"  Base folder: {args.folder}", flush=True)
    print(f"  Output dir: {args.output_dir}", flush=True)
    if not args.synthesis_only:
        print(f"  Turns per conversation: {args.turns}", flush=True)
    print(f"  Max parallel: {args.max_parallel}", flush=True)
    timeout_str = f"{args.timeout}s" if args.timeout else "none"
    print(f"  Timeout per call: {timeout_str}", flush=True)
    if not args.synthesis_only:
        print(f"  Orchestration prompt: {args.orchestration_prompt[:100]}...", flush=True)
    print(flush=True)
    
    # Initialize progress tracker
    global progress
    progress = ProgressTracker(use_rich=not args.verbose)
    progress.start()
    
    # Run all pairs
    if args.synthesis_only:
        # Only regenerate synthesis for existing conversations
        tasks = [
            run_synthesis_only(
                person_a=pair[0],
                person_b=pair[1],
                base_folder=args.folder,
                output_dir=args.output_dir,
                orchestration_prompt=args.orchestration_prompt or "",
                synthesis_prompt_template=args.synthesis_prompt,
                semaphore=semaphore,
                timeout=args.timeout,
                verbose=args.verbose,
            )
            for pair in pairs
        ]
    else:
        tasks = [
            run_conversation_pair(
                person_a=pair[0],
                person_b=pair[1],
                base_folder=args.folder,
                output_dir=args.output_dir,
                orchestration_prompt=args.orchestration_prompt,
                personal_prompt_template=args.personal_prompt,
                synthesis_prompt_template=args.synthesis_prompt,
                num_turns=args.turns,
                semaphore=semaphore,
                timeout=args.timeout,
                verbose=args.verbose,
            )
            for pair in pairs
        ]
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Stop progress display
    progress.stop()
    
    # Report results
    print("\n" + "=" * 60)
    print("Results:")
    for pair, result in zip(pairs, results):
        pair_name = f"{pair[0]}_vs_{pair[1]}"
        if isinstance(result, Exception):
            print(f"  [{pair_name}] FAILED: {result}")
        else:
            print(f"  [{pair_name}] Success: {result}")
    
    # Count successes
    successes = sum(1 for r in results if not isinstance(r, Exception))
    print(f"\nCompleted: {successes}/{len(pairs)} conversations")
    
    return 0 if successes == len(pairs) else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
