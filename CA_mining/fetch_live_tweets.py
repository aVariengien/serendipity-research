# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "tqdm",
# ]
# ///

# %% Config & imports
import argparse
import asyncio
import csv
import json
import os
import sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import httpx
from tqdm import tqdm

# ── Supabase (Community Archive) ─────────────────────────────────────────────
SUPABASE_URL = "https://fabxmporizzqflnftavs.supabase.co/rest/v1"
ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZhYnhtcG9yaXp6cWZsbmZ0YXZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNDQ5MTIsImV4cCI6MjAzNzgyMDkxMn0"
    ".UIEJiUNkLsW28tBHmG-RQDW-I5JNlJLt62CSk9D_qG8"
)
CA_HEADERS = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {ANON_KEY}",
}

# ── Twitter (RapidAPI) ────────────────────────────────────────────────────────
RAPID_API_KEY = os.environ["RAPID_API_KEY"]
TW_HEADERS = {
    "x-rapidapi-host": "twitter-api45.p.rapidapi.com",
    "x-rapidapi-key": RAPID_API_KEY,
}
TW_TIMELINE_URL    = "https://twitter-api45.p.rapidapi.com/timeline.php"
TW_REPLIES_URL     = "https://twitter-api45.p.rapidapi.com/replies.php"
TW_THREAD_URL      = "https://twitter-api45.p.rapidapi.com/tweet_thread.php"
TW_SCREENINFO_URL  = "https://twitter-api45.p.rapidapi.com/screenname.php"

# ── Script settings ───────────────────────────────────────────────────────────
CONCURRENCY            = 50   # simultaneous users
THREAD_CONCURRENCY     = 20   # simultaneous tweet_thread.php requests (across all users)
SCREENINFO_CONCURRENCY = 20   # simultaneous screenname.php requests (enrichment step)
MAX_RETRIES        = 3
RETRY_DELAY        = 5.0  # seconds, multiplied by attempt number
VERBOSE            = False  # set via --verbose flag

OUT_DIR = Path(__file__).parent / "outputs" / "tweets_live"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CONTEXT_DIR = Path(__file__).parent / "outputs" / "context_tweets_live"
CONTEXT_DIR.mkdir(parents=True, exist_ok=True)

ERR_FILE = OUT_DIR / "_errors.txt"


# %% Error logger

class ErrorLog:
    """Thread-safe async logger: prints errors immediately and appends to file."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._count = 0
        self._lock = asyncio.Lock()
        path.write_text("", encoding="utf-8")  # reset on each run

    async def log(self, msg: str) -> None:
        self._count += 1
        tqdm.write(f"  [ERROR] {msg}", file=sys.stderr)
        async with self._lock:
            with self.path.open("a", encoding="utf-8") as f:
                f.write(msg + "\n")

    @property
    def count(self) -> int:
        return self._count

    @staticmethod
    def fmt(exc: BaseException) -> str:
        """Always return a non-empty exception description."""
        msg = str(exc)
        return f"{type(exc).__name__}: {msg}" if msg.strip() else type(exc).__name__


def vlog(msg: str) -> None:
    """Print only when --verbose is active. Uses tqdm.write to avoid bar corruption."""
    if VERBOSE:
        tqdm.write(msg)


def _tweet_summary(tweets: list[dict], indent: str = "    ") -> str:
    """One line per tweet: tweet_id | @author | date | text snippet."""
    lines = []
    for t in tweets:
        tid    = t.get("tweet_id") or t.get("id") or "?"
        author = ((t.get("author") or {}).get("screen_name") or "?")
        try:
            date = parse_twitter_dt(t["created_at"]).strftime("%b %d %Y %H:%M")
        except Exception:
            date = (t.get("created_at") or "")[:16]
        text   = (t.get("text") or "").replace("\n", " ")[:60]
        lines.append(f"{indent}{tid} | @{author} | {date} | {text}")
    return "\n".join(lines)


# %% Supabase helpers

async def ca_get(client: httpx.AsyncClient, table: str, params: dict) -> list[dict]:
    """Fetch all pages from a Supabase table."""
    rows: list[dict] = []
    offset = 0
    page = 1000
    while True:
        resp = await client.get(
            f"{SUPABASE_URL}/{table}",
            params={**params, "offset": offset, "limit": page},
            headers=CA_HEADERS,
            timeout=60.0,
        )
        resp.raise_for_status()
        batch = resp.json()
        rows.extend(batch)
        if len(batch) < page:
            break
        offset += page
    return rows


# %% Twitter timeline helpers

def parse_twitter_dt(s: str) -> datetime:
    """Parse Twitter's 'Thu Feb 26 22:07:50 +0000 2026' format."""
    return parsedate_to_datetime(s).replace(tzinfo=timezone.utc)


