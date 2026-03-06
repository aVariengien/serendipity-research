# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "psycopg[binary]",
#   "tqdm",
# ]
# ///
"""insert_tweets_to_ca.py — Insert fresh JSONL tweets into the Community Archive.

Usage:
    uv run insert_tweets_to_ca.py --test              # run built-in test suite
    uv run insert_tweets_to_ca.py --dry-run           # parse + print, no DB writes
    uv run insert_tweets_to_ca.py --dry-run --limit 5 # dry-run on 5 tweets only
    uv run insert_tweets_to_ca.py --file path.jsonl   # single file only
    uv run insert_tweets_to_ca.py                     # full run (needs POSTGRES_PASSWORD)

Environment variables:
    POSTGRES_PASSWORD  — required for live runs (Supabase DB password)
    POSTGRES_HOST      — optional, defaults to the project's direct connection host
    POSTGRES_USER      — optional, defaults to "postgres"
    POSTGRES_DB        — optional, defaults to "postgres"
    POSTGRES_PORT      — optional, defaults to 5432
"""

import argparse
import json
import os
import sys
from dataclasses import dataclass, field
from email.utils import parsedate_to_datetime
from pathlib import Path

import psycopg
from tqdm import tqdm

# ── Config ────────────────────────────────────────────────────────────────────

POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "db.fabxmporizzqflnftavs.supabase.co")
POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_DB   = os.environ.get("POSTGRES_DB",   "postgres")
POSTGRES_PORT = int(os.environ.get("POSTGRES_PORT", "5432"))
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")

BATCH_SIZE = 500

SCRIPT_DIR = Path(__file__).parent
DEFAULT_DIRS = [
    SCRIPT_DIR / "outputs" / "tweets_live",
    SCRIPT_DIR / "outputs" / "context_tweets_live",
]

# Tables must be inserted in this order to satisfy FK constraints.
# all_account_sparse uses the same DB table as all_account but inserts
# with DO NOTHING so incomplete rows never overwrite existing good data.
INSERT_ORDER = [
    "all_account",          # no FK deps — accounts with a valid username
    "all_account_sparse",   # same DB table — accounts missing username (DO NOTHING)
    "all_profile",          # → all_account
    "account_refresh_log",  # → all_account; tracks per-account fetch window
    "mentioned_users",      # no FK deps (inserted before user_mentions)
    "tweets",               # → all_account
    "tweet_media",          # → tweets
    "tweet_urls",           # → tweets
    "user_mentions",        # → tweets, mentioned_users
    "conversations",        # → tweets
    "quote_tweets",         # → tweets (tweet_id only; quoted_tweet_id has no FK)
    "retweets",             # → tweets (both columns)
]


# ── Data model ────────────────────────────────────────────────────────────────

@dataclass
class TweetBundle:
    """All DB rows derived from a single tweet object."""
    account:         dict
    profile:         dict
    tweet:           dict
    media:           list[dict] = field(default_factory=list)
    urls:            list[dict] = field(default_factory=list)
    mentioned_users: list[dict] = field(default_factory=list)
    user_mentions:   list[dict] = field(default_factory=list)
    conversation:    dict | None = None
    quote_tweet:     dict | None = None  # set on the quoting tweet
    retweet:         dict | None = None  # set on the RT wrapper
    fetched_at:      str  | None = None  # raw tweet's updated_at / fetched_at (ISO 8601)


# ── Parsing helpers ───────────────────────────────────────────────────────────

def parse_twitter_date(s: str) -> str | None:
    """Convert Twitter date string to ISO 8601. Returns None on failure.

    Input:  "Thu Feb 26 17:48:52 +0000 2026"
    Output: "2026-02-26T17:48:52+00:00"
    """
    if not s:
        return None
    try:
        return parsedate_to_datetime(s).isoformat()
    except Exception:
        return None


def parse_media(media_field, tweet_id: str) -> list[dict]:
    """Parse the JSONL media field into tweet_media rows.

    The field can be:
      - []                              → no media
      - {"photo": [{id, media_url_https, sizes: {h, w}}, ...]}
      - {"video": [{id, media_url_https, original_info: {width, height}}, ...]}
    """
    if not media_field or isinstance(media_field, list):
        return []

    rows = []
    for media_type, items in media_field.items():
        for item in items:
            media_id_str = item.get("id") or item.get("id_str")
            if not media_id_str:
                continue
            try:
                media_id = int(media_id_str)
            except (ValueError, TypeError):
                continue

            # Photos use sizes.w/h; videos use original_info.width/height
            sizes = item.get("sizes") or {}
            orig  = item.get("original_info") or {}
            width  = sizes.get("w") or orig.get("width",  0) or 0
            height = sizes.get("h") or orig.get("height", 0) or 0

            rows.append({
                "tweet_id":   tweet_id,
                "media_id":   media_id,
                "media_url":  item.get("media_url_https", ""),
                "media_type": media_type,
                "width":      width,
                "height":     height,
            })
    return rows


# ── Mappers (JSONL dict → DB row dict) ───────────────────────────────────────

def map_account(author: dict, fallback_created_at: str) -> dict:
    """Map an author object to an all_account row.

    account_created_at (the real Twitter account creation date) is used when
    present.  For authors where it wasn't returned by the API we fall back to
    the tweet's created_at as a "no later than" approximation.

    On conflict, created_at is intentionally NOT in the update list so a real
    value previously written by an archive upload is never overwritten.
    """
    return {
        "account_id":           author["rest_id"],
        "username":             author.get("screen_name") or "",
        "account_display_name": author.get("name") or "",
        "created_via":          "twitter_fetched",
        "created_at":           author.get("account_created_at") or fallback_created_at,
        "num_followers":        author.get("num_followers") or author.get("followers_count"),
        "num_likes":            author.get("num_likes") or author.get("favourites_count"),
        "num_tweets":           author.get("num_tweets"),
        "num_following":        author.get("num_following"),
    }


def map_profile(author: dict) -> dict:
    """Map an author object to an all_profile row."""
    return {
        "account_id":       author["rest_id"],
        "avatar_media_url": author.get("avatar"),
        "header_media_url": None,   # not in JSONL
        "bio":              None,   # not in JSONL
        "location":         None,   # not in JSONL
        "website":          None,   # not in JSONL
    }


def map_tweet(raw: dict, account_id: str, created_at_iso: str) -> dict:
    """Map a raw JSONL tweet to a tweets row."""
    return {
        "tweet_id":          raw["tweet_id"],
        "account_id":        account_id,
        "created_at":        created_at_iso,
        "full_text":         raw.get("text") or "",
        "favorite_count":    raw.get("favorites") or 0,
        # Archive processor sums retweets + quotes for retweet_count
        "retweet_count":     (raw.get("retweets") or 0) + (raw.get("quotes") or 0),
        "reply_to_tweet_id": raw.get("in_reply_to_status_id_str") or None,
        "reply_to_user_id":  None,  # not in JSONL
        "reply_to_username": None,  # not in JSONL
    }


def map_urls(urls: list[dict], tweet_id: str) -> list[dict]:
    """Map entities.urls to tweet_urls rows."""
    rows = []
    for u in urls:
        url = u.get("url") or ""
        if not url:
            continue
        rows.append({
            "tweet_id":     tweet_id,
            "url":          url,
            "expanded_url": u.get("expanded_url"),  # nullable in live schema
            "display_url":  u.get("display_url") or "",
        })
    return rows


