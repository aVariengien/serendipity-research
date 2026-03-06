# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "tqdm",
# ]
# ///

# %% Config & imports
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

# ── Paths ─────────────────────────────────────────────────────────────────────
CA_MINING_DIR = Path(__file__).parent
FRESH_DIR     = CA_MINING_DIR / "outputs_fresh" / "tweets_live"
PLAN_CSV      = CA_MINING_DIR / "outputs_fresh" / "fetch_plan.csv"
OUT_CSV       = CA_MINING_DIR / "scrape_estimate.csv"

# ── Twitter RapidAPI ──────────────────────────────────────────────────────────
RAPID_API_KEY = os.environ["RAPID_API_KEY"]
TW_HEADERS = {
    "x-rapidapi-host": "twitter-api45.p.rapidapi.com",
    "x-rapidapi-key": RAPID_API_KEY,
}
TW_SCREENINFO_URL = "https://twitter-api45.p.rapidapi.com/screenname.php"

CONCURRENCY = 10
MAX_RETRIES = 3
RETRY_DELAY = 5.0

TODAY = datetime.now(timezone.utc)


# %% Helpers

def parse_twitter_dt(s: str) -> datetime:
    return parsedate_to_datetime(s).replace(tzinfo=timezone.utc)


def analyze_jsonl(path: Path, cutoff: datetime) -> dict:
    """
    Read a tweets_live JSONL file and return:
    - tweet_count : number of tweets in the file
    - min_date    : oldest tweet date
    - max_date    : newest tweet date
    - rate_per_day: tweets/day over (max_date - cutoff) period
    - days_since_cutoff: (today - cutoff).days
    - estimated_total: rate * days_since_cutoff  [tweets from cutoff to today]
    - days_covered: (max_date - cutoff).days used to compute the rate
    """
    dates: list[datetime] = []
    count = 0

    try:
        with path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    tweet = json.loads(line)
                    dt = parse_twitter_dt(tweet["created_at"])
                    dates.append(dt)
                    count += 1
                except Exception:
                    continue
    except FileNotFoundError:
        return {"error": "jsonl_not_found", "tweet_count": 0}

    if count == 0:
        return {"error": "empty_file", "tweet_count": 0}

    min_date = min(dates)
    max_date = max(dates)
    days_covered = max((max_date - cutoff).days, 1)
    rate_per_day = count / days_covered
    days_since_cutoff = max((TODAY - cutoff).days, 1)
    estimated_total = round(rate_per_day * days_since_cutoff)

    return {
        "tweet_count": count,
        "min_date": min_date.date().isoformat(),
        "max_date": max_date.date().isoformat(),
        "days_covered": days_covered,
        "rate_per_day": round(rate_per_day, 2),
        "days_since_cutoff": days_since_cutoff,
        "estimated_total": estimated_total,
    }


async def fetch_screeninfo(
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    username: str,
    pbar: tqdm,
) -> dict:
    """Call screeninfo.php and return statuses_count (all-time tweet count)."""
    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                resp = await client.get(
                    TW_SCREENINFO_URL,
                    params={"screenname": username},
                    headers=TW_HEADERS,
                    timeout=30.0,
                )
                resp.raise_for_status()
                data = resp.json()

                # API may nest user info under a key or return it flat
                statuses = (
                    data.get("statuses_count")
                    or (data.get("user") or {}).get("statuses_count")
                )
                followers = (
                    data.get("followers_count")
                    or (data.get("user") or {}).get("followers_count")
                )
                name = (
                    data.get("name")
                    or (data.get("user") or {}).get("name")
                    or username
                )
                pbar.update(1)
                return {
                    "username": username,
                    "statuses_count": statuses,
                    "followers_count": followers,
                    "display_name": name,
                    "raw_status": data.get("status", "ok"),
                }

            except Exception as exc:
                if attempt == MAX_RETRIES - 1:
                    pbar.update(1)
                    tqdm.write(f"  [ERROR] {username}: {exc}", file=sys.stderr)
                    return {"username": username, "statuses_count": None, "error": str(exc)}
                await asyncio.sleep(RETRY_DELAY * (attempt + 1))
    return {"username": username, "statuses_count": None, "error": "max_retries"}


# %% Main