async def fetch_page(
    client: httpx.AsyncClient,
    url: str,
    username: str,
    cursor: str | None,
) -> dict:
    """Fetch a single page from any timeline-style endpoint, with retries."""
    import json as _json
    params: dict[str, str] = {"screenname": username}
    if cursor:
        params["cursor"] = cursor
    for attempt in range(MAX_RETRIES):
        try:
            resp = await client.get(url, params=params, headers=TW_HEADERS, timeout=30.0)
            resp.raise_for_status()
            try:
                return resp.json()
            except _json.JSONDecodeError as exc:
                raw = resp.text[:300].replace("\n", " ")
                raise ValueError(
                    f"JSON decode error (HTTP {resp.status_code}) | "
                    f"cursor={cursor!r} | body: {raw!r}"
                ) from exc
        except (httpx.HTTPStatusError, httpx.RequestError, ValueError):
            if attempt == MAX_RETRIES - 1:
                raise
            await asyncio.sleep(RETRY_DELAY * (attempt + 1))
    return {}


async def paginate_endpoint(
    client: httpx.AsyncClient,
    url: str,
    username: str,
    cutoff: datetime | None,
    author_filter: bool,
    request_counter: list[int],
    error_log: ErrorLog,
) -> tuple[list[dict], list[dict]]:
    """
    Paginate a timeline endpoint until the cutoff date (or exhaustion).

    - author_filter: if True, separate tweets into user's own tweets vs context
      tweets from others (needed for replies.php).
    - Stopping condition: stop when a page has >10 author tweets and ALL of
      them are older than the cutoff (avoids early stop from pinned/quoted
      tweets mixed in with fresh content).

    Returns (user_tweets, context_tweets).
    """
    user_tweets: list[dict] = []
    context_tweets: list[dict] = []
    cursor: str | None = None
    username_lower = username.lower()
    endpoint = url.split("/")[-1]

    # Permanent API-level errors — retrying won't help
    PERMANENT_STATUSES = {"notfound", "suspended", "protected"}
    MAX_EMPTY_RETRIES = 4   # retry same cursor this many times on an empty page
    MAX_CURSOR_ADVANCES = 3  # after this many cursor advances with still 0 tweets, give up
                             # (guards against Twitter's ~3200-tweet wall: the API spins
                             # through cosmetically-different cursors that all embed the
                             # same boundary tweet ID and never return content again)

    empty_streak = 0     # consecutive empty-page responses for the current cursor
    cursor_advances = 0  # how many times we advanced to a new cursor after all retries emptied

    while True:
        # ── fetch page with retries ───────────────────────────────────────────
        data: dict = {}
        for attempt in range(MAX_RETRIES):
            request_time = datetime.now(timezone.utc).isoformat()
            try:
                data = await fetch_page(client, url, username, cursor)
            except Exception as exc:
                if attempt == MAX_RETRIES - 1:
                    await error_log.log(
                        f"{username} [{endpoint}] cursor={cursor!r}: {ErrorLog.fmt(exc)}"
                    )
                    return user_tweets, context_tweets
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
                continue

            request_counter[0] += 1
            api_status = data.get("status")

            if api_status in (None, "ok", "active"):
                page_tweets_raw = data.get("timeline", [])
                next_cur = data.get("next_cursor") or "none"
                vlog(
                    f"  → [{endpoint}] @{username} "
                    f"cursor_in={cursor!r} attempt={attempt+1} "
                    f"→ {len(page_tweets_raw)} tweets  next_cursor={next_cur!r}"
                )
                if page_tweets_raw:
                    vlog(_tweet_summary(page_tweets_raw))
                break  # success

            # API returned an error status — check if permanent
            user_status = (data.get("user") or {}).get("status") or ""
            if user_status.lower() in PERMANENT_STATUSES or api_status == "notfound":
                await error_log.log(
                    f"{username} [{endpoint}] cursor={cursor!r}: "
                    f"permanent — status={api_status} user_status={user_status}"
                )
                return user_tweets, context_tweets

            # Transient error — retry
            if attempt == MAX_RETRIES - 1:
                await error_log.log(
                    f"{username} [{endpoint}] cursor={cursor!r}: "
                    f"status={api_status} detail={data.get('detail', '')} "
                    f"(failed after {MAX_RETRIES} retries)"
                )
                return user_tweets, context_tweets
            await asyncio.sleep(RETRY_DELAY * (attempt + 1))

        page_tweets: list[dict] = data.get("timeline", [])
        if not page_tweets:
            empty_streak += 1
            next_cursor_candidate = data.get("next_cursor")
            if empty_streak < MAX_EMPTY_RETRIES:
                vlog(
                    f"  → [{endpoint}] @{username} empty page "
                    f"(streak {empty_streak}/{MAX_EMPTY_RETRIES}), retrying cursor …"
                )
                await asyncio.sleep(RETRY_DELAY)
                continue  # retry the same cursor
            # Exhausted retries on this cursor — advance if the API gave a next_cursor
            if next_cursor_candidate and next_cursor_candidate != cursor:
                cursor_advances += 1
                if cursor_advances > MAX_CURSOR_ADVANCES:
                    vlog(
                        f"  → [{endpoint}] @{username} {cursor_advances} cursor advances "
                        f"all returned 0 tweets — likely hit timeline limit, stopping."
                    )
                    break
                vlog(
                    f"  → [{endpoint}] @{username} {MAX_EMPTY_RETRIES} empty pages, "
                    f"advancing to next_cursor (advance {cursor_advances}/{MAX_CURSOR_ADVANCES}) …"
                )
                cursor = next_cursor_candidate
                empty_streak = 0
                continue
            break  # no next_cursor to advance to, stop

        empty_streak = 0     # reset on any page that returns tweets
        cursor_advances = 0  # real content seen — reset the advance guard too

        # For the cutoff check, count only the user's own tweets per page.
        # Stop only when a page returns >10 author tweets AND every one of them
        # is older than the archive — this avoids stopping early on pages that
        # mix new tweets with a few old pinned/quoted tweets.
        author_tweet_count = 0
        old_tweet_count = 0

        for tweet in page_tweets:
            tweet["fetched_at"] = request_time

            is_context = author_filter and (
                ((tweet.get("author") or {}).get("screen_name") or "").lower() != username_lower
            )

            if is_context:
                context_tweets.append(tweet)
                continue

            if cutoff is not None:
                try:
                    tweet_dt = parse_twitter_dt(tweet["created_at"])
                except Exception:
                    user_tweets.append(tweet)
                    continue
                author_tweet_count += 1
                if tweet_dt <= cutoff:
                    old_tweet_count += 1
                    continue  # already in the archive, skip
                user_tweets.append(tweet)
            else:
                user_tweets.append(tweet)

        # Reached cutoff when the page was clearly in archive territory:
        # >10 author tweets seen and all of them predate the cutoff.
        if cutoff is not None and author_tweet_count > 10 and author_tweet_count == old_tweet_count:
            break

        next_cursor = data.get("next_cursor")
        if not next_cursor or next_cursor == cursor:
            break
        cursor = next_cursor

    return user_tweets, context_tweets