def map_mentions(
    mentions: list[dict], tweet_id: str
) -> tuple[list[dict], list[dict]]:
    """Map entities.user_mentions to (mentioned_users rows, user_mentions rows).

    Deduplicates by user_id within a single tweet.
    """
    mentioned_users = []
    user_mentions   = []
    seen = set()

    for m in mentions:
        user_id = m.get("id_str")
        if not user_id or user_id in seen:
            continue
        seen.add(user_id)

        mentioned_users.append({
            "user_id":     user_id,
            "name":        m.get("name") or "",
            "screen_name": m.get("screen_name") or "",
        })
        user_mentions.append({
            "tweet_id":          tweet_id,
            "mentioned_user_id": user_id,
        })

    return mentioned_users, user_mentions


# ── Bundle builder ────────────────────────────────────────────────────────────

def _build_single_bundle(
    raw: dict, *, is_main: bool
) -> TweetBundle | None:
    """Build a TweetBundle from one raw tweet dict.

    Returns None if required fields (tweet_id, author.rest_id, created_at) are
    missing or invalid — those rows would violate NOT NULL constraints.

    is_main=True  → populate quote_tweet / retweet relationship fields.
    is_main=False → nested tweet; skip those relationship fields.
    """
    tweet_id   = raw.get("tweet_id")
    author     = raw.get("author") or {}
    account_id = author.get("rest_id")

    if not tweet_id or not account_id:
        return None

    created_at_iso = parse_twitter_date(raw.get("created_at") or "")
    if not created_at_iso:
        return None

    entities         = raw.get("entities") or {}
    mentioned_users, user_mentions = map_mentions(
        entities.get("user_mentions") or [], tweet_id
    )

    conversation = None
    if conv_id := raw.get("conversation_id"):
        conversation = {"tweet_id": tweet_id, "conversation_id": str(conv_id)}

    # Relationship rows are only set on the outermost tweet in a nesting chain
    quote_tweet = None
    retweet     = None
    if is_main:
        if (quoted := raw.get("quoted")) and (q_id := quoted.get("tweet_id")):
            quote_tweet = {"tweet_id": tweet_id, "quoted_tweet_id": q_id}
        if (rt := raw.get("retweeted_tweet")) and (r_id := rt.get("tweet_id")):
            retweet = {"tweet_id": tweet_id, "retweeted_tweet_id": r_id}

    # updated_at is the canonical field name; fetched_at is the legacy alias.
    # Both are already ISO 8601 strings written by the fetcher.
    fetched_at = raw.get("updated_at") or raw.get("fetched_at") or None

    return TweetBundle(
        account         = map_account(author, created_at_iso),
        profile         = map_profile(author),
        tweet           = map_tweet(raw, account_id, created_at_iso),
        media           = parse_media(raw.get("media"), tweet_id),
        urls            = map_urls(entities.get("urls") or [], tweet_id),
        mentioned_users = mentioned_users,
        user_mentions   = user_mentions,
        conversation    = conversation,
        quote_tweet     = quote_tweet,
        retweet         = retweet,
        fetched_at      = fetched_at,
    )


def extract_all_bundles(raw: dict) -> list[TweetBundle]:
    """Build bundles for a JSONL tweet including all nested quoted/retweeted tweets.

    Handles up to three levels:
        main tweet
        ├── quoted                   (direct quote tweet)
        └── retweeted_tweet          (retweeted tweet)
            └── quoted               (tweet quoted inside a retweet)
    """
    bundles: list[TweetBundle] = []

    if main := _build_single_bundle(raw, is_main=True):
        bundles.append(main)

    if quoted := raw.get("quoted"):
        if b := _build_single_bundle(quoted, is_main=False):
            bundles.append(b)

    if retweeted := raw.get("retweeted_tweet"):
        if b := _build_single_bundle(retweeted, is_main=False):
            bundles.append(b)
        if nested_quoted := retweeted.get("quoted"):
            if b := _build_single_bundle(nested_quoted, is_main=False):
                bundles.append(b)

    return bundles


# ── Loading ───────────────────────────────────────────────────────────────────

