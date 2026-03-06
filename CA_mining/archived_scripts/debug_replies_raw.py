# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///

# Dumps the raw paginated output of replies.php for a single user.
# Usage: uv run debug_replies_raw.py <username>

import asyncio
import json
import os
import sys
from pathlib import Path

import httpx

RAPID_API_KEY = os.environ["RAPID_API_KEY"]
HEADERS = {
    "x-rapidapi-host": "twitter-api45.p.rapidapi.com",
    "x-rapidapi-key": RAPID_API_KEY,
}
URL = "https://twitter-api45.p.rapidapi.com/replies.php"


async def main(username: str) -> None:
    all_tweets: list[dict] = []
    cursor: str | None = None
    page_num = 0

    async with httpx.AsyncClient() as client:
        while True:
            page_num += 1
            params: dict[str, str] = {"screenname": username}
            if cursor:
                params["cursor"] = cursor

            resp = await client.get(URL, params=params, headers=HEADERS, timeout=30.0)
            resp.raise_for_status()
            data = resp.json()

            tweets = data.get("timeline", [])
            print(f"Page {page_num}: {len(tweets)} tweets  (cursor: {(cursor or 'none')[:40]})")
            for t in tweets:
                author = (t.get("author") or {}).get("screen_name", "?")
                marker = ">>>" if author.lower() == username.lower() else "   "
                print(f"  {marker} {author:<28} {t['created_at'][:16]}  {t['text'][:70]}")

            all_tweets.extend(tweets)

            next_cursor = data.get("next_cursor")
            if not next_cursor or next_cursor == cursor:
                print("\nNo more pages.")
                break
            cursor = next_cursor

    out_file = Path(__file__).parent / "outputs" / f"debug_replies_{username}.jsonl"
    with out_file.open("w", encoding="utf-8") as f:
        for tweet in all_tweets:
            f.write(json.dumps(tweet, ensure_ascii=False) + "\n")

    user_tweets = [
        t for t in all_tweets
        if (t.get("author") or {}).get("screen_name", "").lower() == username.lower()
    ]
    print(f"\nTotal tweets on feed : {len(all_tweets)}")
    print(f"By {username}         : {len(user_tweets)}")
    print(f"Context (others)     : {len(all_tweets) - len(user_tweets)}")
    print(f"Saved to             : {out_file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: uv run {Path(__file__).name} <username>")
        sys.exit(1)
    asyncio.run(main(sys.argv[1]))