async def fetch_thread(
    client: httpx.AsyncClient,
    root_tweet_id: str,
    username: str,
    cutoff: datetime | None,
    request_counter: list[int],
    error_log: ErrorLog,
    thread_semaphore: asyncio.Semaphore,
) -> list[dict]:
    """
    Fetch all continuation tweets in a self-reply thread via tweet_thread.php.
    Thread items use 'id' instead of 'tweet_id' — we normalise to 'tweet_id'.
    Only returns tweets authored by `username` that are newer than `cutoff`.
    """
    import json as _json

    tweets: list[dict] = []
    username_lower = username.lower()
    data: dict = {}

    async with thread_semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.get(
                    TW_THREAD_URL,
                    params={"id": root_tweet_id},
                    headers=TW_HEADERS,
                    timeout=30.0,
                )
                resp.raise_for_status()
                try:
                    data = resp.json()
                except _json.JSONDecodeError as exc:
                    raw = resp.text[:200].replace("\n", " ")
                    raise ValueError(
                        f"JSON decode (HTTP {resp.status_code}) body={raw!r}"
                    ) from exc
                break  # success — exit retry loop
            except (httpx.HTTPStatusError, httpx.RequestError, ValueError) as exc:
                if attempt == MAX_RETRIES - 1:
                    await error_log.log(
                        f"{username} [tweet_thread.php] id={root_tweet_id}: {ErrorLog.fmt(exc)}"
                    )
                    return tweets
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))

    request_counter[0] += 1
    request_time = datetime.now(timezone.utc).isoformat()
    thread_items = data.get("thread", [])
    vlog(
        f"  → [tweet_thread.php] @{username} id={root_tweet_id} "
        f"→ {len(thread_items)} thread items"
    )
    if thread_items:
        vlog(_tweet_summary(thread_items))

    for item in thread_items:
        item["tweet_id"] = item.pop("id", "")
        item["fetched_at"] = request_time

        author_sn = ((item.get("author") or {}).get("screen_name") or "").lower()
        if author_sn != username_lower:
            continue

        if cutoff is not None:
            try:
                if parse_twitter_dt(item["created_at"]) <= cutoff:
                    continue
            except Exception:
                pass

        tweets.append(item)

    return tweets


