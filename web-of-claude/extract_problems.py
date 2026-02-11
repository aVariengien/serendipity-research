#!/usr/bin/env python3
"""
Extract live problems from Substack authors' posts.

Scans each author's folder, reads recent posts, and uses Claude Sonnet
to infer actionable problems the author is currently wrestling with.
"""

import argparse
import asyncio
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import anthropic

# Try to import rich for nice output
try:
    from rich.console import Console
    from rich.table import Table
    from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

console = Console() if RICH_AVAILABLE else None

# ---------------------------------------------------------------------------
# Tool schema for structured output
# ---------------------------------------------------------------------------

PROBLEMS_TOOL = {
    "name": "report_problems",
    "description": "Report the extracted problems for this author.",
    "input_schema": {
        "type": "object",
        "properties": {
            "problems": {
                "type": "array",
                "description": "Up to 2 live problems inferred from this post. Only include problems scoring 5 or above.",
                "items": {
                    "type": "object",
                    "properties": {
                        "problem": {
                            "type": "string",
                            "description": "Short title phrased as an email subject line (max ~10 words)."
                        },
                        "description": {
                            "type": "string",
                            "description": "2-3 sentence explanation of the problem, citing specific posts by title."
                        },
                        "evidence": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "2-4 verbatim quotes or close paraphrases from posts that support this problem."
                        },
                        "email_open_score": {
                            "type": "integer",
                            "description": "1-10 score: how much care/attention would the author give a cold email with this problem as subject."
                        },
                        "email_open_reasoning": {
                            "type": "string",
                            "description": "1-2 sentences justifying the score."
                        },
                        "persistence_months": {
                            "type": "integer",
                            "description": "Estimated number of months this problem will remain alive for the author."
                        },
                        "persistence_reasoning": {
                            "type": "string",
                            "description": "1-2 sentences justifying the persistence estimate."
                        },
                        "category": {
                            "type": "string",
                            "enum": [
                                "project_blocker",
                                "collaboration_need",
                                "skill_gap",
                                "strategic_question",
                                "creative_block",
                                "resource_constraint"
                            ],
                            "description": "The category that best fits this problem."
                        }
                    },
                    "required": [
                        "problem",
                        "description",
                        "evidence",
                        "email_open_score",
                        "email_open_reasoning",
                        "persistence_months",
                        "persistence_reasoning",
                        "category"
                    ]
                }
            }
        },
        "required": ["problems"]
    }
}

# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """You are an analyst who reads an author's recent blog posts and infers what live, actionable problems the author is currently wrestling with.

Your goal: identify problems that are SO alive for this person that if a stranger emailed them with that problem as the subject line, they would invest real time and attention reading it -- even if they're busy and don't know the sender.

Important: the email comes from OUTSIDE the author's close network. Not a friend, not a known collaborator -- a stranger. The author has no social reason to engage. They will only engage if the problem itself is compelling enough.

You are looking for:
- Explicit asks: the author literally says "I need X" or "looking for Y" or "if you know someone who..."
- Clear project blockers: something is stuck and they need external help to unblock it
- Concrete collaboration needs: they need specific skills, perspectives, or connections they don't have
- Resource constraints with urgency: funding, hiring, tools -- where delay costs them

You are NOT looking for:
- Vague intellectual interests or philosophical tensions (these are interesting to think about but you wouldn't drop everything for a stranger's email about them)
- Finished ideas or solved problems
- Generic themes of their writing (e.g. "interested in AI")
- Problems they've already resolved
- Experimental or speculative work where it's unclear if the author will keep pursuing it
- Open questions they're casually musing about vs. actively trying to solve

## Scoring metric: email_open_score (1-10)

The core question: "If a complete stranger -- not someone in the author's network -- sent a cold email with this problem as the subject line, how much care and attention would the author invest in reading and potentially replying?"

You MUST use the full range. Most problems should score in the 3-6 range. 7+ is rare. 9-10 is exceptional.

Calibration anchors:

- 1-2: Tangentially related to their work. They'd delete the email or skim and forget it.
- 3-4: Something they've written about, but it's a background interest or philosophical question -- not something they need help with. They'd read it but think "interesting, but I don't need to act on this." Also: experimental or exploratory work where the author might not persist -- a stranger's input feels premature.
- 5-6: A real problem they're working on, but they could solve it themselves or it's one of several priorities. They'd read carefully but probably wouldn't reply to a stranger about it. Also: technical issues they've identified but have workarounds for, or problems in early-stage projects whose future is uncertain.
- 7-8: Clearly a top priority based on recent writing. They've written about it with urgency, they're actively blocked or constrained, and outside help would meaningfully change their situation. They'd reply and possibly schedule a call.
- 9-10: The author has EXPLICITLY asked for help with this. They've said "I'm looking for...", "if you know someone who...", "I need...". Or: this is so clearly the central challenge of their current work that any relevant help would be welcomed immediately. A stranger's email about this gets opened, read, and replied to the same day.

