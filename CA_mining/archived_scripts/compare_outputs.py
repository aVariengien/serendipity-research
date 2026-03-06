# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "rich",
#   "tqdm",
#   "orjson",
# ]
# ///

"""
Pairwise comparison of all snapshot folders inside past_outputs/.
For every pair (A, B) shows:
  - users added / removed / shared
  - tweets gained / lost  (by tweet_id)
  - context tweets gained / lost
  - per-user delta table (sorted by tweet gain)
"""

# %%
import re
from pathlib import Path
from itertools import combinations
from tqdm import tqdm
import orjson
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich import print as rprint

console = Console()

BASE         = Path(__file__).parent
PAST_OUTPUTS = BASE / "past_outputs"

# %%
# ── Load all snapshots ────────────────────────────────────────────────────────

# Regex to pull tweet_id out of a context line without full JSON parse
_CTX_ID_RE = re.compile(rb'"tweet_id"\s*:\s*"(\d+)"')


def _parse_tweet_line(raw: bytes) -> tuple | None:
    """
    Parse only the fields we need from a tweet JSON line.
    Returns (tweet_id, type, date_str) or None on error.
    type is one of: 'original' | 'reply' | 'retweet'
    """
    try:
        r = orjson.loads(raw)
    except Exception:
        return None
    tid = r.get("tweet_id")
    if not tid:
        return None
    if r.get("retweeted"):
        ttype = "retweet"
    elif r.get("in_reply_to_status_id_str"):
        ttype = "reply"
    else:
        ttype = "original"
    date_str = r.get("updated_at") or r.get("created_at") or ""
    return tid, ttype, date_str


def load_snapshot(folder: Path) -> dict:
    """
    Returns:
      tweets     : {username -> set of tweet_ids}
      context    : {username -> set of tweet_ids}
      tweet_slim : {username -> {tweet_id -> (type, date_str)}}  (minimal meta)
    """
    tweets     = {}
    context    = {}
    tweet_slim = {}

    tweets_dir  = folder / "tweets_live"
    context_dir = folder / "context_tweets_live"

    all_users = set()
    if tweets_dir.exists():
        all_users |= {p.stem for p in tweets_dir.glob("*.jsonl")}
    if context_dir.exists():
        all_users |= {p.stem for p in context_dir.glob("*.jsonl")}

    for user in tqdm(sorted(all_users), desc=f"  loading {folder.name}", leave=False):
        # ── tweets: parse minimal fields only ────────────────────────────────
        tp = tweets_dir / f"{user}.jsonl"
        slim: dict[str, tuple] = {}
        if tp.exists():
            with open(tp, "rb") as f:          # binary read → orjson is faster
                for raw in f:
                    parsed = _parse_tweet_line(raw)
                    if parsed:
                        tid, ttype, date_str = parsed
                        slim[tid] = (ttype, date_str)
        tweets[user]     = set(slim)
        tweet_slim[user] = slim

        # ── context: only need tweet_id, use regex to avoid full JSON parse ──
        cp = context_dir / f"{user}.jsonl"
        c_ids: set[str] = set()
        if cp.exists():
            with open(cp, "rb") as f:
                for raw in f:
                    m = _CTX_ID_RE.search(raw)
                    if m:
                        c_ids.add(m.group(1).decode())
        context[user] = c_ids

    return {"tweets": tweets, "context": context, "tweet_slim": tweet_slim}


def date_range_from_slim(slim: dict) -> tuple:
    """Compute date range from slim meta. Only parses the min/max date strings."""
    iso_dates = [v[1] for v in slim.values() if v[1].startswith("20")]
    if not iso_dates:
        # Fallback: try parsing Twitter-format created_at strings
        all_dates = [v[1] for v in slim.values() if v[1]]
        try:
            parsed = [pd.to_datetime(d, utc=True) for d in all_dates if d]
            return (min(parsed).date(), max(parsed).date()) if parsed else (None, None)
        except Exception:
            return None, None
    iso_dates.sort()
    try:
        dmin = pd.to_datetime(iso_dates[0],  utc=True).date()
        dmax = pd.to_datetime(iso_dates[-1], utc=True).date()
        return dmin, dmax
    except Exception:
        return None, None