async def fetch_user_tweets(
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    thread_semaphore: asyncio.Semaphore,
    username: str,
    cutoff: datetime | None,
    pbar: tqdm,
    tweet_counter: list[int],
    request_counter: list[int],
    error_log: ErrorLog,
    force: bool = False,
) -> None:
    """
    Fetch all tweets + replies for `username` posted after `cutoff`,
    dedup by tweet_id, and write to outputs/tweets_live/{username}.jsonl.
    Context tweets from replies.php are saved to outputs/context_tweets_live/{username}.jsonl.
    Each tweet gets a `fetched_at` = ISO timestamp of the page request.
    Pass force=True to re-fetch even when the output file already exists.
    """
    out_file = OUT_DIR / f"{username}.jsonl"
    if out_file.exists() and not force:
        existing = sum(1 for l in out_file.read_text(encoding="utf-8").splitlines() if l.strip())
        tweet_counter[0] += existing
        pbar.set_postfix(tweets=f"{tweet_counter[0]:,}", reqs=f"{request_counter[0]:,}", refresh=False)
        pbar.update(1)
        return

    async with semaphore:
        # Fetch timeline and replies concurrently
        (timeline_tweets, _), (reply_tweets, context_tweets) = await asyncio.gather(
            paginate_endpoint(client, TW_TIMELINE_URL, username, cutoff, author_filter=False, request_counter=request_counter, error_log=error_log),
            paginate_endpoint(client, TW_REPLIES_URL,  username, cutoff, author_filter=True,  request_counter=request_counter, error_log=error_log),
        )

        # Merge user tweets, dedup by tweet_id (timeline wins on collision)
        # Drop any tweet the API returned without a valid tweet_id
        seen: dict[str, dict] = {}
        for tweet in reply_tweets:
            if tid := (tweet.get("tweet_id") or "").strip():
                seen[tid] = tweet
        for tweet in timeline_tweets:
            if tid := (tweet.get("tweet_id") or "").strip():
                seen[tid] = tweet  # timeline overwrites replies on collision

        # Find self-reply thread roots (tweet_id == conversation_id, authored by user)
        # and fetch their full continuation tweets via tweet_thread.php
        username_lower = username.lower()
        thread_roots = [
            t["tweet_id"] for t in seen.values()
            if t["tweet_id"] == t.get("conversation_id")
            and ((t.get("author") or {}).get("screen_name") or "").lower() == username_lower
            and int(t.get("replies") or 0) > 0
        ]
        if thread_roots:
            thread_results = await asyncio.gather(*[
                fetch_thread(client, root_id, username, cutoff, request_counter, error_log, thread_semaphore)
                for root_id in thread_roots
            ])
            for thread_tweets in thread_results:
                for tweet in thread_tweets:
                    if tid := (tweet.get("tweet_id") or "").strip():
                        seen.setdefault(tid, tweet)  # don't overwrite existing

        merged = sorted(seen.values(), key=lambda t: t.get("tweet_id") or "", reverse=True)

        with out_file.open("w", encoding="utf-8") as f:
            for tweet in merged:
                f.write(json.dumps(tweet, ensure_ascii=False) + "\n")

        # Save context tweets (deduped by tweet_id)
        if context_tweets:
            ctx_seen: dict[str, dict] = {
                t["tweet_id"]: t for t in context_tweets
                if (t.get("tweet_id") or "").strip()
            }
            ctx_file = CONTEXT_DIR / f"{username}.jsonl"
            with ctx_file.open("w", encoding="utf-8") as f:
                for tweet in sorted(ctx_seen.values(), key=lambda t: t["tweet_id"], reverse=True):
                    f.write(json.dumps(tweet, ensure_ascii=False) + "\n")

    tweet_counter[0] += len(merged)
    pbar.set_postfix(tweets=f"{tweet_counter[0]:,}", reqs=f"{request_counter[0]:,}", refresh=False)
    pbar.update(1)


