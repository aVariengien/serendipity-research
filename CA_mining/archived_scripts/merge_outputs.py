# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "orjson",
#   "tqdm",
#   "rich",
# ]
# ///

"""
Merge all past_outputs/ snapshots into a single outputs_merged/ folder.
For each user, takes the union of tweet IDs across all snapshots.
When the same tweet_id appears in multiple snapshots, keeps the most
recent scrape's version (priority: outputs_3march > outputs_fresh > outputs_old).
"""

# %%
import shutil
from pathlib import Path
import orjson
from tqdm import tqdm
from rich.console import Console
from rich import print as rprint

console = Console()

BASE         = Path(__file__).parent
PAST_OUTPUTS = BASE / "past_outputs"
MERGED_DIR   = BASE / "past_outputs" / "outputs_merged"

# Priority order: lowest first (will be overwritten by higher-priority snapshots)
SNAPSHOT_PRIORITY = ["outputs_old", "outputs_fresh", "outputs_3march"]

# %%
# ── Validate sources ──────────────────────────────────────────────────────────

sources = []
for name in SNAPSHOT_PRIORITY:
    d = PAST_OUTPUTS / name
    if not d.exists():
        rprint(f"[yellow]Warning: {d} not found, skipping.[/]")
    else:
        sources.append(d)

if not sources:
    raise SystemExit("No snapshot folders found.")

console.rule(f"[bold]Merging {len(sources)} snapshots → outputs_merged/")
for s in sources:
    rprint(f"  [dim]{s.name}[/]  (priority {SNAPSHOT_PRIORITY.index(s.name) + 1})")

# %%
# ── Create output dirs ────────────────────────────────────────────────────────

tweets_out  = MERGED_DIR / "tweets_live"
context_out = MERGED_DIR / "context_tweets_live"

if MERGED_DIR.exists():
    rprint(f"\n[yellow]outputs_merged/ already exists — removing and recreating.[/]")
    shutil.rmtree(MERGED_DIR)

tweets_out.mkdir(parents=True)
context_out.mkdir(parents=True)
rprint(f"[green]Created[/] {MERGED_DIR}\n")

# %%
# ── Collect all usernames across all snapshots ────────────────────────────────

all_users: set[str] = set()
for src in sources:
    for sub in ("tweets_live", "context_tweets_live"):
        d = src / sub
        if d.exists():
            all_users |= {p.stem for p in d.glob("*.jsonl")}

rprint(f"Total unique users across all snapshots: [bold]{len(all_users)}[/]\n")

# %%
# ── Merge ─────────────────────────────────────────────────────────────────────

stats = {"users_written": 0, "tweets_written": 0, "ctx_written": 0,
         "tweets_deduped": 0, "ctx_deduped": 0}

for user in tqdm(sorted(all_users), desc="Merging users"):

    # ── tweets ──────────────────────────────────────────────────────────────
    # Dict preserves the last-written version per tweet_id.
    # Since we iterate sources in priority order (low → high), the highest-
    # priority snapshot overwrites duplicates.
    tweet_map: dict[str, bytes] = {}

    for src in sources:
        path = src / "tweets_live" / f"{user}.jsonl"
        if not path.exists():
            continue
        with open(path, "rb") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    tid = orjson.loads(raw).get("tweet_id")
                except Exception:
                    continue
                if tid:
                    tweet_map[tid] = raw

    # ── context tweets ───────────────────────────────────────────────────────
    ctx_map: dict[str, bytes] = {}

    for src in sources:
        path = src / "context_tweets_live" / f"{user}.jsonl"
        if not path.exists():
            continue
        with open(path, "rb") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    tid = orjson.loads(raw).get("tweet_id")
                except Exception:
                    continue
                if tid:
                    ctx_map[tid] = raw

    # ── write merged files ───────────────────────────────────────────────────
    if tweet_map:
        out = tweets_out / f"{user}.jsonl"
        with open(out, "wb") as f:
            for raw in tweet_map.values():
                f.write(raw)
                f.write(b"\n")
        stats["tweets_written"] += len(tweet_map)

    if ctx_map:
        out = context_out / f"{user}.jsonl"
        with open(out, "wb") as f:
            for raw in ctx_map.values():
                f.write(raw)
                f.write(b"\n")
        stats["ctx_written"] += len(ctx_map)

    stats["users_written"] += 1

# %%
# ── Summary ───────────────────────────────────────────────────────────────────

console.rule("[bold cyan]MERGE COMPLETE", style="cyan")
rprint(f"  Output folder :  [bold]{MERGED_DIR}[/]")
rprint(f"  Users written :  [bold]{stats['users_written']:,}[/]")
rprint(f"  Tweet records :  [bold]{stats['tweets_written']:,}[/]")
rprint(f"  Context records: [bold]{stats['ctx_written']:,}[/]")

# Quick sanity check against per-snapshot counts
individual_totals = {}
for src in sources:
    td = src / "tweets_live"
    if td.exists():
        n = sum(1 for p in td.glob("*.jsonl")
                for _ in open(p, "rb"))
        individual_totals[src.name] = n

rprint(f"\n  Per-snapshot tweet counts (for reference):")
for name, n in individual_totals.items():
    rprint(f"    {name}: {n:,}")
rprint(f"  Merged (unique): [bold green]{stats['tweets_written']:,}[/]")