def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file, tolerating tweet texts that contain literal newlines.

    Tweet text fields can contain actual newline characters (multi-line tweets,
    bullet lists, etc.).  When the JSONL writer doesn't escape them, a single
    JSON object spans several physical lines.  We detect object boundaries by
    watching for lines that start with '{' and accumulate everything in between.
    """
    rows: list[dict] = []
    pending: list[str] = []

    def _flush() -> None:
        text = "\n".join(pending).strip()
        if not text:
            return
        try:
            # strict=False allows embedded control chars (tabs, bare \r, etc.)
            # that occasionally appear in tweet texts written by the fetcher.
            rows.append(json.loads(text, strict=False))
        except json.JSONDecodeError as e:
            print(f"  [warn] JSON parse error in {path.name}: {e}")

    with path.open(encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if line.startswith("{") and pending:
                _flush()
                pending = [line]
            else:
                pending.append(line)

    if pending:
        _flush()

    return rows


# ── Streaming record builder ─────────────────────────────────────────────────

def _write_sparse_author_tweets_log(
    events: list[dict],
    good_account_ids: set[str],
    log_dir: Path,
) -> None:
    """Log every tweet whose author had an empty username in that specific fetch.

    Splits into two groups:
      - username found elsewhere: author appeared with a real username in another
        tweet — the DB row will be correct, but the fetcher missed it here.
      - no username found: author is completely unknown — account_id is all we have.

    This log is useful for diagnosing which API calls returned incomplete author
    data, and for identifying accounts that may need a targeted re-fetch.
    """
    found_elsewhere = [e for e in events if e["account_id"] in good_account_ids]
    truly_unknown   = [e for e in events if e["account_id"] not in good_account_ids]

    log_path = log_dir / "sparse_author_tweets.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("w", encoding="utf-8") as f:
        f.write(f"Tweets with sparse author (empty username in that fetch) — {len(events)} events\n")
        f.write("=" * 70 + "\n\n")

        f.write(f"GROUP 1 — Username found in another tweet ({len(found_elsewhere)} events)\n")
        f.write("These fetches returned incomplete author data, but the account is known.\n")
        f.write("No action needed; the DB row will have the correct username.\n")
        f.write("-" * 70 + "\n")
        for e in found_elsewhere:
            f.write(f"  account_id={e['account_id']}  tweet_id={e['tweet_id']}\n")
            f.write(f"    text: {e['text_preview']!r}\n")
        f.write("\n")

        f.write(f"GROUP 2 — No username found anywhere ({len(truly_unknown)} events)\n")
        f.write("The account_id below can be used for a targeted re-fetch to get the username.\n")
        f.write("-" * 70 + "\n")
        # Deduplicate by account_id so each unknown account appears once
        seen: set[str] = set()
        for e in truly_unknown:
            aid = e["account_id"]
            marker = " ← first occurrence" if aid not in seen else ""
            seen.add(aid)
            f.write(f"  account_id={aid}  tweet_id={e['tweet_id']}{marker}\n")
            f.write(f"    text: {e['text_preview']!r}\n")

    print(f"  → sparse author tweets log: {log_path}  ({len(found_elsewhere)} recoverable, {len(truly_unknown)} unknown)")




def stream_to_records(
    dirs: list[Path],
    *,
    limit: int | None = None,
    file: Path | None = None,
    log_dir: Path | None = None,
) -> tuple[dict[str, list[dict]], int, int]:
    """Read JSONL files and build per-table row dicts in a single streaming pass.

    Memory profile: only the final row dicts are kept alive. Raw tweet dicts and
    TweetBundle objects are discarded immediately after each tweet is processed —
    no intermediate list of all tweets or all bundles is ever held in memory.

    When log_dir is set, writes sparse_author_tweets.log — every tweet whose author
    had an empty username in that specific fetch, grouped by whether a username was
    eventually found in another tweet or remains truly unknown.

    Returns:
        records   — dict mapping table name → list of row dicts (deduped, FK-safe)
        raw_count — number of unique tweet_ids encountered
        skipped   — tweets dropped because required fields were missing
    """
    sources = [file] if file else [
        p
        for d in dirs
        if d.exists()
        for p in sorted(d.glob("*.jsonl"))
    ]

    # Per-table accumulator: dedup_key → row dict.
    # Using a dict (not a list) means deduplication is O(1) and costs only the key.
    tables: dict[str, dict[str, dict]] = {t: {} for t in INSERT_ORDER}

    def _add(table: str, key: str, row: dict) -> None:
        """Insert row into table accumulator; first occurrence wins."""
        if key not in tables[table]:
            tables[table][key] = row

    seen_tweet_ids: set[str] = set()   # cross-file dedup
    raw_count = 0
    skipped   = 0
    done      = False
    # Every (tweet_id, account_id, text_preview) where the author had no username.
    # Enriched after the loop to show whether a username was found elsewhere.
    sparse_author_events: list[dict] = []
    # Tracks the best (latest) tweet created_at seen per account for all_profile.
    # Profile data (avatar etc.) from the most recent tweet wins.
    profile_tweet_date: dict[str, str] = {}

    for path in tqdm(sources, desc="Processing files", unit="file"):
        if done:
            break
        for raw in load_jsonl(path):
            tweet_id = raw.get("tweet_id")
            if not tweet_id:
                continue
            tweet_id = str(tweet_id)
            if tweet_id in seen_tweet_ids:
                continue
            seen_tweet_ids.add(tweet_id)
            raw_count += 1

            # Build bundles for this tweet (main + nested quoted/RT).
            # Bundles go out of scope at the end of this block — GC-eligible.
            bundles = extract_all_bundles(raw)
            if not bundles:
                skipped += 1
            else:
                for b in bundles:
                    # Route to sparse bucket when username is missing so these
                    # rows never overwrite existing data (DO NOTHING on conflict).
                    has_username = bool(b.account.get("username"))
                    acct_key = "all_account" if has_username else "all_account_sparse"

                    # For all_account, prefer earliest created_at across all occurrences
                    # of the same account_id.  Nested author objects (quoted/RT) often
                    # lack account_created_at, so their created_at is a tweet-date
                    # fallback (e.g. 2025-08).  The real account creation date
                    # (e.g. 2019-07) is always lexicographically earlier in ISO 8601.
                    aid = b.account["account_id"]
                    if acct_key == "all_account":
                        existing = tables["all_account"].get(aid)
                        if existing is None or b.account.get("created_at", "") < existing.get("created_at", ""):
                            tables["all_account"][aid] = b.account
                    else:
                        _add(acct_key, aid, b.account)

                    if not has_username:
                        sparse_author_events.append({
                            "account_id":   b.account["account_id"],
                            "tweet_id":     b.tweet["tweet_id"],
                            "text_preview": b.tweet.get("full_text", "")[:100],
                        })
                    # all_profile: keep the row from the most recent tweet so the
                    # avatar reflects the latest known state for that account.
                    prof_aid    = b.profile["account_id"]
                    tweet_date  = b.tweet.get("created_at", "")
                    if tweet_date > profile_tweet_date.get(prof_aid, ""):
                        tables["all_profile"][prof_aid] = b.profile
                        profile_tweet_date[prof_aid]    = tweet_date

                    _add("tweets",         b.tweet["tweet_id"],       b.tweet)
                    for m in b.media:
                        _add("tweet_media", str(m["media_id"]), m)
                    for u in b.urls:
                        _add("tweet_urls", f"{u['tweet_id']}|{u['url']}", u)
                    for mu in b.mentioned_users:
                        _add("mentioned_users", mu["user_id"], mu)
                    for um in b.user_mentions:
                        _add("user_mentions", f"{um['tweet_id']}|{um['mentioned_user_id']}", um)
                    if b.conversation:
                        _add("conversations", b.conversation["tweet_id"], b.conversation)
                    if b.quote_tweet:
                        qt = b.quote_tweet
                        _add("quote_tweets", f"{qt['tweet_id']}|{qt['quoted_tweet_id']}", qt)
                    if b.retweet:
                        _add("retweets", b.retweet["tweet_id"], b.retweet)

                    # account_refresh_log: track min/max fetched_at per account.
                    # Only for accounts with a known username (sparse ones are noise).
                    if has_username and b.fetched_at:
                        aid   = b.account["account_id"]
                        entry = tables["account_refresh_log"].get(aid)
                        if entry is None:
                            tables["account_refresh_log"][aid] = {
                                "account_id":   aid,
                                "started_at":   b.fetched_at,
                                "completed_at": b.fetched_at,
                            }
                        else:
                            if b.fetched_at < entry["started_at"]:
                                entry["started_at"]   = b.fetched_at
                            if b.fetched_at > entry["completed_at"]:
                                entry["completed_at"] = b.fetched_at

            if limit and raw_count >= limit:
                done = True
                break

    # An account can appear in both buckets when different tweets by the same author
    # carry different data quality (one with username, one without).  Keep only the
    # sparse entry if the account has no good entry — good data always wins.
    good_account_ids = set(tables["all_account"].keys())
    tables["all_account_sparse"] = {
        k: v for k, v in tables["all_account_sparse"].items()
        if k not in good_account_ids
    }

    if log_dir and sparse_author_events:
        _write_sparse_author_tweets_log(sparse_author_events, good_account_ids, log_dir)

    # FK safety: drop relationship rows whose tweet_id wasn't successfully mapped.
    # This can happen when a nested tweet is skipped due to missing required fields.
    tweet_ids = set(tables["tweets"].keys())

    tables["conversations"] = {
        k: v for k, v in tables["conversations"].items() if v["tweet_id"] in tweet_ids
    }
    tables["quote_tweets"] = {
        k: v for k, v in tables["quote_tweets"].items() if v["tweet_id"] in tweet_ids
    }
    tables["retweets"] = {
        k: v for k, v in tables["retweets"].items()
        if v["tweet_id"] in tweet_ids
        and (v["retweeted_tweet_id"] is None or v["retweeted_tweet_id"] in tweet_ids)
    }

    records = {t: list(rows.values()) for t, rows in tables.items()}
    return records, raw_count, skipped


# ── DB insertion ──────────────────────────────────────────────────────────────

# Per-table schema: which columns to send, which conflict key to use, and which
# columns to refresh on conflict.  Mirrors the production PersistenceWorker's
# TABLE_CONFIGS in DbUtils.ts.
#
# columns    — sent in every INSERT
# conflict   — ON CONFLICT target (string = single col, list = composite)
# update     — columns refreshed via DO UPDATE SET col = EXCLUDED.col; [] → DO NOTHING
# update_sql — raw SQL expression for DO UPDATE SET (used when LEAST/GREATEST needed)
#
# all_account: created_at is intentionally excluded from `update` so the real
# Twitter account-creation date (set by archive uploads) is never overwritten
# by our tweet-date fallback.
TABLE_CONFIGS: dict[str, dict] = {
    "all_account": {
        "columns":  ["account_id", "created_via", "username", "created_at",
                     "account_display_name", "num_tweets", "num_following",
                     "num_followers", "num_likes"],
        "conflict": "account_id",
        "update":   ["username", "account_display_name",
                     "num_tweets", "num_following", "num_followers", "num_likes"],
    },
    # Sparse accounts (no username/display_name from API) use DO NOTHING so we
    # never overwrite existing data, but still establish the FK row if new.
    "all_account_sparse": {
        "sql_table": "all_account",   # actual DB table name
        "columns":  ["account_id", "created_via", "username", "created_at",
                     "account_display_name", "num_tweets", "num_following",
                     "num_followers", "num_likes"],
        "conflict": "account_id",
        "update":   [],               # DO NOTHING — never overwrite existing data
    },
    "all_profile": {
        "columns":  ["account_id", "avatar_media_url", "header_media_url",
                     "bio", "location", "website"],
        "conflict": "account_id",
        "update":   ["avatar_media_url", "header_media_url", "bio", "location", "website"],
    },
    # Widens the time window on each run: started_at moves earlier, completed_at later.
    "account_refresh_log": {
        "columns":  ["account_id", "started_at", "completed_at"],
        "conflict": "account_id",
        "update":   [],
        "update_sql": (
            "started_at   = LEAST(EXCLUDED.started_at,   account_refresh_log.started_at), "
            "completed_at = GREATEST(EXCLUDED.completed_at, account_refresh_log.completed_at)"
        ),
    },
    "mentioned_users": {
        "columns":  ["user_id", "name", "screen_name"],
        "conflict": "user_id",
        "update":   [],
    },
    "tweets": {
        "columns":  ["tweet_id", "account_id", "created_at", "full_text",
                     "favorite_count", "retweet_count",
                     "reply_to_tweet_id", "reply_to_user_id", "reply_to_username"],
        "conflict": "tweet_id",
        "update":   ["favorite_count", "retweet_count"],
    },
    "tweet_media": {
        "columns":  ["tweet_id", "media_id", "media_type", "media_url", "width", "height"],
        "conflict": "media_id",
        "update":   ["media_url", "width", "height"],
    },
    "tweet_urls": {
        "columns":  ["tweet_id", "url", "expanded_url", "display_url"],
        "conflict": ["tweet_id", "url"],
        "update":   ["expanded_url", "display_url"],
    },
    "user_mentions": {
        "columns":  ["tweet_id", "mentioned_user_id"],
        "conflict": ["tweet_id", "mentioned_user_id"],
        "update":   [],
    },
    "conversations": {
        "columns":  ["tweet_id", "conversation_id"],
        "conflict": "tweet_id",
        "update":   [],
    },
    "quote_tweets": {
        "columns":  ["tweet_id", "quoted_tweet_id"],
        "conflict": ["tweet_id", "quoted_tweet_id"],
        "update":   [],
    },
    "retweets": {
        "columns":  ["tweet_id", "retweeted_tweet_id"],
        "conflict": "tweet_id",
        "update":   ["retweeted_tweet_id"],
    },
}


def _build_upsert_sql(table: str) -> str:
    """Build the INSERT ... ON CONFLICT SQL for a table using its TABLE_CONFIGS entry.

    The optional sql_table key allows a logical table name (e.g. all_account_sparse)
    to insert into a different physical DB table (e.g. all_account).
    """
    cfg        = TABLE_CONFIGS[table]
    sql_table  = cfg.get("sql_table", table)   # physical DB table name
    cols       = cfg["columns"]
    conflict   = cfg["conflict"]
    update     = cfg["update"]
    update_sql = cfg.get("update_sql")         # raw SQL expression, e.g. LEAST/GREATEST

    col_list     = ", ".join(cols)
    placeholders = ", ".join(f"%({c})s" for c in cols)
    conflict_str = conflict if isinstance(conflict, str) else ", ".join(conflict)

    if update_sql:
        on_conflict = f"ON CONFLICT ({conflict_str}) DO UPDATE SET {update_sql}"
    elif update:
        update_str  = ", ".join(f"{c} = EXCLUDED.{c}" for c in update)
        on_conflict = f"ON CONFLICT ({conflict_str}) DO UPDATE SET {update_str}"
    else:
        on_conflict = f"ON CONFLICT ({conflict_str}) DO NOTHING"

    return f"INSERT INTO {sql_table} ({col_list}) VALUES ({placeholders}) {on_conflict}"


def _insert_batch(cur: psycopg.Cursor, table: str, rows: list[dict]) -> None:
    """Execute a bulk upsert for one table using a pre-built SQL template."""
    cur.executemany(_build_upsert_sql(table), rows)


def insert_all(
    records: dict[str, list[dict]],
    conn: psycopg.Connection | None,
    *,
    dry_run: bool = False,
    verbose: bool = False,
) -> None:
    """Insert all record tables in FK-safe order, committing after each table."""
    for table in INSERT_ORDER:
        rows = records.get(table) or []
        if not rows:
            print(f"  {table}: 0 rows — skip")
            continue

        if dry_run:
            cfg      = TABLE_CONFIGS[table]
            strategy = "DO UPDATE" if (cfg.get("update") or cfg.get("update_sql")) else "DO NOTHING"
            print(f"  {table}: would insert {len(rows)} rows  [{strategy}]")
            if verbose:
                print(f"    sample → {rows[0]}")
            continue

        n_batches = (len(rows) + BATCH_SIZE - 1) // BATCH_SIZE
        with conn.cursor() as cur:          # type: ignore[union-attr]
            for i in tqdm(
                range(0, len(rows), BATCH_SIZE),
                total=n_batches,
                desc=f"  {table}",
                unit="batch",
                leave=True,
            ):
                _insert_batch(cur, table, rows[i : i + BATCH_SIZE])
        conn.commit()                       # type: ignore[union-attr]


# ── Real-data validation ──────────────────────────────────────────────────────

def _write_sparse_accounts_log(
    sparse_accounts: list[dict],
    records: dict[str, list[dict]],
    log_path: Path,
) -> None:
    """Write an info log for sparse accounts (no username returned by API).

    These accounts will be inserted with DO NOTHING on conflict, so existing
    data is never overwritten.  This log documents which accounts are affected
    and what tweets they authored for future investigation.
    """
    tweets_by_account: dict[str, list[dict]] = {}
    for t in records.get("tweets", []):
        tweets_by_account.setdefault(t["account_id"], []).append(t)

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as f:
        f.write(f"Sparse accounts (no username from API) — {len(sparse_accounts)} accounts\n")
        f.write("These are inserted with DO NOTHING to protect existing DB data.\n")
        f.write("=" * 60 + "\n\n")
        for acct in sparse_accounts:
            aid = acct.get("account_id", "?")
            f.write(f"Account ({aid}):\n")
            for k, v in acct.items():
                f.write(f"  {k}: {v!r}\n")
            tweets = tweets_by_account.get(aid, [])
            f.write(f"\nTweets by this account ({len(tweets)}):\n")
            for tw in tweets:
                f.write(
                    f"  tweet_id={tw['tweet_id']}"
                    f"  created_at={tw.get('created_at', '?')}"
                    f"  text={tw.get('full_text', '')[:80]!r}\n"
                )
            f.write("\n" + "-" * 60 + "\n\n")

    print(f"    → sparse accounts log written to {log_path}")


def validate_records(
    records: dict[str, list[dict]],
    *,
    raw_count: int,
    skipped: int,
    log_dir: Path | None = None,
) -> bool:
    """Run structural assertions on real parsed data.

    Unlike the unit test suite (which uses synthetic fixtures), this function
    operates on the actual output of a full parse run.  Call it after
    stream_to_records() to get a data-quality report before writing to the DB.

    When log_dir is provided, detailed inspection files are written there for
    any issues that benefit from deeper investigation (e.g. empty usernames).

    Returns True if all checks pass.
    """

    def _check(name: str, cond: bool, detail: str = "") -> bool:
        mark = "✓" if cond else "✗"
        suffix = f"  → {detail}" if detail and not cond else (f"  ({detail})" if detail else "")
        print(f"    {mark}  {name}{suffix}")
        return cond

    tweet_ids = {r["tweet_id"] for r in records.get("tweets", [])}
    ok = True

    # ── 1. Volume checks ──────────────────────────────────────────────────────
    print("\n  [volume]")
    ok &= _check("tweets table is not empty", len(tweet_ids) > 0)
    ok &= _check("all_account table is not empty", len(records.get("all_account", [])) > 0)

    if raw_count > 0:
        skip_pct = 100 * skipped / raw_count
        ok &= _check(
            f"skip rate < 10%  ({skipped}/{raw_count} = {skip_pct:.1f}%)",
            skip_pct < 10,
            f"{skip_pct:.1f}% tweets were dropped due to missing required fields",
        )

    # Accounts should cover every distinct account_id in tweets.
    # Both all_account (good) and all_account_sparse (incomplete) count here
    # since both produce a valid FK row in the DB.
    tweet_account_ids = {r["account_id"] for r in records.get("tweets", [])}
    account_ids = (
        {r["account_id"] for r in records.get("all_account", [])}
        | {r["account_id"] for r in records.get("all_account_sparse", [])}
    )
    missing_accounts = tweet_account_ids - account_ids
    ok &= _check(
        "every tweet account_id has an all_account row",
        len(missing_accounts) == 0,
        f"{len(missing_accounts)} account_ids missing: {list(missing_accounts)[:5]}",
    )

    sparse = records.get("all_account_sparse", [])
    if sparse:
        print(f"    ℹ  {len(sparse)} sparse accounts (no username from API) → will insert with DO NOTHING")
        if log_dir:
            _write_sparse_accounts_log(sparse, records, log_dir / "sparse_accounts.log")

    # ── 2. Required fields (NOT NULL in DB schema) ────────────────────────────
    print("\n  [required fields]")

    def _null_check(table: str, col: str) -> bool:
        rows = records.get(table, [])
        bad  = [r for r in rows if r.get(col) is None or r.get(col) == ""]
        return _check(
            f"{table}.{col} never null/empty",
            len(bad) == 0,
            f"{len(bad)} rows with null/empty {col}",
        )

    ok &= _null_check("tweets",      "tweet_id")
    ok &= _null_check("tweets",      "account_id")
    ok &= _null_check("tweets",      "created_at")
    ok &= _null_check("all_account", "account_id")
    ok &= _null_check("all_account", "created_at")
    ok &= _null_check("all_account", "username")   # sparse accounts are now separate
    ok &= _null_check("all_profile", "account_id")
    ok &= _null_check("tweet_media", "tweet_id")
    ok &= _null_check("tweet_media", "media_id")
    ok &= _null_check("tweet_urls",  "tweet_id")
    ok &= _null_check("tweet_urls",  "url")

    # ── 3. Type integrity ─────────────────────────────────────────────────────
    print("\n  [type integrity]")

    bad_media_ids = [
        r["media_id"] for r in records.get("tweet_media", [])
        if not isinstance(r.get("media_id"), int)
    ]
    ok &= _check(
        "tweet_media.media_id is always int",
        len(bad_media_ids) == 0,
        f"{len(bad_media_ids)} non-int media_ids: {bad_media_ids[:5]}",
    )

    bad_dates = [
        r["created_at"] for r in records.get("tweets", [])
        if r.get("created_at") and not str(r["created_at"]).startswith(("19", "20"))
    ]
    ok &= _check(
        "tweets.created_at looks like ISO date",
        len(bad_dates) == 0,
        f"{len(bad_dates)} suspicious dates: {bad_dates[:3]}",
    )

    # ── 4. FK consistency (within our batch) ──────────────────────────────────
    print("\n  [FK consistency]")

    def _fk_check(table: str, col: str, ref_ids: set, *, allow_null: bool = False) -> bool:
        rows = records.get(table, [])
        bad  = [
            r[col] for r in rows
            if r.get(col) is not None and r[col] not in ref_ids
        ] if allow_null else [
            r[col] for r in rows
            if r.get(col) not in ref_ids
        ]
        label = f"{table}.{col} → tweets" if ref_ids is tweet_ids else f"{table}.{col} FK"
        return _check(label, len(bad) == 0, f"{len(bad)} dangling refs: {bad[:5]}")

    ok &= _fk_check("conversations",  "tweet_id",           tweet_ids)
    ok &= _fk_check("quote_tweets",   "tweet_id",           tweet_ids)
    ok &= _fk_check("retweets",       "tweet_id",           tweet_ids)
    ok &= _fk_check("user_mentions",  "tweet_id",           tweet_ids)
    ok &= _fk_check("tweet_media",    "tweet_id",           tweet_ids)
    ok &= _fk_check("tweet_urls",     "tweet_id",           tweet_ids)

    # quoted_tweet_id has no DB FK but we can still flag if it's unexpectedly empty
    qt_rows   = records.get("quote_tweets", [])
    bad_qt_id = [r for r in qt_rows if not r.get("quoted_tweet_id")]
    ok &= _check(
        "quote_tweets.quoted_tweet_id never null",
        len(bad_qt_id) == 0,
        f"{len(bad_qt_id)} rows with null quoted_tweet_id",
    )

    good_account_ids = {r["account_id"] for r in records.get("all_account", [])}
    rl_rows = records.get("account_refresh_log", [])
    bad_rl_fk = [r["account_id"] for r in rl_rows if r["account_id"] not in good_account_ids]
    ok &= _check(
        "account_refresh_log.account_id → all_account",
        len(bad_rl_fk) == 0,
        f"{len(bad_rl_fk)} dangling refs: {bad_rl_fk[:5]}",
    )
    bad_rl_window = [r for r in rl_rows if r.get("started_at", "") > r.get("completed_at", "")]
    ok &= _check(
        "account_refresh_log: started_at ≤ completed_at",
        len(bad_rl_window) == 0,
        f"{len(bad_rl_window)} rows where started_at > completed_at",
    )
    print(f"    ℹ  {len(rl_rows)} account_refresh_log entries")

    # ── 5. Summary ────────────────────────────────────────────────────────────
    print()
    if ok:
        print("  All validation checks passed.")
    else:
        print("  Some checks FAILED — review output above before running live.")

    return ok


# ── Test suite ────────────────────────────────────────────────────────────────

def _collect_from_bundles(bundles: list[TweetBundle]) -> dict[str, list[dict]]:
    """Test helper: aggregate a list of bundles into per-table records.

    Mirrors the accumulation logic inside stream_to_records so tests can build
    records from synthetic bundles without touching the filesystem.
    """
    tables: dict[str, dict] = {t: {} for t in INSERT_ORDER}
    profile_tweet_date: dict[str, str] = {}

    def _add(table: str, key: str, row: dict) -> None:
        if key not in tables[table]:
            tables[table][key] = row

    for b in bundles:
        has_username = bool(b.account.get("username"))
        acct_key = "all_account" if has_username else "all_account_sparse"

        aid = b.account["account_id"]
        if acct_key == "all_account":
            existing = tables["all_account"].get(aid)
            if existing is None or b.account.get("created_at", "") < existing.get("created_at", ""):
                tables["all_account"][aid] = b.account
        else:
            _add(acct_key, aid, b.account)

        prof_aid   = b.profile["account_id"]
        tweet_date = b.tweet.get("created_at", "")
        if tweet_date > profile_tweet_date.get(prof_aid, ""):
            tables["all_profile"][prof_aid] = b.profile
            profile_tweet_date[prof_aid]    = tweet_date
        _add("tweets",         b.tweet["tweet_id"],       b.tweet)
        for m in b.media:
            _add("tweet_media", str(m["media_id"]), m)
        for u in b.urls:
            _add("tweet_urls", f"{u['tweet_id']}|{u['url']}", u)
        for mu in b.mentioned_users:
            _add("mentioned_users", mu["user_id"], mu)
        for um in b.user_mentions:
            _add("user_mentions", f"{um['tweet_id']}|{um['mentioned_user_id']}", um)
        if b.conversation:
            _add("conversations", b.conversation["tweet_id"], b.conversation)
        if b.quote_tweet:
            qt = b.quote_tweet
            _add("quote_tweets", f"{qt['tweet_id']}|{qt['quoted_tweet_id']}", qt)
        if b.retweet:
            _add("retweets", b.retweet["tweet_id"], b.retweet)

        if has_username and b.fetched_at:
            aid   = b.account["account_id"]
            entry = tables["account_refresh_log"].get(aid)
            if entry is None:
                tables["account_refresh_log"][aid] = {
                    "account_id":   aid,
                    "started_at":   b.fetched_at,
                    "completed_at": b.fetched_at,
                }
            else:
                if b.fetched_at < entry["started_at"]:
                    entry["started_at"]   = b.fetched_at
                if b.fetched_at > entry["completed_at"]:
                    entry["completed_at"] = b.fetched_at

    tweet_ids = set(tables["tweets"].keys())
    tables["retweets"] = {
        k: v for k, v in tables["retweets"].items()
        if v["tweet_id"] in tweet_ids
        and (v["retweeted_tweet_id"] is None or v["retweeted_tweet_id"] in tweet_ids)
    }

    return {t: list(rows.values()) for t, rows in tables.items()}


_AUTHOR = {
    "rest_id":            "111",
    "name":               "Alice",
    "screen_name":        "alice",
    "followers_count":    100,
    "favourites_count":   50,
    "avatar":             "https://pbs.twimg.com/profile_images/alice.jpg",
    "blue_verified":      False,
    "account_created_at": "2019-05-01T12:00:00+00:00",
    "num_tweets":         500,
    "num_following":      80,
    "num_followers":      100,
    "num_likes":          50,
}

_TWEET = {
    "tweet_id":       "1001",
    "created_at":     "Thu Feb 26 17:48:52 +0000 2026",
    "text":           "Hello world!",
    "favorites":      5,
    "retweets":       2,
    "quotes":         1,
    "conversation_id": "1001",
    "views":          "500",
    "media":          [],
    "entities":       {"urls": [], "user_mentions": [], "hashtags": [], "symbols": [], "timestamps": []},
    "author":         _AUTHOR,
}


def _ok(name: str, cond: bool, detail: str = "") -> bool:
    mark = "✓" if cond else "✗"
    print(f"    {mark} {name}" + (f"  ({detail})" if detail and not cond else ""))
    return cond


def test_parse_date() -> bool:
    p = True
    p &= _ok("valid Twitter date → ISO",    bool(parse_twitter_date("Thu Feb 26 17:48:52 +0000 2026")))
    p &= _ok("ISO contains correct date",   "2026-02-26" in (parse_twitter_date("Thu Feb 26 17:48:52 +0000 2026") or ""))
    p &= _ok("empty string → None",         parse_twitter_date("") is None)
    p &= _ok("invalid string → None",       parse_twitter_date("not a date") is None)
    return p


def test_simple_tweet() -> bool:
    b = _build_single_bundle(_TWEET, is_main=True)
    p  = _ok("bundle created",              b is not None)
    if not b: return False
    p &= _ok("tweet_id",                    b.tweet["tweet_id"] == "1001")
    p &= _ok("account_id",                  b.tweet["account_id"] == "111")
    p &= _ok("full_text",                   b.tweet["full_text"] == "Hello world!")
    p &= _ok("favorite_count = 5",          b.tweet["favorite_count"] == 5)
    p &= _ok("retweet_count = retweets+quotes = 3", b.tweet["retweet_count"] == 3)
    p &= _ok("reply fields are None",       b.tweet["reply_to_tweet_id"] is None)
    p &= _ok("account username",            b.account["username"] == "alice")
    p &= _ok("account created_via",        b.account["created_via"] == "twitter_fetched")
    p &= _ok("account_created_at used",    b.account["created_at"] == "2019-05-01T12:00:00+00:00")
    p &= _ok("num_tweets populated",       b.account["num_tweets"] == 500)
    p &= _ok("num_following populated",    b.account["num_following"] == 80)
    p &= _ok("profile avatar set",         b.profile["avatar_media_url"] is not None)
    p &= _ok("conversation captured",       b.conversation is not None)
    p &= _ok("conversation_id correct",     (b.conversation or {}).get("conversation_id") == "1001")
    p &= _ok("no quote_tweet on plain tweet", b.quote_tweet is None)
    p &= _ok("no retweet on plain tweet",   b.retweet is None)
    return p


def test_account_created_at_fallback() -> bool:
    """Author without account_created_at → falls back to tweet's created_at."""
    author_no_ts = {k: v for k, v in _AUTHOR.items() if k != "account_created_at"}
    raw = {**_TWEET, "author": author_no_ts}
    b = _build_single_bundle(raw, is_main=True)
    p = _ok("bundle created", b is not None)
    if b:
        p &= _ok("created_at falls back to tweet date",
                 b.account["created_at"] == "2026-02-26T17:48:52+00:00")
    return p


