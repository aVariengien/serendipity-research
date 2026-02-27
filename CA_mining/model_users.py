# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "openai",
#   "tqdm",
# ]
# ///

# %% Imports & config
from __future__ import annotations

import os
import time
from pathlib import Path

from openai import OpenAI, RateLimitError, APIError
from tqdm import tqdm

USERS_DIR = Path(__file__).parent / "outputs" / "users"
MODELS_DIR = Path(__file__).parent / "outputs" / "models"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

MODEL = "zai-glm-4.7"
CHARS_PER_TOKEN = 4
CHUNK_SIZE_TOKENS = 50_000
CHUNK_SIZE_CHARS = CHUNK_SIZE_TOKENS * CHARS_PER_TOKEN  # 200_000

client = OpenAI(
    api_key=os.environ["CEREBRAS_API_KEY"],
    base_url="https://api.cerebras.ai/v1",
)


# %% Prompts

EXTRACT_SYSTEM = """\
You are extracting the intellectual portrait of a Twitter user from their tweets.

Your goal: find the JUICE. Not a summary — a portrait of what's alive to them.

Weight costly signals heavily:
- Long tweets and threads = they spent real mental effort here
- Topics that appear at multiple distinct time points = persistent obsession, not just reaction
- Sources, papers, people, links they cite with genuine engagement (not just casual mention)
- Arguments they make repeatedly = deep conviction
- Questions they keep asking = live uncertainty

Output a compact, dense portrait in markdown. Use their actual words and phrases.
No padding. No generic observations. Favor specificity.

## What's Alive Right Now
The 2-4 topics they're most actively thinking/writing about in the most recent tweets.

## Recurring Obsessions
Themes that appear across multiple time periods — what they keep returning to.

## Sources & Things That Struck Them
Papers, books, people, links, ideas they reference with genuine engagement. Be specific.

## Their Vocabulary
The distinctive words, phrases, and framings they use. What conceptual language is theirs?

## Where They Spend Real Time
Their longest threads and most elaborated thoughts. What did they work through carefully?
"""

SYNTHESIS_SYSTEM = """\
You have partial analyses of a Twitter user's tweets from multiple chunks.
Synthesize into a single, coherent intellectual portrait.

Prioritize:
- What appears in MULTIPLE chunks = persistent signal
- Costly elaborated thinking (threads, long arguments)
- Distinctive vocabulary that recurs

Collapse redundancy. Preserve specificity. Use their actual words.

Output the same sections as the input analyses, but unified and distilled.

## What's Alive Right Now
## Recurring Obsessions
## Sources & Things That Struck Them
## Their Vocabulary
## Where They Spend Real Time
"""


# %% Core functions

def chunk_text(text: str, chunk_size: int = CHUNK_SIZE_CHARS) -> list[str]:
    """Split text into chunks, trying to break at tweet separators (---) when possible."""
    if len(text) <= chunk_size:
        return [text]

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        if end >= len(text):
            chunks.append(text[start:])
            break
        # Try to split at a tweet separator near the end of the chunk
        sep = text.rfind("\n---\n", start + chunk_size // 2, end)
        if sep != -1:
            end = sep + 5  # include the separator in the chunk
        chunks.append(text[start:end])
        start = end

    return chunks


def call_api(system: str, user: str, max_retries: int = 5) -> str:
    """Call the Cerebras API with exponential backoff on rate-limit errors."""
    delay = 5
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                max_tokens=2_000,
                temperature=0.7,
                extra_body={"disable_reasoning": False},
            )
            return response.choices[0].message.content or ""
        except RateLimitError:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 120)
        except APIError as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 120)
    return ""


def analyze_chunk(chunk: str, username: str, chunk_num: int, total_chunks: int) -> str:
    label = f"@{username}"
    if total_chunks > 1:
        label += f" — part {chunk_num}/{total_chunks}"
    user_msg = f"Twitter user: {label}\n\n{chunk}"
    return call_api(EXTRACT_SYSTEM, user_msg)


def synthesize_chunks(partial_analyses: list[str], username: str) -> str:
    combined = "\n\n---\n\n".join(
        f"### Part {i + 1}\n{a}" for i, a in enumerate(partial_analyses)
    )
    user_msg = f"Twitter user: @{username}\n\nPartial analyses:\n\n{combined}"
    return call_api(SYNTHESIS_SYSTEM, user_msg)


def process_user(md_path: Path, pbar: tqdm) -> None:
    username = md_path.stem
    out_path = MODELS_DIR / f"{username}.md"

    if out_path.exists():
        pbar.set_postfix_str(f"skip {username}")
        return

    pbar.set_postfix_str(username)
    text = md_path.read_text(encoding="utf-8")
    file_chars = len(text)
    chunks = chunk_text(text)

    if len(chunks) == 1:
        analysis = analyze_chunk(chunks[0], username, 1, 1)
    else:
        partial: list[str] = []
        for i, chunk in enumerate(chunks, 1):
            pbar.set_postfix_str(f"{username} chunk {i}/{len(chunks)}")
            partial.append(analyze_chunk(chunk, username, i, len(chunks)))
        pbar.set_postfix_str(f"{username} synthesizing")
        analysis = synthesize_chunks(partial, username)

    approx_tokens = file_chars // CHARS_PER_TOKEN
    header = (
        f"# @{username} — Intellectual Portrait\n\n"
        f"_Source: {file_chars:,} chars (~{approx_tokens:,} tokens), "
        f"{len(chunks)} chunk(s)_\n\n"
    )
    out_path.write_text(header + analysis, encoding="utf-8")


# %% Main

user_files = sorted(USERS_DIR.glob("*.md"))
already_done = sum(1 for f in user_files if (MODELS_DIR / f.name).exists())

print(f"Found {len(user_files)} user files")
print(f"Already processed: {already_done} — skipping those")
print(f"To process: {len(user_files) - already_done}")
print(f"Output dir: {MODELS_DIR}\n")

with tqdm(user_files, unit=" users", dynamic_ncols=True) as pbar:
    for md_path in pbar:
        try:
            process_user(md_path, pbar)
        except Exception as e:
            tqdm.write(f"ERROR processing {md_path.stem}: {e}")

print(f"\nDone! Portraits saved to {MODELS_DIR}/")
