# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "rich",
#   "pyarrow",
# ]
# ///

"""
Explore outputs/ and outputs_old/ folders.
Stats: tweets per user, context tweets, general overview.
"""

# %%
import json
from pathlib import Path
from collections import defaultdict
import pandas as pd
from rich.console import Console
from rich.table import Table
from rich import print as rprint

console = Console()

BASE = Path(__file__).parent
OUTPUTS     = BASE / "outputs"
OUTPUTS_OLD = BASE / "outputs_old"

# %%
# ── Helpers ──────────────────────────────────────────────────────────────────

def load_jsonl(path: Path) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return records


def tweet_type(record: dict) -> str:
    if "retweeted" in record and record["retweeted"]:
        return "retweet"
    if record.get("in_reply_to_status_id_str"):
        return "reply"
    return "original"


def collect_user_stats(tweets_dir: Path, context_dir: Path, source_label: str) -> pd.DataFrame:
    rows = []

    # Merge all known usernames
    all_users = set()
    if tweets_dir.exists():
        all_users |= {p.stem for p in tweets_dir.glob("*.jsonl")}
    if context_dir.exists():
        all_users |= {p.stem for p in context_dir.glob("*.jsonl")}

    for user in sorted(all_users):
        # ── tweets ──
        tweet_path = tweets_dir / f"{user}.jsonl" if tweets_dir.exists() else None
        tweets = load_jsonl(tweet_path) if tweet_path and tweet_path.exists() else []

        tweet_ids = {t["tweet_id"] for t in tweets}
        n_original = sum(1 for t in tweets if tweet_type(t) == "original")
        n_reply    = sum(1 for t in tweets if tweet_type(t) == "reply")
        n_retweet  = sum(1 for t in tweets if tweet_type(t) == "retweet")

        dates = []
        for t in tweets:
            upd = t.get("updated_at") or t.get("created_at")
            if upd:
                try:
                    dates.append(pd.to_datetime(upd, utc=True))
                except Exception:
                    pass
        min_date = min(dates).date() if dates else None
        max_date = max(dates).date() if dates else None

        total_views = sum(
            int(t["views"]) for t in tweets if t.get("views") and str(t["views"]).isdigit()
        )
        total_likes = sum(t.get("favorites", 0) or 0 for t in tweets)

        # ── context tweets ──
        ctx_path = context_dir / f"{user}.jsonl" if context_dir.exists() else None
        ctx_tweets = load_jsonl(ctx_path) if ctx_path and ctx_path.exists() else []

        ctx_ids = {t["tweet_id"] for t in ctx_tweets}
        ctx_unique_authors = {
            t.get("author", {}).get("screen_name") for t in ctx_tweets
            if t.get("author", {}).get("screen_name")
        }

        rows.append({
            "source": source_label,
            "user": user,
            "n_tweets": len(tweets),
            "n_original": n_original,
            "n_reply": n_reply,
            "n_retweet": n_retweet,
            "n_unique_tweet_ids": len(tweet_ids),
            "total_views": total_views,
            "total_likes": total_likes,
            "date_min": min_date,
            "date_max": max_date,
            "n_context_tweets": len(ctx_tweets),
            "n_context_unique_ids": len(ctx_ids),
            "n_context_authors": len(ctx_unique_authors),
        })

    return pd.DataFrame(rows)


# %%
# ── Load both sources ─────────────────────────────────────────────────────────

console.rule("[bold]Loading outputs/")
df_new = collect_user_stats(
    OUTPUTS / "tweets_live",
    OUTPUTS / "context_tweets_live",
    source_label="outputs",
)

console.rule("[bold]Loading outputs_old/")
df_old = collect_user_stats(
    OUTPUTS_OLD / "tweets_live",
    OUTPUTS_OLD / "context_tweets_live",
    source_label="outputs_old",
)

# Also load the parquets from outputs_old if present
parquet_tweets_path = OUTPUTS_OLD / "tweets_2months.parquet"
parquet_ctx_path    = OUTPUTS_OLD / "context_tweets.parquet"

df_parquet_tweets = pd.read_parquet(parquet_tweets_path) if parquet_tweets_path.exists() else None
df_parquet_ctx    = pd.read_parquet(parquet_ctx_path)    if parquet_ctx_path.exists()    else None

df_all = pd.concat([df_new, df_old], ignore_index=True)

# %%
# ── General stats ─────────────────────────────────────────────────────────────

console.rule("[bold cyan]GENERAL STATS", style="cyan")

for label, df in [("outputs (live)", df_new), ("outputs_old (live)", df_old)]:
    rprint(f"\n[bold underline]{label}[/]")
    rprint(f"  Users with tweet files:        {(df['n_tweets'] > 0).sum()}")
    rprint(f"  Users with context files:      {(df['n_context_tweets'] > 0).sum()}")
    rprint(f"  Total tweet records:           {df['n_tweets'].sum():,}")
    rprint(f"    ↳ Original:                  {df['n_original'].sum():,}")
    rprint(f"    ↳ Replies:                   {df['n_reply'].sum():,}")
    rprint(f"    ↳ Retweets:                  {df['n_retweet'].sum():,}")
    rprint(f"  Unique tweet IDs:              {df['n_unique_tweet_ids'].sum():,}")
    rprint(f"  Total context tweet records:   {df['n_context_tweets'].sum():,}")
    rprint(f"  Unique context IDs:            {df['n_context_unique_ids'].sum():,}")
    rprint(f"  Total views (w/ data):         {df['total_views'].sum():,.0f}")
    rprint(f"  Total likes:                   {df['total_likes'].sum():,.0f}")
    valid_dates = df.dropna(subset=["date_min", "date_max"])
    if not valid_dates.empty:
        rprint(f"  Date range:                    {valid_dates['date_min'].min()}  →  {valid_dates['date_max'].max()}")