# %% Author account_created_at enrichment

def _collect_screen_names_from_tweet(
    tweet: dict, names: set[str], only_missing: bool = False
) -> None:
    """Recursively collect author screen_names from a tweet and all nested sub-tweets.
    If only_missing=True, skip authors that already have account_created_at."""
    author = tweet.get("author")
    if isinstance(author, dict):
        if not only_missing or "account_created_at" not in author:
            sn = (author.get("screen_name") or "").strip()
            if sn:
                names.add(sn.lower())
    for key in ("quoted", "retweeted_tweet"):
        nested = tweet.get(key)
        if isinstance(nested, dict):
            _collect_screen_names_from_tweet(nested, names, only_missing=only_missing)


def _collect_screen_names_from_files(
    files: list[Path], only_missing: bool = False
) -> set[str]:
    """
    Return every unique screen_name (lowercased) found in the given JSONL files.
    Recursively walks tweet.author, tweet.quoted.author,
    tweet.retweeted_tweet.author, and any further nesting.
    If only_missing=True, skips authors that already have account_created_at.
    """
    names: set[str] = set()
    for f in files:
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    tweet = json.loads(line)
                    _collect_screen_names_from_tweet(tweet, names, only_missing=only_missing)
                except Exception:
                    continue
        except Exception:
            continue
    return names


def _collect_screen_names(dirs: list[Path]) -> set[str]:
    """Collect screen names from all JSONL files across the given directories."""
    files = [f for d in dirs for f in sorted(d.glob("*.jsonl"))]
    return _collect_screen_names_from_files(files)


# Profile fields we enrich into every author object.
# Maps: author dict key  →  (CA column, API response key | None)
# num_likes is CA-only — the screenname.php endpoint doesn't expose it.
_PROFILE_FIELDS: list[tuple[str, str, str | None]] = [
    # (author_key,        ca_column,      api_key)
    ("account_created_at", "created_at",   "created_at"),   # needs date parsing for API
    ("num_tweets",         "num_tweets",   "statuses_count"),
    ("num_following",      "num_following","friends"),
    ("num_followers",      "num_followers","sub_count"),     # API exposes followers as sub_count
    ("num_likes",          "num_likes",    None),            # CA-only
]


def _apply_author_profile(
    tweet: dict, mapping: dict[str, dict], only_missing: bool = False
) -> None:
    """
    Recursively inject profile fields into tweet.author and any nested sub-tweet
    authors (quoted, retweeted_tweet, and further nesting). In-place.
    Only sets fields present in `mapping`; never overwrites with None.
    If only_missing=True, skips author objects that already have account_created_at.
    """
    author = tweet.get("author")
    if isinstance(author, dict):
        if not only_missing or "account_created_at" not in author:
            sn = (author.get("screen_name") or "").lower()
            if sn and sn in mapping:
                for key, value in mapping[sn].items():
                    if value is not None:
                        author[key] = value
    for key in ("quoted", "retweeted_tweet"):
        nested = tweet.get(key)
        if isinstance(nested, dict):
            _apply_author_profile(nested, mapping, only_missing=only_missing)


async def _fetch_screeninfo_one(
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    screen_name: str,
    error_log: ErrorLog,
) -> tuple[str, dict]:
    """
    Call screenname.php for one account.
    Returns (screen_name_lower, profile_dict) where profile_dict contains
    only the keys we care about (author_key from _PROFILE_FIELDS), excluding
    CA-only fields and None values.
    """
    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.get(
                    TW_SCREENINFO_URL,
                    params={"screenname": screen_name},
                    headers=TW_HEADERS,
                    timeout=30.0,
                )
                resp.raise_for_status()
                data = resp.json()
                profile: dict = {}
                for author_key, _ca_col, api_key in _PROFILE_FIELDS:
                    if api_key is None:
                        continue  # CA-only field
                    raw = data.get(api_key)
                    if raw is None:
                        continue
                    if author_key == "account_created_at":
                        try:
                            raw = parse_twitter_dt(str(raw)).isoformat()
                        except Exception:
                            pass
                    profile[author_key] = raw
                return screen_name.lower(), profile
            except Exception as exc:
                if attempt == MAX_RETRIES - 1:
                    await error_log.log(
                        f"screenname.php @{screen_name}: {ErrorLog.fmt(exc)}"
                    )
                    return screen_name.lower(), {}
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
    return screen_name.lower(), {}


