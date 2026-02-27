# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "polars",
#   "pyarrow",
#   "tqdm",
# ]
# ///

# %% Config & imports
import asyncio
import json
from pathlib import Path

import httpx
import polars as pl
from tqdm import tqdm

SUPABASE_URL = "https://fabxmporizzqflnftavs.supabase.co/rest/v1"
ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
    ".eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZhYnhtcG9yaXp6cWZsbmZ0YXZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjIyNDQ5MTIsImV4cCI6MjAzNzgyMDkxMn0"
    ".UIEJiUNkLsW28tBHmG-RQDW-I5JNlJLt62CSk9D_qG8"
)
HEADERS = {
    "apikey": ANON_KEY,
    "Authorization": f"Bearer {ANON_KEY}",
}

# 2 months back from Feb 26, 2026
CUTOFF = "2025-12-26T00:00:00Z"
PAGE_SIZE = 1000
OUT_DIR = Path(__file__).parent / "outputs"
OUT_DIR.mkdir(exist_ok=True)


# %% Helpers
async def fetch_page(
    client: httpx.AsyncClient,
    table: str,
    params: dict,
    offset: int,
) -> list[dict]:
    """Fetch a single page of results."""
    response = await client.get(
        f"{SUPABASE_URL}/{table}",
        params={**params, "offset": offset, "limit": PAGE_SIZE},
        headers=HEADERS,
        timeout=60.0,
    )
    response.raise_for_status()
    return response.json()


async def fetch_all_pages(
    client: httpx.AsyncClient,
    table: str,
    params: dict,
    desc: str,
) -> list[dict]:
    """Paginate through all results with a progress bar."""
    all_rows = []
    offset = 0
    pbar = tqdm(desc=desc, unit=" rows", dynamic_ncols=True)
    while True:
        rows = await fetch_page(client, table, params, offset)
        if not rows:
            break
        all_rows.extend(rows)
        pbar.update(len(rows))
        if len(rows) < PAGE_SIZE:
            break
        offset += PAGE_SIZE
    pbar.close()
    return all_rows


async def fetch_tweets_by_ids_batched(
    client: httpx.AsyncClient,
    tweet_ids: list[str],
    batch_size: int = 100,
) -> list[dict]:
    """Fetch tweets by a list of IDs in batches (PostgREST `in` filter)."""
    results = []
    pbar = tqdm(
        total=len(tweet_ids),
        desc="Fetching context tweets",
        unit=" tweets",
        dynamic_ncols=True,
    )
    for i in range(0, len(tweet_ids), batch_size):
        batch = tweet_ids[i : i + batch_size]
        ids_str = "(" + ",".join(batch) + ")"
        rows = await fetch_page(
            client,
            "enriched_tweets",
            {"tweet_id": f"in.{ids_str}", "select": "*"},
            offset=0,
        )
        results.extend(rows)
        pbar.update(len(batch))
    pbar.close()
    return results


async def fetch_member_tweets_batched(
    client: httpx.AsyncClient,
    account_ids: list[str],
    cutoff: str,
    batch_size: int = 20,
) -> list[dict]:
    """Fetch recent tweets for all archive members, batching by account_id."""
    all_rows: list[dict] = []
    pbar = tqdm(
        total=len(account_ids),
        desc="Accounts fetched",
        unit=" accounts",
        dynamic_ncols=True,
    )
    for i in range(0, len(account_ids), batch_size):
        batch = account_ids[i : i + batch_size]
        ids_str = "(" + ",".join(batch) + ")"
        rows = await fetch_all_pages(
            client,
            table="enriched_tweets",
            params={
                "account_id": f"in.{ids_str}",
                "created_at": f"gte.{cutoff}",
                "order": "created_at.asc",
                "select": "*",
            },
            desc=f"  batch {i // batch_size + 1}",
        )
        all_rows.extend(rows)
        pbar.update(len(batch))
    pbar.close()
    return all_rows


# %% Main
async def main():
    async with httpx.AsyncClient() as client:

        # ── Step 0: fetch all archive member account IDs ─────────────────────
        print("\n[0/3] Fetching archive member account IDs …")
        accounts = await fetch_all_pages(
            client,
            table="account",
            params={"select": "account_id,username"},
            desc="Accounts",
        )
        account_ids = [a["account_id"] for a in accounts]
        print(f"    → {len(account_ids):,} archive members found")

        # ── Step 1: fetch tweets for those members from last 2 months ────────
        print(f"\n[1/3] Downloading tweets for {len(account_ids)} members since {CUTOFF} …")
        main_tweets = await fetch_member_tweets_batched(
            client,
            account_ids=account_ids,
            cutoff=CUTOFF,
        )
        print(f"    → {len(main_tweets):,} tweets downloaded")

        if not main_tweets:
            print("No tweets found in this date range — exiting.")
            return

        df_main = pl.DataFrame(main_tweets)
        df_main.write_parquet(OUT_DIR / "tweets_2months.parquet")
        print(f"    → Saved to {OUT_DIR / 'tweets_2months.parquet'}")

        # ── Step 2: collect referenced tweet IDs (parents + quoted) ─────────
        print("\n[2/3] Collecting referenced tweet IDs for context …")
        main_ids = set(df_main["tweet_id"].to_list())

        referenced_ids: set[str] = set()

        # Parent tweets (the tweet this is a reply to)
        if "reply_to_tweet_id" in df_main.columns:
            parents = (
                df_main
                .filter(pl.col("reply_to_tweet_id").is_not_null())
                ["reply_to_tweet_id"]
                .to_list()
            )
            referenced_ids.update(str(x) for x in parents)

        # Quoted tweets
        if "quoted_tweet_id" in df_main.columns:
            quotes = (
                df_main
                .filter(pl.col("quoted_tweet_id").is_not_null())
                ["quoted_tweet_id"]
                .to_list()
            )
            referenced_ids.update(str(x) for x in quotes)

        # Only fetch ones not already in our main set
        to_fetch = sorted(referenced_ids - main_ids)
        print(f"    → {len(to_fetch):,} unique referenced tweet IDs to look up")

        # ── Step 3: fetch context tweets ─────────────────────────────────────
        print("\n[3/3] Fetching context tweets from DB …")
        if to_fetch:
            context_rows = await fetch_tweets_by_ids_batched(client, to_fetch)
            print(f"    → {len(context_rows):,} context tweets found in DB")
            df_context = pl.DataFrame(context_rows)
        else:
            print("    → No referenced tweets to fetch")
            df_context = pl.DataFrame()

        df_context.write_parquet(OUT_DIR / "context_tweets.parquet")
        print(f"    → Saved to {OUT_DIR / 'context_tweets.parquet'}")

    # ── Summary ───────────────────────────────────────────────────────────────
    print("\n=== Done ===")
    print(f"  tweets_2months.parquet : {len(df_main):,} rows")
    print(f"  context_tweets.parquet : {len(df_context):,} rows")
    print(f"\nColumn schema (main tweets):")
    for col, dtype in zip(df_main.columns, df_main.dtypes):
        print(f"  {col:<30} {dtype}")


if __name__ == "__main__":
    asyncio.run(main())