# Parquet summary
if df_parquet_tweets is not None:
    rprint(f"\n[bold underline]outputs_old/tweets_2months.parquet[/]")
    rprint(f"  Rows:     {len(df_parquet_tweets):,}")
    rprint(f"  Users:    {df_parquet_tweets['username'].nunique():,}")
    if "created_at" in df_parquet_tweets.columns:
        dates = pd.to_datetime(df_parquet_tweets["created_at"], utc=True, errors="coerce").dropna()
        if not dates.empty:
            rprint(f"  Date range:  {dates.min().date()}  →  {dates.max().date()}")

if df_parquet_ctx is not None:
    rprint(f"\n[bold underline]outputs_old/context_tweets.parquet[/]")
    rprint(f"  Rows:  {len(df_parquet_ctx):,}")
    col_check = "username" if "username" in df_parquet_ctx.columns else None
    if col_check:
        rprint(f"  Users: {df_parquet_ctx[col_check].nunique():,}")

# %%
# ── Per-user table ─────────────────────────────────────────────────────────────

def make_rich_table(df: pd.DataFrame, title: str) -> Table:
    table = Table(title=title, show_lines=False, header_style="bold magenta")
    table.add_column("User",           style="cyan", no_wrap=True)
    table.add_column("Tweets",         justify="right")
    table.add_column("Original",       justify="right")
    table.add_column("Replies",        justify="right")
    table.add_column("RTs",            justify="right")
    table.add_column("Views",          justify="right")
    table.add_column("Likes",          justify="right")
    table.add_column("Context",        justify="right")
    table.add_column("Ctx Authors",    justify="right")
    table.add_column("Date Min",       justify="center")
    table.add_column("Date Max",       justify="center")

    df_sorted = df.sort_values("n_tweets", ascending=False)
    for _, row in df_sorted.iterrows():
        table.add_row(
            row["user"],
            f"{row['n_tweets']:,}",
            f"{row['n_original']:,}",
            f"{row['n_reply']:,}",
            f"{row['n_retweet']:,}",
            f"{int(row['total_views']):,}" if row["total_views"] else "—",
            f"{int(row['total_likes']):,}" if row["total_likes"] else "—",
            f"{row['n_context_tweets']:,}",
            f"{row['n_context_authors']:,}",
            str(row["date_min"]) if row["date_min"] else "—",
            str(row["date_max"]) if row["date_max"] else "—",
        )
    return table


console.rule("[bold cyan]PER-USER TABLE — outputs/", style="cyan")
console.print(make_rich_table(df_new, "outputs/ (live tweets)"))

console.rule("[bold cyan]PER-USER TABLE — outputs_old/", style="cyan")
console.print(make_rich_table(df_old, "outputs_old/ (live tweets)"))

# %%
# ── Users only in one source ──────────────────────────────────────────────────

users_new = set(df_new["user"])
users_old = set(df_old["user"])
only_new  = users_new - users_old
only_old  = users_old - users_new
both      = users_new & users_old

console.rule("[bold cyan]OVERLAP ANALYSIS", style="cyan")
rprint(f"  Users in outputs only:         {len(only_new)}")
rprint(f"  Users in outputs_old only:     {len(only_old)}")
rprint(f"  Users in both:                 {len(both)}")

if only_new:
    rprint(f"\n  [green]Only in outputs/:[/]  {', '.join(sorted(only_new)[:20])}")
if only_old:
    rprint(f"\n  [yellow]Only in outputs_old/:[/]  {', '.join(sorted(only_old)[:20])}")

# %%
# ── Difference per shared user ────────────────────────────────────────────────

console.rule("[bold cyan]TWEET DELTA (outputs vs outputs_old) — shared users", style="cyan")

merge = df_new.set_index("user")[["n_tweets", "n_context_tweets"]].rename(
    columns={"n_tweets": "new_tweets", "n_context_tweets": "new_ctx"}
).join(
    df_old.set_index("user")[["n_tweets", "n_context_tweets"]].rename(
        columns={"n_tweets": "old_tweets", "n_context_tweets": "old_ctx"}
    ),
    how="inner"
)
merge["delta_tweets"] = merge["new_tweets"] - merge["old_tweets"]
merge["delta_ctx"]    = merge["new_ctx"]    - merge["old_ctx"]
merge = merge.sort_values("delta_tweets", ascending=False)

delta_table = Table(title="Tweet count delta (outputs − outputs_old)", show_lines=False, header_style="bold magenta")
delta_table.add_column("User",          style="cyan", no_wrap=True)
delta_table.add_column("outputs",       justify="right")
delta_table.add_column("outputs_old",   justify="right")
delta_table.add_column("Δ tweets",      justify="right")
delta_table.add_column("Δ context",     justify="right")

for user, row in merge.iterrows():
    delta_col = "[green]" if row["delta_tweets"] >= 0 else "[red]"
    delta_table.add_row(
        user,
        f"{int(row['new_tweets']):,}",
        f"{int(row['old_tweets']):,}",
        f"{delta_col}{int(row['delta_tweets']):+,}[/]",
        f"{int(row['delta_ctx']):+,}",
    )
console.print(delta_table)

rprint(f"\nDone. Total users analysed: [bold]{len(df_all['user'].unique())}[/]")