async def enrich_author_profiles(
    client: httpx.AsyncClient,
    error_log: ErrorLog,
    step_label: str = "3",
    only_users: list[str] | None = None,
    only_missing: bool = False,
) -> None:
    """
    Enrich all JSONL files in tweets_live/ and context_tweets_live/ with
    author profile fields: account_created_at, num_tweets, num_following,
    num_followers, num_likes (CA-only).

    If only_users is given, only process the JSONL files for those usernames
    (both tweets_live/<user>.jsonl and context_tweets_live/<user>.jsonl).

    If only_missing=True, skip any author object that already has
    account_created_at — useful for incremental re-runs to avoid redundant
    API calls.

    Strategy (CA takes priority over API):
      1. Pull all fields from CA all_account for any screen_name already there.
      2. Call screenname.php for every remaining screen_name.
      3. Rewrite every JSONL file injecting fields into tweet.author (and
         tweet.quoted.author).
    """
    ca_select = ",".join(
        ["username"] + [ca_col for _, ca_col, _ in _PROFILE_FIELDS]
    )
    print(f"[{step_label}] Enriching author profiles "
          f"(created_at / num_tweets / num_following / num_followers / num_likes) …")

    # ── Resolve target files ──────────────────────────────────────────────────
    if only_users:
        filter_stems = {u.lower() for u in only_users}
        target_files = [
            f for d in [OUT_DIR, CONTEXT_DIR]
            for f in sorted(d.glob("*.jsonl"))
            if f.stem.lower() in filter_stems
        ]
        if not target_files:
            print(f"      No JSONL files found for: {', '.join(sorted(filter_stems))}")
            return
        print(f"      Filtering to {len(target_files)} file(s): "
              f"{', '.join(f.name for f in target_files)}")
    else:
        target_files = [
            f for d in [OUT_DIR, CONTEXT_DIR]
            for f in sorted(d.glob("*.jsonl"))
        ]

    # ── 1. Collect all unique screen names from target files ──────────────────
    screen_names = _collect_screen_names_from_files(target_files, only_missing=only_missing)
    if not screen_names:
        msg = "all authors already enriched" if only_missing else "no JSONL files found"
        print(f"      Nothing to do — {msg}.")
        return
    suffix = " (skipping already-enriched authors)" if only_missing else ""
    print(f"      {len(screen_names):,} unique screen names to enrich{suffix}")

    # ── 2. Look up profile data from Community Archive (all_account table) ────
    print("      Fetching profile data from Community Archive …")
    ca_rows = await ca_get(client, "all_account", {"select": ca_select})
    ca_map: dict[str, dict] = {}
    for row in ca_rows:
        uname = (row.get("username") or "").lower().strip()
        if not uname:
            continue
        profile: dict = {}
        for author_key, ca_col, _api_key in _PROFILE_FIELDS:
            val = row.get(ca_col)
            if val is not None:
                profile[author_key] = val
        if profile:
            ca_map[uname] = profile

    # Decide which screen names need an API call:
    # any name not in CA, OR in CA but missing account_created_at
    missing = {
        sn for sn in screen_names
        if sn not in ca_map or "account_created_at" not in ca_map[sn]
    }
    covered = len(screen_names) - len(missing)
    print(f"      {covered:,} fully covered by CA, {len(missing):,} need API calls")

    # ── 3. Fetch missing screen names from screenname.php ─────────────────────
    api_map: dict[str, dict] = {}
    if missing:
        semaphore = asyncio.Semaphore(SCREENINFO_CONCURRENCY)
        results: list[tuple[str, dict]] = []

        with tqdm(total=len(missing), desc="  screeninfo", unit=" accts", dynamic_ncols=True) as pbar:
            async def _one(sn: str) -> None:
                results.append(
                    await _fetch_screeninfo_one(client, semaphore, sn, error_log)
                )
                pbar.update(1)

            await asyncio.gather(*[_one(sn) for sn in missing])

        api_map = {sn: p for sn, p in results if p}
        not_found = len(missing) - len(api_map)
        print(f"      {len(api_map):,} fetched via API  "
              f"({not_found:,} not found / suspended / no data)")

    # ── 4. Merge: start with API data, let CA overwrite (CA takes priority) ────
    full_map: dict[str, dict] = {}
    for sn, profile in api_map.items():
        full_map[sn] = dict(profile)
    for sn, profile in ca_map.items():
        if sn in full_map:
            full_map[sn].update(profile)   # CA wins on any shared key
        else:
            full_map[sn] = dict(profile)

    # ── 5. Rewrite JSONL files ─────────────────────────────────────────────────
    files_rewritten = 0
    tweets_total = 0

    for f in tqdm(target_files, desc="  Rewriting", unit=" files", dynamic_ncols=True):
        lines_out: list[str] = []
        try:
            for line in f.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    tweet = json.loads(line)
                    _apply_author_profile(tweet, full_map, only_missing=only_missing)
                    lines_out.append(json.dumps(tweet, ensure_ascii=False))
                    tweets_total += 1
                except Exception:
                    lines_out.append(line)
        except Exception as exc:
            await error_log.log(f"enrich rewrite {f.name}: {ErrorLog.fmt(exc)}")
            continue

        if lines_out:
            f.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
            files_rewritten += 1

    print(f"      {files_rewritten:,} files rewritten, {tweets_total:,} tweet objects enriched")


