# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "tqdm",
# ]
# ///

import asyncio
import httpx
from tqdm.asyncio import tqdm
from pathlib import Path

USERS_FILE = Path(__file__).parent / "outputs" / "ca_users.txt"
OUTPUT_FILE = Path(__file__).parent / "outputs" / "alive_accounts.txt"
DEAD_OUTPUT_FILE = Path(__file__).parent / "outputs" / "dead_accounts.txt"

CONCURRENCY = 20
TIMEOUT = 10


async def check_user(client: httpx.AsyncClient, username: str) -> tuple[str, bool]:
    url = f"https://publish.twitter.com/oembed?url=https://twitter.com/{username}"
    try:
        resp = await client.get(url, timeout=TIMEOUT)
        return username, resp.status_code == 200
    except Exception:
        return username, False


async def main():
    usernames = [u.strip() for u in USERS_FILE.read_text().splitlines() if u.strip()]
    print(f"Checking {len(usernames)} accounts with concurrency={CONCURRENCY}...")

    results = []
    sem = asyncio.Semaphore(CONCURRENCY)

    async def bounded_check(client, username):
        async with sem:
            return await check_user(client, username)

    async with httpx.AsyncClient(follow_redirects=True) as client:
        tasks = [bounded_check(client, u) for u in usernames]
        for coro in tqdm.as_completed(tasks, total=len(tasks), desc="Checking accounts"):
            result = await coro
            results.append(result)

    alive = sorted(u for u, ok in results if ok)
    dead = sorted(u for u, ok in results if not ok)

    OUTPUT_FILE.write_text("\n".join(alive) + "\n")
    DEAD_OUTPUT_FILE.write_text("\n".join(dead) + "\n")

    print(f"\nAlive: {len(alive)} | Dead/suspended: {len(dead)}")
    if dead:
        print("\nDead/suspended accounts:")
        for u in dead:
            print(f"  {u}")
    print(f"\nResults saved to:\n  {OUTPUT_FILE}\n  {DEAD_OUTPUT_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