# ── discover snapshot folders ─────────────────────────────────────────────────
snapshot_dirs = sorted([d for d in PAST_OUTPUTS.iterdir() if d.is_dir()])
console.rule(f"[bold]Found {len(snapshot_dirs)} snapshots: {[d.name for d in snapshot_dirs]}")

snapshots = {}
for sd in snapshot_dirs:
    console.print(f"[cyan]Loading[/] {sd.name} …")
    snapshots[sd.name] = load_snapshot(sd)

# %%
# ── General per-snapshot stats ────────────────────────────────────────────────

console.rule("[bold cyan]SNAPSHOT OVERVIEW", style="cyan")

overview = Table(show_lines=False, header_style="bold magenta")
overview.add_column("Snapshot",         style="cyan")
overview.add_column("Users (tweets)",   justify="right")
overview.add_column("Users (context)",  justify="right")
overview.add_column("Total tweets",     justify="right")
overview.add_column("Unique IDs",       justify="right")
overview.add_column("Total ctx tweets", justify="right")
overview.add_column("Date min",         justify="center")
overview.add_column("Date max",         justify="center")

for name, snap in snapshots.items():
    all_tweet_ids = set().union(*snap["tweets"].values()) if snap["tweets"] else set()
    total_records = sum(len(v) for v in snap["tweets"].values())
    total_ctx     = sum(len(v) for v in snap["context"].values())
    merged_slim   = {tid: meta for u in snap["tweet_slim"].values() for tid, meta in u.items()}
    dmin, dmax    = date_range_from_slim(merged_slim)
    overview.add_row(
        name,
        str(len(snap["tweets"])),
        str(len(snap["context"])),
        f"{total_records:,}",
        f"{len(all_tweet_ids):,}",
        f"{total_ctx:,}",
        str(dmin) if dmin else "—",
        str(dmax) if dmax else "—",
    )

console.print(overview)

# %%
# ── Pairwise comparison ───────────────────────────────────────────────────────

pairs = list(combinations(snapshot_dirs, 2))
console.rule(f"[bold cyan]{len(pairs)} PAIRWISE COMPARISONS", style="cyan")