def test_reply_tweet() -> bool:
    raw = {**_TWEET, "tweet_id": "1002", "in_reply_to_status_id_str": "999"}
    b   = _build_single_bundle(raw, is_main=True)
    p   = _ok("bundle created",             b is not None)
    if b:
        p &= _ok("reply_to_tweet_id set",   b.tweet["reply_to_tweet_id"] == "999")
    return p


def test_null_tweet_id_skipped() -> bool:
    raw = {**_TWEET, "tweet_id": None}
    return _ok("null tweet_id → None", _build_single_bundle(raw, is_main=True) is None)


def test_null_account_id_skipped() -> bool:
    raw = {**_TWEET, "author": {**_AUTHOR, "rest_id": None}}
    return _ok("null account_id → None", _build_single_bundle(raw, is_main=True) is None)


def test_missing_author_skipped() -> bool:
    raw = {**_TWEET, "author": {}}
    return _ok("missing author → None", _build_single_bundle(raw, is_main=True) is None)


def test_invalid_date_skipped() -> bool:
    raw = {**_TWEET, "created_at": "not-a-date"}
    return _ok("invalid date → None", _build_single_bundle(raw, is_main=True) is None)


def test_quote_tweet() -> bool:
    quoted = {**_TWEET, "tweet_id": "2001", "author": {**_AUTHOR, "rest_id": "222"}}
    raw    = {**_TWEET, "tweet_id": "1003", "quoted": quoted}
    bs     = extract_all_bundles(raw)
    ids    = {b.tweet["tweet_id"] for b in bs}
    p  = _ok("2 bundles (main + QT)",       len(bs) == 2, str(ids))
    main   = next((b for b in bs if b.tweet["tweet_id"] == "1003"), None)
    qt     = next((b for b in bs if b.tweet["tweet_id"] == "2001"), None)
    if main:
        p &= _ok("quote_tweet set on main",         main.quote_tweet is not None)
        p &= _ok("quoted_tweet_id = 2001",          (main.quote_tweet or {}).get("quoted_tweet_id") == "2001")
    if qt:
        p &= _ok("QT bundle has no quote_tweet rel", qt.quote_tweet is None)
    return p