async def main() -> None:
    # ── Load fetch plan ───────────────────────────────────────────────────────
    if not PLAN_CSV.exists():
        print(f"ERROR: fetch_plan.csv not found at {PLAN_CSV}", file=sys.stderr)
        print("Run:  uv run fetch_live_tweets.py --plan  to generate it first.")
        sys.exit(1)

    with PLAN_CSV.open(encoding="utf-8") as f:
        plan = list(csv.DictReader(f))

    users_with_archive   = [r for r in plan if r["fetch_from_cutoff"] != "full_timeline"]
    users_full_timeline  = [r for r in plan if r["fetch_from_cutoff"] == "full_timeline"]

    print(f"Loaded {len(plan):,} users from fetch_plan.csv")
    print(f"  {len(users_with_archive):,} with archive cutoff")
    print(f"  {len(users_full_timeline):,} with full_timeline (no archive upload)\n")

    results: list[dict] = []

    # ── Users with archive: compute rate from .jsonl files ───────────────────
    print("Analyzing .jsonl files for users with archive cutoff …")
    for row in tqdm(users_with_archive, unit=" users"):
        username = row["username"]
        try:
            cutoff = datetime.fromisoformat(row["fetch_from_cutoff"].replace("Z", "+00:00"))
        except Exception:
            results.append({
                "username": username,
                "has_archive": True,
                "archive_cutoff": row["fetch_from_cutoff"],
                "error": "bad_cutoff_date",
            })
            continue

        jsonl_path = FRESH_DIR / f"{username}.jsonl"
        stats = analyze_jsonl(jsonl_path, cutoff)

        results.append({
            "username": username,
            "has_archive": True,
            "archive_cutoff": cutoff.date().isoformat(),
            **stats,
        })

    # ── Users without archive: call screeninfo API ────────────────────────────
    if users_full_timeline:
        print(f"\nFetching all-time tweet counts for {len(users_full_timeline)} full-timeline users …")
        semaphore = asyncio.Semaphore(CONCURRENCY)

        async with httpx.AsyncClient() as client:
            with tqdm(total=len(users_full_timeline), unit=" users") as pbar:
                tasks = [
                    fetch_screeninfo(client, semaphore, row["username"], pbar)
                    for row in users_full_timeline
                ]
                api_results = await asyncio.gather(*tasks)

        for api_data, row in zip(api_results, users_full_timeline):
            results.append({
                "username": row["username"],
                "has_archive": False,
                "archive_cutoff": "none",
                "statuses_count_alltime": api_data.get("statuses_count"),
                "followers_count": api_data.get("followers_count"),
                "display_name": api_data.get("display_name"),
                "api_error": api_data.get("error"),
            })

    # ── Write CSV ─────────────────────────────────────────────────────────────
    fieldnames = [
        "username", "has_archive", "archive_cutoff",
        # archive users
        "tweet_count_in_fresh", "min_date", "max_date",
        "days_covered", "rate_per_day", "days_since_cutoff", "estimated_total",
        # full-timeline users
        "statuses_count_alltime", "followers_count", "display_name",
        # shared
        "error", "api_error",
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for r in results:
            # rename tweet_count → tweet_count_in_fresh for clarity
            if "tweet_count" in r:
                r["tweet_count_in_fresh"] = r.pop("tweet_count")
            writer.writerow(r)

    print(f"\nResults written to {OUT_CSV}\n")

    # ── Print summary ─────────────────────────────────────────────────────────
    archive_rows = [r for r in results if r.get("has_archive")]
    full_rows    = [r for r in results if not r.get("has_archive")]

    valid_archive = [r for r in archive_rows if r.get("estimated_total") is not None]
    total_estimated_archive = sum(r["estimated_total"] for r in valid_archive)

    valid_full = [r for r in full_rows if r.get("statuses_count_alltime") is not None]
    total_alltime_full = sum(r["statuses_count_alltime"] for r in valid_full)

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"\nUsers WITH archive cutoff ({len(archive_rows)} users):")
    print(f"  Resolved from .jsonl : {len(valid_archive)}")
    errors = [r for r in archive_rows if r.get("error")]
    if errors:
        print(f"  Errors (no jsonl/empty): {len(errors)}")
    print(f"  Median rate/day      : {_median([r['rate_per_day'] for r in valid_archive if r.get('rate_per_day')]):.2f}")
    print(f"  Estimated total tweets (cutoff → today): {total_estimated_archive:,}")

    print(f"\nUsers WITHOUT archive ({len(full_rows)} users, full timeline):")
    print(f"  API results obtained : {len(valid_full)}")
    api_errors = [r for r in full_rows if r.get("api_error")]
    if api_errors:
        print(f"  API errors           : {len(api_errors)}")
    print(f"  Total all-time tweets: {total_alltime_full:,}")

    print(f"\nGrand total estimated tweets to scrape: {total_estimated_archive + total_alltime_full:,}")
    print()

    # Top 10 highest-volume archive users
    if valid_archive:
        print("Top 10 archive users by estimated tweets:")
        top10 = sorted(valid_archive, key=lambda r: r.get("estimated_total", 0), reverse=True)[:10]
        for r in top10:
            print(f"  {r['username']:<30} cutoff={r['archive_cutoff']}  "
                  f"rate={r.get('rate_per_day', 0):.1f}/day  "
                  f"est={r.get('estimated_total', 0):,}")

    # Top 10 highest-volume full-timeline users
    if valid_full:
        print("\nTop 10 full-timeline users by all-time tweet count:")
        top10f = sorted(valid_full, key=lambda r: r.get("statuses_count_alltime", 0), reverse=True)[:10]
        for r in top10f:
            print(f"  {r['username']:<30} all-time={r.get('statuses_count_alltime', 0):,}")


def _median(values: list[float]) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 else (s[mid - 1] + s[mid]) / 2


if __name__ == "__main__":
    asyncio.run(main())