for dir_a, dir_b in pairs:
    name_a, name_b = dir_a.name, dir_b.name
    snap_a, snap_b = snapshots[name_a], snapshots[name_b]

    users_a = set(snap_a["tweets"]) | set(snap_a["context"])
    users_b = set(snap_b["tweets"]) | set(snap_b["context"])

    only_a  = users_a - users_b
    only_b  = users_b - users_a
    shared  = users_a & users_b

    all_ids_a = set().union(*snap_a["tweets"].values()) if snap_a["tweets"] else set()
    all_ids_b = set().union(*snap_b["tweets"].values()) if snap_b["tweets"] else set()
    all_ctx_a = set().union(*snap_a["context"].values()) if snap_a["context"] else set()
    all_ctx_b = set().union(*snap_b["context"].values()) if snap_b["context"] else set()

    new_tweet_ids   = all_ids_b - all_ids_a    # in B but not A
    lost_tweet_ids  = all_ids_a - all_ids_b    # in A but not B
    new_ctx_ids     = all_ctx_b - all_ctx_a
    lost_ctx_ids    = all_ctx_a - all_ctx_b

    console.print()
    console.rule(f"[bold yellow]{name_a}  →  {name_b}", style="yellow")

    # High-level summary
    summary = Table(show_lines=False, header_style="bold")
    summary.add_column("Metric", style="dim")
    summary.add_column(name_a,   justify="right", style="blue")
    summary.add_column(name_b,   justify="right", style="green")
    summary.add_column("Δ (B−A)", justify="right")

    def delta_str(a, b):
        d = b - a
        color = "green" if d > 0 else ("red" if d < 0 else "dim")
        return f"[{color}]{d:+,}[/]"

    ta = sum(len(v) for v in snap_a["tweets"].values())
    tb = sum(len(v) for v in snap_b["tweets"].values())
    ca = sum(len(v) for v in snap_a["context"].values())
    cb = sum(len(v) for v in snap_b["context"].values())

    summary.add_row("Users",              f"{len(users_a):,}", f"{len(users_b):,}", delta_str(len(users_a), len(users_b)))
    summary.add_row("Tweet records",      f"{ta:,}",           f"{tb:,}",           delta_str(ta, tb))
    summary.add_row("Unique tweet IDs",   f"{len(all_ids_a):,}", f"{len(all_ids_b):,}", delta_str(len(all_ids_a), len(all_ids_b)))
    summary.add_row("New tweet IDs in B", "—", f"{len(new_tweet_ids):,}", f"[green]+{len(new_tweet_ids):,}[/]")
    summary.add_row("Lost tweet IDs",     f"{len(lost_tweet_ids):,}", "—", f"[red]-{len(lost_tweet_ids):,}[/]")
    summary.add_row("Context records",    f"{ca:,}", f"{cb:,}", delta_str(ca, cb))
    summary.add_row("New context IDs",    "—", f"{len(new_ctx_ids):,}", f"[green]+{len(new_ctx_ids):,}[/]")
    summary.add_row("Lost context IDs",   f"{len(lost_ctx_ids):,}", "—", f"[red]-{len(lost_ctx_ids):,}[/]")
    summary.add_row("Users only in A",    f"{len(only_a)}", "—", "")
    summary.add_row("Users only in B",    "—", f"{len(only_b)}", "")
    summary.add_row("Shared users",       f"{len(shared):,}", f"{len(shared):,}", "")
    console.print(summary)

    if only_a:
        rprint(f"  [blue]Only in {name_a}:[/] {', '.join(sorted(only_a)[:30])}{'…' if len(only_a)>30 else ''}")
    if only_b:
        rprint(f"  [green]Only in {name_b}:[/] {', '.join(sorted(only_b)[:30])}{'…' if len(only_b)>30 else ''}")

    # ── Per-user delta table ──────────────────────────────────────────────────
    per_user_rows = []
    for user in sorted(shared):
        ids_a = snap_a["tweets"].get(user, set())
        ids_b = snap_b["tweets"].get(user, set())
        ctx_a = snap_a["context"].get(user, set())
        ctx_b = snap_b["context"].get(user, set())

        gained   = ids_b - ids_a
        lost     = ids_a - ids_b
        ctx_gain = ctx_b - ctx_a
        ctx_lost = ctx_a - ctx_b

        # type breakdown of gained tweets — read directly from slim meta
        slim_b       = snap_b["tweet_slim"].get(user, {})
        gained_orig  = sum(1 for tid in gained if slim_b.get(tid, ("original",))[0] == "original")
        gained_reply = sum(1 for tid in gained if slim_b.get(tid, ("original",))[0] == "reply")
        gained_rt    = sum(1 for tid in gained if slim_b.get(tid, ("original",))[0] == "retweet")

        per_user_rows.append({
            "user":       user,
            "tweets_a":   len(ids_a),
            "tweets_b":   len(ids_b),
            "gained":     len(gained),
            "gained_orig":  gained_orig,
            "gained_reply": gained_reply,
            "gained_rt":    gained_rt,
            "lost":       len(lost),
            "ctx_gain":   len(ctx_gain),
            "ctx_lost":   len(ctx_lost),
        })

    df_pu = pd.DataFrame(per_user_rows).sort_values("gained", ascending=False)

    user_table = Table(
        title=f"Per-user delta: {name_a} → {name_b} (sorted by tweets gained)",
        show_lines=False, header_style="bold magenta"
    )
    user_table.add_column("User",           style="cyan", no_wrap=True)
    user_table.add_column(f"{name_a}",      justify="right")
    user_table.add_column(f"{name_b}",      justify="right")
    user_table.add_column("Gained",         justify="right", style="green")
    user_table.add_column("+orig",          justify="right")
    user_table.add_column("+reply",         justify="right")
    user_table.add_column("+RT",            justify="right")
    user_table.add_column("Lost",           justify="right", style="red")
    user_table.add_column("Ctx +",          justify="right")
    user_table.add_column("Ctx −",          justify="right")

    for _, row in df_pu.iterrows():
        user_table.add_row(
            row["user"],
            f"{int(row['tweets_a']):,}",
            f"{int(row['tweets_b']):,}",
            f"+{int(row['gained']):,}",
            f"+{int(row['gained_orig']):,}",
            f"+{int(row['gained_reply']):,}",
            f"+{int(row['gained_rt']):,}",
            f"-{int(row['lost']):,}",
            f"+{int(row['ctx_gain']):,}",
            f"-{int(row['ctx_lost']):,}",
        )
    console.print(user_table)

rprint("\n[bold green]Done.[/]")
