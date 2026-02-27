# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "polars",
#   "pyarrow",
#   "tqdm",
# ]
# ///

# %% Imports & config
from __future__ import annotations

import json
import re
import textwrap
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import polars as pl
from tqdm import tqdm

OUT_DIR = Path(__file__).parent / "outputs"
USERS_DIR = OUT_DIR / "users"
USERS_DIR.mkdir(parents=True, exist_ok=True)

CUTOFF = datetime(2025, 12, 26, tzinfo=timezone.utc)
INDENT = "    "
BRANCH_CONNECTOR = "└─ "
SINGLE_ARROW = "↓"

EXCERPT_MAX_CHARS = 300  # max chars shown per URL preview line


# %% Load URL cache (built by resolve_urls.py)
_url_cache: dict[str, dict] = {}
_cache_path = OUT_DIR / "url_cache.json"
if _cache_path.exists():
    _url_cache = json.loads(_cache_path.read_text())
    _cached_links = sum(1 for d in _url_cache.values() if d.get("type") == "link")
    _cached_imgs = sum(1 for d in _url_cache.values() if d.get("type") == "image")
    print(f"URL cache loaded: {len(_url_cache):,} entries "
          f"({_cached_links:,} links, {_cached_imgs:,} images)")
else:
    print("No url_cache.json found — t.co URLs will not be resolved. "
          "Run resolve_urls.py first to enable URL previews.")


def _short_domain(url: str) -> str:
    try:
        host = urlparse(url).netloc.lstrip("www.")
        path = urlparse(url).path
        if path and path != "/":
            slug = path.rstrip("/").rsplit("/", 1)[-1][:40]
            return f"{host}/{slug}" if slug else host
        return host
    except Exception:
        return url[:40]


def annotate_urls(text: str, body_pad: str) -> tuple[str, str]:
    """Replace t.co URLs in tweet text with resolved links.

    Returns (annotated_text, url_previews_block) where url_previews_block
    contains one line per link with title/excerpt (empty string if none).
    """
    if not _url_cache:
        return text, ""

    previews: list[str] = []
    seen_tco: set[str] = set()

    def replace(m: re.Match) -> str:
        tco = m.group(0)
        data = _url_cache.get(tco, {})
        resolved = data.get("resolved")
        if not resolved:
            return tco

        url_type = data.get("type", "link")

        if url_type == "image":
            return f"[🖼 image]({resolved})"

        # Link
        domain_slug = _short_domain(resolved)
        inline = f"[🔗 {domain_slug}]({resolved})"

        # Build preview line (shown below tweet body)
        if tco not in seen_tco:
            seen_tco.add(tco)
            title = (data.get("title") or "").strip()
            excerpt = (data.get("excerpt") or "").strip()
            if title or excerpt:
                label = title if title else excerpt[:60]
                detail = excerpt if excerpt and excerpt != title else ""
                preview = f"{body_pad}  ↳ **{label}**"
                if detail:
                    short_detail = detail[:EXCERPT_MAX_CHARS]
                    if len(detail) > EXCERPT_MAX_CHARS:
                        short_detail += "…"
                    preview += f"\n{body_pad}    {short_detail}"
                previews.append(preview)

        return inline

    annotated = re.sub(r"https://t\.co/\w+", replace, text)
    previews_block = "\n".join(previews)
    return annotated, previews_block


# %% Load data
print("Loading parquet files …")
df_main = pl.read_parquet(OUT_DIR / "tweets_2months.parquet")
df_context = pl.read_parquet(OUT_DIR / "context_tweets.parquet")

print(f"  Main tweets   : {len(df_main):,}")
print(f"  Context tweets: {len(df_context):,}")


# %% Build a unified lookup dict: tweet_id -> row dict
def df_to_lookup(df: pl.DataFrame) -> dict[str, dict]:
    if df.is_empty():
        return {}
    # Cast nullable numeric cols to avoid type errors
    return {row["tweet_id"]: row for row in df.to_dicts()}


all_tweets: dict[str, dict] = {}
all_tweets.update(df_to_lookup(df_context))
all_tweets.update(df_to_lookup(df_main))  # main takes priority on overlap


# %% Build reply trees
# parent_id -> list of child tweet_ids
children_of: dict[str | None, list[str]] = defaultdict(list)
for tid, row in all_tweets.items():
    parent = row.get("reply_to_tweet_id")
    children_of[parent].append(tid)

def find_true_root(tweet_id: str) -> str:
    """Walk up the reply chain to find the topmost tweet we have in all_tweets."""
    current = tweet_id
    visited: set[str] = set()
    while True:
        if current in visited:
            break  # cycle guard
        visited.add(current)
        row = all_tweets.get(current)
        if row is None:
            break
        parent = row.get("reply_to_tweet_id")
        if parent is None or parent not in all_tweets:
            break
        current = parent
    return current


def find_roots(tweet_ids: set[str]) -> list[str]:
    """For a member's tweet set, find all unique thread roots (may be context tweets)."""
    seen: set[str] = set()
    roots: list[str] = []
    for tid in tweet_ids:
        root = find_true_root(tid)
        if root not in seen:
            seen.add(root)
            roots.append(root)
    return roots


def collect_thread(root_id: str, member_ids: set[str]) -> set[str]:
    """DFS to collect all tweet IDs in a conversation reachable from root."""
    visited: set[str] = set()
    stack = [root_id]
    while stack:
        tid = stack.pop()
        if tid in visited:
            continue
        visited.add(tid)
        for child in children_of.get(tid, []):
            stack.append(child)
    return visited