## Persistence estimate

Estimate how many months from now this problem will STILL be alive for the author. Consider:
- Is this a short sprint (1-2 months) or a long-term project (6-12+ months)?
- How deep are they into it? Early = longer persistence.
- Is it structural (ongoing) or situational (will resolve)?
- For speculative/experimental work: discount persistence -- the author may pivot away.

## Rules
- Report at most 2 problems per post.
- Be SPECIFIC. "Need help with their project" is bad. "Hiring a data pipeline architect for Community Archive's tweet analysis system" is good.
- The problem title should work as an email subject line -- specific enough that the author immediately knows what it's about.
- Cite specific posts by title as evidence.
- Use verbatim quotes when possible.
- Distinguish between "the author finds this intellectually interesting" (low score) and "the author actively needs help with this" (high score). The bar is: would they engage a STRANGER over email about it?"""


def build_user_prompt(author: str, date: str, title: str, content: str) -> str:
    """Build the user prompt for a single post.
    
    Args:
        author: Clean author name
        date: Post date string
        title: Post title
        content: Post content
    """
    return f"""Below is a blog post by "{author}".

Read it carefully, then identify up to 2 live problems this author is currently wrestling with, as revealed by this post.

Use the report_problems tool to submit your analysis. If no problems score 5+, report an empty list.

--- POST ---
Date: {date}
Title: {title}