def test_retweet() -> bool:
    orig = {**_TWEET, "tweet_id": "3001", "author": {**_AUTHOR, "rest_id": "333"}}
    raw  = {**_TWEET, "tweet_id": "1004", "text": "RT @alice: Hello!",
            "retweeted_tweet": orig}
    bs   = extract_all_bundles(raw)
    ids  = {b.tweet["tweet_id"] for b in bs}
    p  = _ok("2 bundles (RT + original)",   len(bs) == 2, str(ids))
    rt   = next((b for b in bs if b.tweet["tweet_id"] == "1004"), None)
    if rt:
        p &= _ok("retweet rel set",             rt.retweet is not None)
        p &= _ok("retweeted_tweet_id = 3001",   (rt.retweet or {}).get("retweeted_tweet_id") == "3001")
    return p


def test_nested_quote_in_retweet() -> bool:
    """RT of a tweet that itself quotes something → 3 bundles."""
    nqt  = {**_TWEET, "tweet_id": "9001", "author": {**_AUTHOR, "rest_id": "999"}}
    orig = {**_TWEET, "tweet_id": "8001", "author": {**_AUTHOR, "rest_id": "888"}, "quoted": nqt}
    raw  = {**_TWEET, "tweet_id": "7001", "retweeted_tweet": orig}
    bs   = extract_all_bundles(raw)
    ids  = {b.tweet["tweet_id"] for b in bs}
    return _ok("3 bundles: RT + original + nested QT", ids == {"7001", "8001", "9001"}, str(ids))