# %% Rendering helpers
def fmt_date(created_at: str | None) -> str:
    if not created_at:
        return "unknown date"
    try:
        dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
        return dt.strftime("%b %d, %Y %H:%M")
    except Exception:
        return str(created_at)


def fmt_metrics(row: dict) -> str:
    parts = []
    if row.get("favorite_count") is not None:
        parts.append(f"likes={row['favorite_count']:,}")
    if row.get("retweet_count") is not None:
        parts.append(f"RT={row['retweet_count']:,}")
    return "  [" + "  ".join(parts) + "]" if parts else ""


def wrap_text(text: str, width: int = 100, prefix: str = "") -> str:
    lines = text.splitlines()
    wrapped = []
    for line in lines:
        wrapped.extend(textwrap.wrap(line, width=width) or [""])
    return ("\n" + prefix).join(wrapped)


def render_tweet_block(
    row: dict,
    depth: int = 0,
    connector: str = "",
    is_context: bool = False,
) -> str:
    """Render a single tweet as a text block."""
    pad = INDENT * depth
    username = row.get("username") or row.get("reply_to_username") or "unknown"
    display = row.get("account_display_name") or username
    date = fmt_date(row.get("created_at"))
    metrics = fmt_metrics(row)
    text = row.get("full_text") or ""
    dim = " [context]" if is_context else ""

    header = f"{pad}{connector}@{username} ({display}){dim} · {date}{metrics}"
    # Align body text under the start of the username (past the connector)
    body_pad = pad + " " * len(connector)

    # Annotate t.co URLs before wrapping
    annotated_text, url_previews = annotate_urls(text, body_pad)
    body = wrap_text(annotated_text, width=100, prefix=body_pad)

    # Inline quoted tweet if present
    quoted_block = ""
    quoted_id = row.get("quoted_tweet_id")
    if quoted_id and quoted_id in all_tweets:
        q = all_tweets[quoted_id]
        q_username = q.get("username") or "unknown"
        q_date = fmt_date(q.get("created_at"))
        q_metrics = fmt_metrics(q)
        q_text = q.get("full_text") or ""
        q_annotated, q_previews = annotate_urls(q_text, body_pad + "  | ")
        q_body = wrap_text(q_annotated, width=90, prefix=body_pad + "  | ")
        quoted_block = (
            f"\n{body_pad}  [quoting @{q_username} · {q_date}{q_metrics}]\n"
            f"{body_pad}  | {q_body}"
        )
        if q_previews:
            quoted_block += f"\n{q_previews}"

    previews_section = f"\n{url_previews}" if url_previews else ""
    return f"{header}\n{body_pad}{body}{previews_section}{quoted_block}"


def render_tree(
    root_id: str,
    member_ids: set[str],
    depth: int = 0,
    connector: str | None = None,
) -> str:
    """Recursively render a tweet and its replies as a tree.

    Single-child chains stay at the same indentation level, with '↓' replacing
    the '└─' elbow. Branches (multiple children) increase indentation.
    """
    row = all_tweets.get(root_id)
    if row is None:
        return ""

    is_context = root_id not in member_ids
    # Use the explicitly passed connector if given, otherwise derive from depth
    resolved_connector = connector if connector is not None else (BRANCH_CONNECTOR if depth > 0 else "")
    block = render_tweet_block(row, depth=depth, connector=resolved_connector, is_context=is_context)

    child_ids = sorted(
        children_of.get(root_id, []),
        key=lambda tid: all_tweets.get(tid, {}).get("created_at") or "",
    )

    if not child_ids:
        return block

    if len(child_ids) == 1:
        # Single child: same depth, ↓ replaces the └─ elbow on the child
        pad = INDENT * depth
        arrow = f"{pad}{SINGLE_ARROW}"
        child_block = render_tree(child_ids[0], member_ids, depth=depth, connector="")
        return f"{block}\n\n{arrow}\n\n{child_block}"

    # Multiple children: branch out at increased depth
    child_blocks = [render_tree(cid, member_ids, depth=depth + 1) for cid in child_ids]
    return "\n\n".join([block] + [b for b in child_blocks if b])


# %% Generate one file per user
member_tweet_ids_by_user: dict[str, list[str]] = defaultdict(list)
for row in df_main.to_dicts():
    member_tweet_ids_by_user[row["username"]].append(row["tweet_id"])

users = sorted(member_tweet_ids_by_user.keys())
print(f"\nRendering {len(users)} user files …")

for username in tqdm(users, unit=" users", dynamic_ncols=True):
    tweet_ids = set(member_tweet_ids_by_user[username])

    # Find root tweets (start of threads or standalone tweets)
    roots = find_roots(tweet_ids)

    # Group roots into conversations: each root may have a whole subtree
    # Sort conversations by the most recent tweet they contain
    def latest_in_thread(root_id: str) -> str:
        members_in_thread = collect_thread(root_id, tweet_ids) & tweet_ids
        dates = [
            all_tweets[t].get("created_at") or ""
            for t in members_in_thread
            if t in all_tweets
        ]
        return max(dates) if dates else ""

    roots_sorted = sorted(roots, key=latest_in_thread, reverse=True)

    # Build file
    lines: list[str] = []

    for root_id in roots_sorted:
        tree_str = render_tree(root_id, tweet_ids)
        if tree_str:
            lines.append(tree_str)
            lines.append("")
            lines.append("---")
            lines.append("")

    out_path = USERS_DIR / f"{username}.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")

print(f"\nDone! Files saved to {USERS_DIR}/")
print(f"  {len(users)} user files created.")