{content}"""


# ---------------------------------------------------------------------------
# File loading
# ---------------------------------------------------------------------------

DATE_PREFIX_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.md$")


# Rough chars-per-token estimate for truncation
_CHARS_PER_TOKEN = 4
_MAX_POST_TOKENS = 10_000
_MAX_POST_CHARS = _MAX_POST_TOKENS * _CHARS_PER_TOKEN  # ~40k chars ≈ 10k tokens


def _truncate_post(content: str) -> tuple[str, bool]:
    """Truncate a single post to ~10k tokens by keeping first 5k + last 5k tokens.
    
    Returns (content, was_truncated).
    """
    if len(content) <= _MAX_POST_CHARS:
        return content, False

    half = _MAX_POST_CHARS // 2
    head = content[:half]
    tail = content[-half:]
    truncated = (
        head
        + "\n\n[... TRUNCATED — middle section removed to fit token limit ...]\n\n"
        + tail
    )
    return truncated, True


def load_posts(folder: Path, max_posts: int) -> tuple[list[tuple[str, str, str]], int]:
    """Load the most recent posts from a folder.
    
    Returns (posts, truncated_count) where posts is a list of
    (date_str, title, content) sorted newest-first, and truncated_count
    is the number of posts that were capped at ~10k tokens.
    """
    entries: list[tuple[str, str, Path]] = []
    for f in folder.iterdir():
        if not f.is_file() or f.suffix != ".md":
            continue
        m = DATE_PREFIX_RE.match(f.name)
        if m:
            date_str = m.group(1)
            title_slug = m.group(2)
            title = title_slug.replace("-", " ").strip()
            entries.append((date_str, title, f))
        else:
            # Files without date prefix -- use mtime as fallback
            entries.append(("unknown", f.stem, f))

    # Sort by date descending
    entries.sort(key=lambda e: e[0], reverse=True)
    entries = entries[:max_posts]

    posts = []
    truncated_count = 0
    for date_str, title, path in entries:
        content = path.read_text(encoding="utf-8", errors="replace")
        content, was_truncated = _truncate_post(content)
        if was_truncated:
            truncated_count += 1
        posts.append((date_str, title, content))

    return posts, truncated_count


def discover_authors(folder: Path) -> list[str]:
    """Find all substack_posts_* subdirectories."""
    authors = []
    for d in sorted(folder.iterdir()):
        if d.is_dir() and d.name.startswith("substack_posts_"):
            authors.append(d.name)
    return authors


# ---------------------------------------------------------------------------
# API call
# ---------------------------------------------------------------------------

async def analyze_post(
    client: anthropic.AsyncAnthropic,
    author: str,
    date: str,
    title: str,
    content: str,
    model: str,
) -> tuple[list[dict], dict]:
    """Analyze a single post and return (problems, usage).
    
    Returns:
        problems: list of validated problem dicts (max 2 per post)
        usage: dict with input_tokens and output_tokens
    """
    user_prompt = build_user_prompt(author, date, title, content)

    response = await client.messages.create(
        model=model,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        tools=[PROBLEMS_TOOL],
        tool_choice={"type": "tool", "name": "report_problems"},
        messages=[{"role": "user", "content": user_prompt}],
    )

    # Extract the tool call input
    problems = []
    for block in response.content:
        if block.type == "tool_use" and block.name == "report_problems":
            raw = block.input.get("problems", [])
            for p in raw:
                if isinstance(p, dict) and "problem" in p and "email_open_score" in p:
                    p["source_post"] = title
                    p["source_date"] = date
                    problems.append(p)
            problems = problems[:2]  # max 2 per post
            break

    usage = {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
    }
    return problems, usage


async def analyze_author(
    client: anthropic.AsyncAnthropic,
    author_folder: str,
    base_folder: Path,
    max_posts: int,
    model: str,
    verbose: bool = False,
    semaphore: asyncio.Semaphore | None = None,
) -> dict:
    """Analyze a single author by calling the API once per post."""
    clean_name = author_folder.replace("substack_posts_", "")
    folder_path = base_folder / author_folder

    posts, truncated_count = load_posts(folder_path, max_posts)
    if not posts:
        return {
            "author": clean_name,
            "folder": author_folder,
            "analyzed_at": datetime.now().isoformat(),
            "posts_analyzed": 0,
            "posts_truncated": 0,
            "problems": [],
        }

    if truncated_count and verbose:
        print(f"  [{clean_name}] {truncated_count}/{len(posts)} posts truncated to ~{_MAX_POST_TOKENS} tokens", flush=True)

    if verbose:
        print(f"  [{clean_name}] Analyzing {len(posts)} posts (1 API call each)...", flush=True)

    # Analyze each post concurrently (respecting the shared semaphore)
    async def _call(date: str, title: str, content: str):
        if semaphore:
            async with semaphore:
                return await analyze_post(client, clean_name, date, title, content, model)
        return await analyze_post(client, clean_name, date, title, content, model)

    tasks = [_call(date, title, content) for date, title, content in posts]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Aggregate problems and usage across all posts
    all_problems: list[dict] = []
    total_input = 0
    total_output = 0
    errors = 0

    for i, res in enumerate(results):
        if isinstance(res, Exception):
            errors += 1
            if verbose:
                print(f"  [{clean_name}] Error on post {i+1}: {res}", flush=True)
            continue
        problems, usage = res
        all_problems.extend(problems)
        total_input += usage["input_tokens"]
        total_output += usage["output_tokens"]

    # Sort by score descending, keep top problems
    all_problems.sort(key=lambda p: p.get("email_open_score", 0), reverse=True)

    if verbose:
        print(f"  [{clean_name}] Done: {len(all_problems)} problems from {len(posts) - errors}/{len(posts)} posts", flush=True)

    return {
        "author": clean_name,
        "folder": author_folder,
        "analyzed_at": datetime.now().isoformat(),
        "posts_analyzed": len(posts),
        "posts_truncated": truncated_count,
        "posts_errored": errors,
        "problems": all_problems,
        "usage": {
            "input_tokens": total_input,
            "output_tokens": total_output,
        },
    }


# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------

def print_summary(all_results: list[dict]):
    """Print summary statistics using rich tables."""
    if not RICH_AVAILABLE or console is None:
        _print_summary_plain(all_results)
        return

    console.print()
    console.rule("[bold]Summary Statistics[/bold]")
    console.print()

    # --- Per-author table ---
    author_table = Table(title="Per-Author Results")
    author_table.add_column("Author", style="cyan")
    author_table.add_column("Posts", justify="right")
    author_table.add_column("Truncated", justify="right", style="dim")
    author_table.add_column("Problems", justify="right")
    author_table.add_column("Highest", justify="right", style="bold")
    author_table.add_column("Avg Score", justify="right")

    all_problems = []
    total_truncated = 0
    for r in sorted(all_results, key=lambda x: x["author"]):
        # Filter to only valid dict problems
        problems = [p for p in r.get("problems", []) if isinstance(p, dict) and "email_open_score" in p]
        scores = [p["email_open_score"] for p in problems]
        highest = max(scores) if scores else "-"
        avg = f"{sum(scores) / len(scores):.1f}" if scores else "-"
        trunc = r.get("posts_truncated", 0)
        total_truncated += trunc
        author_table.add_row(
            r["author"],
            str(r["posts_analyzed"]),
            str(trunc) if trunc else "-",
            str(len(problems)),
            str(highest),
            avg,
        )
        for p in problems:
            all_problems.append({"author": r["author"], **p})

    console.print(author_table)
    console.print()

    # --- Aggregate stats ---
    total_authors = len(all_results)
    total_problems = len(all_problems)
    all_scores = [p["email_open_score"] for p in all_problems if "email_open_score" in p]
    all_persistence = [p["persistence_months"] for p in all_problems if "persistence_months" in p]
    all_categories = [p["category"] for p in all_problems if "category" in p]

    agg_table = Table(title="Aggregate Statistics")
    agg_table.add_column("Metric", style="bold")
    agg_table.add_column("Value", justify="right")

    agg_table.add_row("Authors processed", str(total_authors))
    agg_table.add_row("Total problems found", str(total_problems))
    if total_truncated:
        agg_table.add_row("Posts truncated (>10k tokens)", str(total_truncated))

    if all_scores:
        agg_table.add_row("Avg email_open_score", f"{sum(all_scores) / len(all_scores):.1f}")
        score_9_10 = sum(1 for s in all_scores if s >= 9)
        score_7_8 = sum(1 for s in all_scores if 7 <= s <= 8)
        score_5_6 = sum(1 for s in all_scores if 5 <= s <= 6)
        agg_table.add_row("Scores 9-10 (urgent)", str(score_9_10))
        agg_table.add_row("Scores 7-8 (high)", str(score_7_8))
        agg_table.add_row("Scores 5-6 (moderate)", str(score_5_6))

    if all_persistence:
        agg_table.add_row("Avg persistence (months)", f"{sum(all_persistence) / len(all_persistence):.1f}")

    if all_categories:
        from collections import Counter
        cat_counts = Counter(all_categories)
        top_cats = cat_counts.most_common(3)
        for cat, count in top_cats:
            agg_table.add_row(f"Category: {cat}", str(count))

    console.print(agg_table)
    console.print()

    # --- Top problems leaderboard ---
    if all_problems:
        sorted_problems = sorted(all_problems, key=lambda p: p.get("email_open_score", 0), reverse=True)
        top_n = sorted_problems[:10]

        top_table = Table(title="Top Problems (Best Outreach Opportunities)")
        top_table.add_column("Score", justify="right", style="bold green")
        top_table.add_column("Author", style="cyan")
        top_table.add_column("Problem", style="white")
        top_table.add_column("Source Post", style="dim")
        top_table.add_column("Persistence", justify="right")
        top_table.add_column("Category")

        for p in top_n:
            source = p.get("source_post", "?")
            # Truncate long post titles for display
            if len(source) > 40:
                source = source[:37] + "..."
            top_table.add_row(
                str(p.get("email_open_score", "?")),
                p.get("author", "?"),
                p.get("problem", "?"),
                source,
                f"{p.get('persistence_months', '?')}mo",
                p.get("category", "?"),
            )

        console.print(top_table)

    # --- Token usage ---
    total_input = sum(r.get("usage", {}).get("input_tokens", 0) for r in all_results)
    total_output = sum(r.get("usage", {}).get("output_tokens", 0) for r in all_results)
    if total_input or total_output:
        console.print()
        console.print(f"[dim]Total tokens used: {total_input:,} input + {total_output:,} output = {total_input + total_output:,} total[/dim]")

    console.print()


def _print_summary_plain(all_results: list[dict]):
    """Fallback plain-text summary when rich is not available."""
    print("\n" + "=" * 60)
    print("SUMMARY STATISTICS")
    print("=" * 60)

    all_problems = []
    for r in sorted(all_results, key=lambda x: x["author"]):
        problems = [p for p in r.get("problems", []) if isinstance(p, dict) and "email_open_score" in p]
        scores = [p["email_open_score"] for p in problems]
        highest = max(scores) if scores else "-"
        avg = f"{sum(scores) / len(scores):.1f}" if scores else "-"
        trunc = r.get("posts_truncated", 0)
        trunc_str = f"  truncated={trunc}" if trunc else ""
        print(f"  {r['author']:25s}  posts={r['posts_analyzed']}{trunc_str}  problems={len(problems)}  highest={highest}  avg={avg}")
        for p in problems:
            all_problems.append({"author": r["author"], **p})

    total_problems = len(all_problems)
    all_scores = [p["email_open_score"] for p in all_problems if "email_open_score" in p]
    print(f"\nTotal: {len(all_results)} authors, {total_problems} problems")
    if all_scores:
        print(f"Average score: {sum(all_scores) / len(all_scores):.1f}")

    if all_problems:
        sorted_problems = sorted(all_problems, key=lambda p: p.get("email_open_score", 0), reverse=True)
        print("\nTop problems:")
        for p in sorted_problems[:5]:
            print(f"  [{p.get('email_open_score', '?')}] {p.get('author', '?')}: {p.get('problem', '?')}")

    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main():
    parser = argparse.ArgumentParser(
        description="Extract live problems from Substack authors' posts using Claude Sonnet",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--folder", "-f",
        type=Path,
        default=Path("./note_folders"),
        help="Path to folder containing substack_posts_* subfolders (default: ./note_folders)",
    )
    parser.add_argument(
        "--output-dir", "-o",
        type=Path,
        default=Path("./problems"),
        help="Where to save JSON results (default: ./problems)",
    )
    parser.add_argument(
        "--max-posts", "-n",
        type=int,
        default=20,
        help="Maximum number of recent posts to analyze per author (default: 20)",
    )
    parser.add_argument(
        "--max-parallel", "-m",
        type=int,
        default=5,
        help="Max concurrent API calls (default: 5)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="claude-sonnet-4-5-20250929",
        help="Anthropic model to use (default: claude-sonnet-4-5-20250929)",
    )
    parser.add_argument(
        "--authors",
        type=str,
        nargs="*",
        default=None,
        help="Specific author folders to analyze (default: all substack_posts_* folders)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    # Validate
    if not args.folder.exists():
        print(f"Error: Folder not found: {args.folder}")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    # Discover authors
    if args.authors:
        author_folders = args.authors
    else:
        author_folders = discover_authors(args.folder)

    if not author_folders:
        print("No author folders found.")
        sys.exit(1)

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Count total posts across all authors for progress display
    total_posts = 0
    for af in author_folders:
        folder_path = args.folder / af
        if folder_path.is_dir():
            total_posts += min(args.max_posts, sum(1 for f in folder_path.iterdir() if f.suffix == ".md"))

    print(f"Extract Problems - Analyzing {len(author_folders)} authors ({total_posts} posts, 1 API call each)", flush=True)
    print(f"  Folder: {args.folder}", flush=True)
    print(f"  Output: {args.output_dir}", flush=True)
    print(f"  Model: {args.model}", flush=True)
    print(f"  Max posts per author: {args.max_posts}", flush=True)
    print(f"  Max parallel API calls: {args.max_parallel}", flush=True)
    print(flush=True)

    client = anthropic.AsyncAnthropic(api_key=api_key)
    # Semaphore controls total concurrent API calls across all authors
    semaphore = asyncio.Semaphore(args.max_parallel)

    async def process_author(author_folder: str) -> dict:
        try:
            result = await analyze_author(
                client=client,
                author_folder=author_folder,
                base_folder=args.folder,
                max_posts=args.max_posts,
                model=args.model,
                verbose=args.verbose,
                semaphore=semaphore,
            )
            # Save JSON
            clean_name = author_folder.replace("substack_posts_", "")
            out_path = args.output_dir / f"{clean_name}.json"
            out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
            return result
        except Exception as e:
            clean_name = author_folder.replace("substack_posts_", "")
            print(f"  [ERROR] {clean_name}: {e}", flush=True)
            return {
                "author": clean_name,
                "folder": author_folder,
                "analyzed_at": datetime.now().isoformat(),
                "posts_analyzed": 0,
                "posts_truncated": 0,
                "problems": [],
                "error": str(e),
            }

    # Run with progress
    if RICH_AVAILABLE and not args.verbose:
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(bar_width=30),
            TaskProgressColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Analyzing authors...", total=len(author_folders))
            results = []

            # Process in batches controlled by semaphore
            tasks = []
            for af in author_folders:
                tasks.append(process_author(af))

            for coro in asyncio.as_completed(tasks):
                result = await coro
                results.append(result)
                clean = result.get("author", "?")
                n_problems = len(result.get("problems", []))
                progress.update(task, advance=1, description=f"Done: {clean} ({n_problems} problems)")
    else:
        tasks = [process_author(af) for af in author_folders]
        results = await asyncio.gather(*tasks)

    # Print summary
    print_summary(list(results))

    # Final count
    successes = sum(1 for r in results if "error" not in r)
    print(f"Saved {successes}/{len(author_folders)} author results to {args.output_dir}/")

    return 0 if successes == len(author_folders) else 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