def test_media_photo() -> bool:
    raw = {
        **_TWEET, "tweet_id": "1010",
        "media": {"photo": [{"media_url_https": "https://pbs.twimg.com/media/test.jpg",
                              "id": "9876543210", "sizes": {"h": 1200, "w": 900}}]},
    }
    b = _build_single_bundle(raw, is_main=True)
    p = _ok("1 media row produced", b is not None and len(b.media) == 1)
    if b and b.media:
        m = b.media[0]
        p &= _ok("media_id cast to int",    m["media_id"] == 9876543210)
        p &= _ok("media_type = photo",      m["media_type"] == "photo")
        p &= _ok("width = 900",             m["width"] == 900)
        p &= _ok("height = 1200",           m["height"] == 1200)
    return p


def test_media_empty_list() -> bool:
    b = _build_single_bundle(_TWEET, is_main=True)
    return _ok("media=[] → no rows", b is not None and b.media == [])


def test_url_extraction() -> bool:
    raw = {**_TWEET, "tweet_id": "1020", "entities": {
        **_TWEET["entities"],
        "urls": [{"url": "https://t.co/abc", "expanded_url": "https://example.com",
                  "display_url": "example.com"}],
    }}
    b = _build_single_bundle(raw, is_main=True)
    p = _ok("1 url row produced", b is not None and len(b.urls) == 1)
    if b and b.urls:
        p &= _ok("url captured",          b.urls[0]["url"] == "https://t.co/abc")
        p &= _ok("expanded_url captured", b.urls[0]["expanded_url"] == "https://example.com")
    return p


