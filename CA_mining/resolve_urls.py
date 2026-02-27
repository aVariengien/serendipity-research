# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "polars",
#   "pyarrow",
#   "tqdm",
# ]
# ///

# %% Imports & config
from __future__ import annotations

import argparse
import asyncio
import json
import re
from pathlib import Path
from urllib.parse import urlparse

import httpx
import polars as pl
from tqdm import tqdm

OUT_DIR = Path(__file__).parent / "outputs"
CACHE_FILE = OUT_DIR / "url_cache.json"

REDIRECT_CONCURRENCY = 30
JINA_CONCURRENCY = 8
JINA_EXCERPT_CHARS = 400
SAVE_EVERY = 200

IMAGE_HOSTS = {
    "pbs.twimg.com",
    "abs.twimg.com",
    "video.twimg.com",
    "ton.twimg.com",
    "t.co",  # sometimes resolves back to t.co for media
}
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".mp4", ".mov", ".avi", ".svg"}


# %% Helpers

def classify_url(url: str) -> str:
    try:
        parsed = urlparse(url)
        hostname = (parsed.hostname or "").lower()
        if hostname in IMAGE_HOSTS:
            return "image"
        ext = Path(parsed.path).suffix.lower()
        if ext in IMAGE_EXTENSIONS:
            return "image"
        # Twitter/X pic redirects
        if "twimg.com" in hostname:
            return "image"
    except Exception:
        pass
    return "link"


async def resolve_tco(client: httpx.AsyncClient, tco_url: str) -> str | None:
    """Follow t.co redirect chain to get the final URL."""
    try:
        r = await client.head(tco_url, follow_redirects=True, timeout=10.0)
        final = str(r.url)
        # HEAD sometimes doesn't follow all redirects; verify it's not still t.co
        if "t.co" in final and final != tco_url:
            return final
        return final
    except Exception:
        # Fallback to GET
        try:
            r = await client.get(
                tco_url,
                follow_redirects=True,
                timeout=10.0,
                headers={"User-Agent": "Mozilla/5.0"},
            )
            return str(r.url)
        except Exception:
            return None


def parse_jina_response(text: str) -> dict[str, str]:
    """Extract title and first meaningful content from Jina Reader markdown output."""
    title = ""
    excerpt_parts: list[str] = []

    meta_prefixes = (
        "Title:", "URL:", "Published", "Description:", "Warning:",
        "Error:", "X-Frame-Options", "Strict-Transport", "===", "---",
    )

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("Title:"):
            title = stripped[6:].strip()
        elif not any(stripped.startswith(p) for p in meta_prefixes):
            # Skip markdown headings (# H1, ## H2 …) but keep their text
            if stripped.startswith("#"):
                stripped = stripped.lstrip("#").strip()
            excerpt_parts.append(stripped)
            if sum(len(s) for s in excerpt_parts) >= JINA_EXCERPT_CHARS:
                break

    excerpt = " ".join(excerpt_parts).strip()[:JINA_EXCERPT_CHARS]
    return {"title": title, "excerpt": excerpt}


async def fetch_jina_excerpt(client: httpx.AsyncClient, url: str) -> dict[str, str]:
    try:
        r = await client.get(
            f"https://r.jina.ai/{url}",
            timeout=30.0,
            headers={"Accept": "text/plain"},
        )
        if r.status_code == 200:
            return parse_jina_response(r.text)
    except Exception:
        pass
    return {"title": "", "excerpt": ""}


# %% Main