# %% Main

async def main(plan_only: bool = False, only_users: list[str] | None = None, force: bool = False, enrich_only: bool = False) -> None:
    error_log = ErrorLog(ERR_FILE)

    async with httpx.AsyncClient() as client:

        # ── Enrich-only shortcut ──────────────────────────────────────────────
        if enrich_only:
            await enrich_author_profiles(
                client, error_log, step_label="1/1", only_users=only_users,
                only_missing=True,
            )
            if error_log.count:
                print(f"  Errors: {error_log.count:,} → {ERR_FILE}")
            return

        # ── Step 0: collect all users ─────────────────────────────────────────
        print("[0/4] Fetching users from Community Archive …")

        ca_accounts = await ca_get(client, "account", {"select": "account_id,username"})
        ca_map: dict[str, str] = {a["username"].lower(): a["account_id"] for a in ca_accounts}
        print(f"      {len(ca_map):,} accounts in account")

        optin_rows = await ca_get(client, "optin", {"select": "username,twitter_user_id"})
        optin_map: dict[str, str | None] = {
            r["username"].lower(): r.get("twitter_user_id")
            for r in optin_rows
            if r.get("username") and r.get("twitter_user_id")
        }
        print(f"      {len(optin_map):,} rows in optin (with twitter_user_id)")

        # Merge: ca_map wins for account_id when present
        all_users: dict[str, str | None] = {**optin_map, **ca_map}
        # Track source for plan output
        source_map: dict[str, str] = {
            **{u: "optin" for u in optin_map},
            **{u: "all_account" for u in ca_map},
        }
        print(f"      {len(all_users):,} unique users total")

        if only_users:
            filter_lower = {u.lower() for u in only_users}
            all_users = {k: v for k, v in all_users.items() if k in filter_lower}
            source_map = {k: v for k, v in source_map.items() if k in filter_lower}
            unknown = filter_lower - set(all_users)
            if unknown:
                print(f"      WARNING: unknown users (not in CA): {', '.join(sorted(unknown))}")
            print(f"      Filtered to {len(all_users)} user(s): {', '.join(sorted(all_users))}")
        print()

        # ── Step 1: get latest archive_at per account_id ───────────────────────
        print("[1/4] Fetching latest archive upload dates …")
        upload_rows = await ca_get(
            client,
            "archive_upload",
            {"select": "account_id,archive_at", "upload_phase": "eq.completed"},
        )
        # account_id -> latest archive_at (as datetime)
        archive_cutoffs: dict[str, datetime] = {}
        for row in upload_rows:
            acct_id = row["account_id"]
            try:
                dt = datetime.fromisoformat(row["archive_at"].replace("Z", "+00:00"))
            except Exception:
                continue
            if acct_id not in archive_cutoffs or dt > archive_cutoffs[acct_id]:
                archive_cutoffs[acct_id] = dt

        # Build per-username cutoff map (username_lower -> datetime | None)
        username_cutoffs: dict[str, datetime | None] = {}
        for username_lower, account_id in all_users.items():
            if account_id and account_id in archive_cutoffs:
                username_cutoffs[username_lower] = archive_cutoffs[account_id]
            else:
                username_cutoffs[username_lower] = None  # optin-only: fetch everything

        n_with_archive = sum(1 for v in username_cutoffs.values() if v is not None)
        n_no_archive = sum(1 for v in username_cutoffs.values() if v is None)
        print(f"      {n_with_archive:,} users have an archive cutoff")
        print(f"      {n_no_archive:,} users have no archive (will fetch full timeline)\n")

        # Preserve original-case usernames for the API call
        orig_case: dict[str, str] = {}
        for r in ca_accounts:
            orig_case[r["username"].lower()] = r["username"]
        for r in optin_rows:
            if r.get("username"):
                orig_case.setdefault(r["username"].lower(), r["username"])

        # ── Plan output (--plan flag) ─────────────────────────────────────────
        if plan_only:
            plan_file = OUT_DIR.parent / "fetch_plan.csv"
            with plan_file.open("w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["username", "account_id", "source", "fetch_from_cutoff"])
                for uname_lower in sorted(all_users):
                    writer.writerow([
                        orig_case.get(uname_lower, uname_lower),
                        all_users[uname_lower] or "",
                        source_map.get(uname_lower, ""),
                        username_cutoffs[uname_lower].isoformat() if username_cutoffs[uname_lower] else "full_timeline",
                    ])
            print(f"Plan written to {plan_file}  ({len(all_users):,} rows)")
            print("Re-run without --plan to start fetching.")
            return

        # ── Step 2: fetch live tweets ─────────────────────────────────────────
        print(f"[2/4] Fetching live tweets for {len(all_users):,} users …")
        already_done = sum(
            1 for u in all_users if (OUT_DIR / f"{u}.jsonl").exists()
        )
        if force:
            print(f"      Already fetched: {already_done} (--force: will re-fetch)")
        else:
            print(f"      Already fetched: {already_done} (skipping)")
        print(f"      Concurrency: {CONCURRENCY}\n")

        semaphore        = asyncio.Semaphore(CONCURRENCY)
        thread_semaphore = asyncio.Semaphore(THREAD_CONCURRENCY)
        tweet_counter: list[int]   = [0]
        request_counter: list[int] = [0]

        with tqdm(
            total=len(all_users), desc="Users", unit=" users", dynamic_ncols=True
        ) as pbar:
            tasks = [
                fetch_user_tweets(
                    client,
                    semaphore,
                    thread_semaphore,
                    orig_case.get(uname_lower, uname_lower),
                    username_cutoffs[uname_lower],
                    pbar,
                    tweet_counter,
                    request_counter,
                    error_log,
                    force=force,
                )
                for uname_lower in all_users
            ]
            await asyncio.gather(*tasks)

        # ── Step 3: enrich author account_created_at ──────────────────────────
        await enrich_author_profiles(client, error_log, step_label="3/4", only_users=only_users)

    # ── Step 4: summary ───────────────────────────────────────────────────────
    print("\n[4/4] Summary")

    n_user_files = sum(1 for u in all_users if (OUT_DIR / f"{orig_case.get(u, u)}.jsonl").exists())
    n_ctx_files  = sum(1 for u in all_users if (CONTEXT_DIR / f"{orig_case.get(u, u)}.jsonl").exists())

    print(f"  API requests  : {request_counter[0]:,}")
    print(f"  User tweets   : {tweet_counter[0]:,}  ({n_user_files} files) → {OUT_DIR}")
    print(f"  Context tweets: {n_ctx_files} files → {CONTEXT_DIR}")
    if error_log.count:
        print(f"  Errors        : {error_log.count:,} → {ERR_FILE}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch live tweets for CA users")
    parser.add_argument(
        "--plan",
        action="store_true",
        help="Dry-run: resolve all users and cutoff dates, write fetch_plan.csv, then exit.",
    )
    parser.add_argument(
        "--users",
        nargs="+",
        metavar="USERNAME",
        help="Only fetch these specific users (space-separated). Useful for testing.",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print each API call and its returned tweets (id, author, date) in real time.",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Re-fetch users even when their output file already exists.",
    )
    parser.add_argument(
        "--enrich-only",
        action="store_true",
        help=(
            "Skip tweet fetching entirely. Only run the account_created_at enrichment "
            "step on all existing JSONL files in outputs/tweets_live/ and "
            "outputs/context_tweets_live/."
        ),
    )
    args = parser.parse_args()
    if args.verbose:
        VERBOSE = True  # noqa: F841 — sets module global at __main__ level
    asyncio.run(main(
        plan_only=args.plan,
        only_users=args.users,
        force=args.force,
        enrich_only=args.enrich_only,
    ))