def test_mention_extraction() -> bool:
    raw = {**_TWEET, "tweet_id": "1030", "entities": {
        **_TWEET["entities"],
        "user_mentions": [
            {"id_str": "555", "name": "Bob",   "screen_name": "bob"},
            {"id_str": "666", "name": "Carol", "screen_name": "carol"},
            {"id_str": "555", "name": "Bob",   "screen_name": "bob"},  # duplicate
        ],
    }}
    b = _build_single_bundle(raw, is_main=True)
    p  = _ok("bundle created", b is not None)
    if b:
        p &= _ok("2 unique mentioned_users (deduped)", len(b.mentioned_users) == 2)
        p &= _ok("2 user_mention rows",                len(b.user_mentions)   == 2)
    return p


def test_deduplication() -> bool:
    """Same tweet_id from two files → only one row after collection."""
    t1 = {**_TWEET, "tweet_id": "9999", "favorites": 5}
    t2 = {**_TWEET, "tweet_id": "9999", "favorites": 99}  # same id, different count
    bs = extract_all_bundles(t1) + extract_all_bundles(t2)
    recs = _collect_from_bundles(bs)
    matching = [r for r in recs["tweets"] if r["tweet_id"] == "9999"]
    return _ok("duplicate tweet_id → 1 row", len(matching) == 1)


def test_fk_safety_dangling_retweet() -> bool:
    """If retweeted tweet is skipped (bad data), retweet row should be dropped."""
    # Force original to be skipped by giving it a null tweet_id
    bad_orig = {**_TWEET, "tweet_id": None, "author": {**_AUTHOR, "rest_id": "333"}}
    raw = {**_TWEET, "tweet_id": "1005", "retweeted_tweet": bad_orig}
    bs  = extract_all_bundles(raw)
    recs = _collect_from_bundles(bs)
    # The RT wrapper tweet should exist, but retweeted_tweet_id won't be in our set
    # because bad_orig was skipped. _collect_from_bundles should filter it out.
    dangling = [r for r in recs["retweets"] if r.get("retweeted_tweet_id") not in {None, ""}
                and r["retweeted_tweet_id"] not in {t["tweet_id"] for t in recs["tweets"]}]
    return _ok("dangling retweet FK dropped", len(dangling) == 0)


def test_profile_latest_tweet_date_wins() -> bool:
    """Profile (avatar) from the most recent tweet should win over an earlier one."""
    old_author = {**_AUTHOR, "avatar": "https://pbs.twimg.com/old_avatar.jpg"}
    new_author = {**_AUTHOR, "avatar": "https://pbs.twimg.com/new_avatar.jpg"}
    old_raw = {**_TWEET, "tweet_id": "P1", "created_at": "Mon Jan 01 00:00:00 +0000 2024",
               "author": old_author}
    new_raw = {**_TWEET, "tweet_id": "P2", "created_at": "Thu Feb 26 17:00:00 +0000 2026",
               "author": new_author}

    # Old tweet processed first
    recs = _collect_from_bundles(extract_all_bundles(old_raw) + extract_all_bundles(new_raw))
    profiles = [r for r in recs["all_profile"] if r["account_id"] == _AUTHOR["rest_id"]]
    p  = _ok("exactly 1 profile row",           len(profiles) == 1)
    if profiles:
        p &= _ok("latest tweet's avatar wins",  profiles[0]["avatar_media_url"] == "https://pbs.twimg.com/new_avatar.jpg")
        p &= _ok("old avatar discarded",        profiles[0]["avatar_media_url"] != "https://pbs.twimg.com/old_avatar.jpg")
    return p