async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resolve t.co URLs and optionally fetch Jina excerpts for link previews."
    )
    parser.add_argument(
        "--skip-jina",
        action="store_true",
        help="Only resolve t.co redirects; skip Jina excerpt fetching.",
    )
    args = parser.parse_args()

    # ── Load existing cache ────────────────────────────────────────────────────
    cache: dict[str, dict] = {}
    if CACHE_FILE.exists():
        cache = json.loads(CACHE_FILE.read_text())
    print(f"Loaded {len(cache):,} cached URL entries from {CACHE_FILE.name}")

    # ── Extract all t.co URLs ──────────────────────────────────────────────────
    print("\nLoading parquet files …")
    df_main = pl.read_parquet(OUT_DIR / "tweets_2months.parquet")
    df_ctx = pl.read_parquet(OUT_DIR / "context_tweets.parquet")

    all_tco: set[str] = set()
    for df in [df_main, df_ctx]:
        if df.is_empty():
            continue
        for row in df.to_dicts():
            text = row.get("full_text") or ""
            all_tco.update(re.findall(r"https://t\.co/\w+", text))

    to_resolve = sorted(all_tco - set(cache))

    print(f"Total unique t.co URLs : {len(all_tco):,}")
    print(f"Already cached         : {len(cache):,}")
    print(f"To resolve now         : {len(to_resolve):,}")

    # ── Phase 1: Resolve t.co redirects ───────────────────────────────────────
    if to_resolve:
        print(f"\n[Phase 1] Resolving {len(to_resolve):,} t.co redirects "
              f"(concurrency={REDIRECT_CONCURRENCY}) …")

        sem = asyncio.Semaphore(REDIRECT_CONCURRENCY)
        save_counter = 0

        async def resolve_one(client: httpx.AsyncClient, tco: str) -> None:
            nonlocal save_counter
            async with sem:
                resolved = await resolve_tco(client, tco)
                url_type = classify_url(resolved) if resolved else "unknown"
                cache[tco] = {"resolved": resolved, "type": url_type}
                save_counter += 1
                if save_counter % SAVE_EVERY == 0:
                    CACHE_FILE.write_text(json.dumps(cache))

        async with httpx.AsyncClient() as client:
            tasks = [resolve_one(client, tco) for tco in to_resolve]
            pbar = tqdm(
                asyncio.as_completed(tasks),
                total=len(tasks),
                desc="Resolving redirects",
                unit=" URLs",
                dynamic_ncols=True,
            )
            for coro in pbar:
                await coro

        CACHE_FILE.write_text(json.dumps(cache))
        img_count = sum(1 for d in cache.values() if d.get("type") == "image")
        lnk_count = sum(1 for d in cache.values() if d.get("type") == "link")
        print(f"  → Done. {img_count:,} images, {lnk_count:,} links, "
              f"{len(cache) - img_count - lnk_count:,} unknown")
    else:
        print("\nAll t.co URLs already resolved — skipping Phase 1")

    # ── Phase 2: Jina excerpts ─────────────────────────────────────────────────
    if args.skip_jina:
        print("\n--skip-jina set → skipping Jina excerpt fetching")
        print(f"\nCache saved to {CACHE_FILE}")
        return

    link_entries = [
        (tco, data)
        for tco, data in cache.items()
        if data.get("type") == "link"
        and data.get("resolved")
        and "title" not in data  # not yet enriched
    ]

    print(f"\n[Phase 2] Fetching Jina excerpts for {len(link_entries):,} link URLs "
          f"(concurrency={JINA_CONCURRENCY}) …")
    print("  (Tip: Ctrl+C to stop — progress is saved incrementally)")

    if not link_entries:
        print("  All links already enriched — nothing to do")
    else:
        sem = asyncio.Semaphore(JINA_CONCURRENCY)
        save_counter = 0

        async def enrich_one(client: httpx.AsyncClient, tco: str, resolved: str) -> None:
            nonlocal save_counter
            async with sem:
                result = await fetch_jina_excerpt(client, resolved)
                cache[tco].update(result)
                save_counter += 1
                if save_counter % SAVE_EVERY == 0:
                    CACHE_FILE.write_text(json.dumps(cache))

        async with httpx.AsyncClient() as client:
            tasks = [enrich_one(client, tco, data["resolved"]) for tco, data in link_entries]
            pbar = tqdm(
                asyncio.as_completed(tasks),
                total=len(tasks),
                desc="Jina excerpts",
                unit=" URLs",
                dynamic_ncols=True,
            )
            for coro in pbar:
                await coro

        CACHE_FILE.write_text(json.dumps(cache))
        enriched = sum(
            1 for d in cache.values()
            if d.get("type") == "link" and d.get("title") is not None
        )
        print(f"  → Done. {enriched:,} links enriched with title/excerpt")

    print(f"\nCache saved to {CACHE_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