def test_account_created_at_earliest_wins() -> bool:
    """Nested author objects (quoted/RT) lack account_created_at and fall back to the
    tweet date.  When the same account appears later with a real account_created_at,
    the earlier (real) date must win over the later fallback date."""
    # Simulate a nested author — no account_created_at, fallback will be tweet date 2025-08-08
    nested_author = {k: v for k, v in _AUTHOR.items() if k != "account_created_at"}
    nested_raw    = {**_TWEET, "tweet_id": "N1", "created_at": "Fri Aug 08 23:28:29 +0000 2025",
                     "author": nested_author}
    # Simulate a top-level tweet with the real account_created_at = 2019-07-09
    full_raw      = {**_TWEET, "tweet_id": "N2"}   # _TWEET author has account_created_at

    # Process nested first (as happens alphabetically in the file stream)
    recs = _collect_from_bundles(extract_all_bundles(nested_raw) + extract_all_bundles(full_raw))
    accounts = [r for r in recs["all_account"] if r["account_id"] == _AUTHOR["rest_id"]]
    p  = _ok("exactly 1 all_account row",          len(accounts) == 1)
    if accounts:
        p &= _ok("real account_created_at wins",   accounts[0]["created_at"] == "2019-05-01T12:00:00+00:00")
        p &= _ok("fallback date discarded",        accounts[0]["created_at"] != "2025-08-08T23:28:29+00:00")
    return p


def test_refresh_log_single_tweet() -> bool:
    """A single tweet with updated_at produces one refresh_log entry where started = completed."""
    raw  = {**_TWEET, "updated_at": "2026-03-02T17:43:57+00:00"}
    recs = _collect_from_bundles(extract_all_bundles(raw))
    rl   = recs.get("account_refresh_log", [])
    p    = _ok("1 refresh_log entry",              len(rl) == 1)
    if rl:
        p &= _ok("started_at == completed_at",     rl[0]["started_at"] == rl[0]["completed_at"])
        p &= _ok("timestamp preserved",            rl[0]["started_at"] == "2026-03-02T17:43:57+00:00")
        p &= _ok("account_id correct",             rl[0]["account_id"] == _AUTHOR["rest_id"])
    return p


def test_refresh_log_window() -> bool:
    """Two tweets for the same account produce started_at=min, completed_at=max."""
    t1   = {**_TWEET, "tweet_id": "A1", "updated_at": "2026-03-01T10:00:00+00:00"}
    t2   = {**_TWEET, "tweet_id": "A2", "updated_at": "2026-03-02T20:00:00+00:00"}
    recs = _collect_from_bundles(extract_all_bundles(t1) + extract_all_bundles(t2))
    rl   = recs.get("account_refresh_log", [])
    p    = _ok("1 refresh_log entry (same account)", len(rl) == 1)
    if rl:
        p &= _ok("started_at = earliest", rl[0]["started_at"]   == "2026-03-01T10:00:00+00:00")
        p &= _ok("completed_at = latest", rl[0]["completed_at"] == "2026-03-02T20:00:00+00:00")
    return p


def test_refresh_log_sparse_excluded() -> bool:
    """Sparse accounts (no username) must not appear in account_refresh_log."""
    sparse_author = {**_AUTHOR, "screen_name": ""}
    raw  = {**_TWEET, "author": sparse_author, "updated_at": "2026-03-02T17:43:57+00:00"}
    recs = _collect_from_bundles(extract_all_bundles(raw))
    rl   = recs.get("account_refresh_log", [])
    return _ok("sparse account → no refresh_log entry", len(rl) == 0)


def run_tests() -> bool:
    suite = [
        ("parse_date",                  test_parse_date),
        ("simple tweet mapping",        test_simple_tweet),
        ("account_created_at fallback", test_account_created_at_fallback),
        ("reply tweet",                 test_reply_tweet),
        ("null tweet_id skipped",       test_null_tweet_id_skipped),
        ("null account_id skipped",     test_null_account_id_skipped),
        ("missing author skipped",      test_missing_author_skipped),
        ("invalid date skipped",        test_invalid_date_skipped),
        ("quote tweet",                 test_quote_tweet),
        ("retweet",                     test_retweet),
        ("nested quote in retweet",     test_nested_quote_in_retweet),
        ("media photo",                 test_media_photo),
        ("media empty list",            test_media_empty_list),
        ("url extraction",              test_url_extraction),
        ("mention extraction + dedup",  test_mention_extraction),
        ("tweet deduplication",              test_deduplication),
        ("FK safety: dangling retweet",      test_fk_safety_dangling_retweet),
        ("profile: latest tweet date wins",   test_profile_latest_tweet_date_wins),
        ("account created_at: earliest wins", test_account_created_at_earliest_wins),
        ("refresh_log: single tweet",        test_refresh_log_single_tweet),
        ("refresh_log: time window",         test_refresh_log_window),
        ("refresh_log: sparse excluded",     test_refresh_log_sparse_excluded),
    ]

    passed = failed = 0
    for name, fn in suite:
        print(f"\n  [{name}]")
        try:
            ok = fn()
            passed += 1 if ok else 0
            failed += 0 if ok else 1
        except Exception as exc:
            print(f"    ✗ EXCEPTION: {exc}")
            failed += 1

    print(f"\n{'─' * 40}")
    print(f"  {passed} passed  |  {failed} failed  |  {passed + failed} total")
    return failed == 0


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Insert fresh JSONL tweets into the Community Archive DB.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--test",     action="store_true", help="Run built-in test suite")
    parser.add_argument("--dry-run",  action="store_true", help="Parse and print without writing to DB")
    parser.add_argument("--validate", action="store_true", help="Run data-quality checks on parsed output (auto-enabled with --dry-run)")
    parser.add_argument("--verbose",  action="store_true", help="Print a sample row per table in dry-run")
    parser.add_argument("--file",     type=Path,           help="Process a single JSONL file instead of all files")
    parser.add_argument("--limit",    type=int,            help="Cap the number of tweets to process")
    parser.add_argument("--dirs",     nargs="+", type=Path, help="Override default input directories")
    args = parser.parse_args()

    if args.test:
        print("Running test suite...\n")
        ok = run_tests()
        sys.exit(0 if ok else 1)

    if not args.dry_run and not POSTGRES_PASSWORD:
        print("Error: POSTGRES_PASSWORD env var is required for live runs.")
        print("  Find it in Supabase → Settings → Database → Connection string.")
        print("  export POSTGRES_PASSWORD=<your-db-password>")
        print("  Or use --dry-run to test without writing to the DB.")
        sys.exit(1)

    input_dirs = args.dirs or DEFAULT_DIRS

    # ── Stream: load + parse + collect in one pass ────────────────────────────
    print("Streaming JSONL files → DB rows...")
    records, raw_count, skipped = stream_to_records(
        input_dirs,
        limit=args.limit,
        file=args.file,
        log_dir=SCRIPT_DIR / "outputs",
    )
    print(f"  {raw_count} unique tweets processed  |  {skipped} skipped (bad data)")

    print("\nRecord counts per table:")
    for table in INSERT_ORDER:
        print(f"  {table}: {len(records.get(table, []))}")

    # Validation runs automatically on dry-run (safe read-only check) or when
    # explicitly requested with --validate before a live run.
    if args.dry_run or args.validate:
        print("\nValidating parsed data...")
        valid = validate_records(
            records,
            raw_count=raw_count,
            skipped=skipped,
            log_dir=SCRIPT_DIR / "outputs",
        )
        if not valid and not args.dry_run:
            print("\nAborting live run due to validation failures.")
            sys.exit(1)

    # ── Insert ────────────────────────────────────────────────────────────────
    mode = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{mode}Inserting...")

    if args.dry_run:
        insert_all(records, conn=None, dry_run=True, verbose=args.verbose)
    else:
        with psycopg.connect(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            dbname=POSTGRES_DB,
        ) as conn:
            insert_all(records, conn)

    print("\nDone.")


if __name__ == "__main__":
    main()
