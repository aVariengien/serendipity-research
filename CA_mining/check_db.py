# /// script
# requires-python = ">=3.11"
# dependencies = ["psycopg[binary]"]
# ///
"""Post-insert DB health checks for the Community Archive local instance.

Usage:
    uv run --env-file .env.local check_db.py
    uv run --env-file .env.local check_db.py --account 0xosprey
"""

import argparse
import os
import sys

import psycopg

POSTGRES_HOST     = os.environ.get("POSTGRES_HOST", "db.fabxmporizzqflnftavs.supabase.co")
POSTGRES_USER     = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_DB       = os.environ.get("POSTGRES_DB",   "postgres")
POSTGRES_PORT     = int(os.environ.get("POSTGRES_PORT", "5432"))
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")

# ── Helpers ───────────────────────────────────────────────────────────────────

def section(title: str) -> None:
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")


def ok(label: str) -> None:
    print(f"  ✓  {label}")


def fail(label: str) -> None:
    print(f"  ✗  {label}")


def check(label: str, cond: bool, detail: str = "") -> bool:
    if cond:
        ok(label)
    else:
        fail(label + (f"  → {detail}" if detail else ""))
    return cond


def table_row(label: str, value, width: int = 36) -> None:
    print(f"  {label:<{width}} {value}")


# ── Checks ────────────────────────────────────────────────────────────────────

def check_row_counts(cur: psycopg.Cursor) -> None:
    section("1. Row counts")
    tables = [
        "all_account",
        "all_profile",
        "account_refresh_log",
        "tweets",
        "tweet_media",
        "tweet_urls",
        "user_mentions",
        "conversations",
        "quote_tweets",
        "retweets",
    ]
    for tbl in tables:
        cur.execute(f"SELECT count(*) FROM {tbl}")  # noqa: S608 — internal script, no user input
        (n,) = cur.fetchone()
        table_row(tbl, f"{n:,}")


def check_refresh_log(cur: psycopg.Cursor) -> bool:
    section("2. account_refresh_log")
    passed = True

    cur.execute("SELECT count(*) FROM account_refresh_log WHERE started_at > completed_at")
    (bad,) = cur.fetchone()
    passed &= check("started_at ≤ completed_at for all rows", bad == 0,
                    f"{bad} rows where started_at > completed_at")

    cur.execute("""
        SELECT count(*) FROM all_account a
        LEFT JOIN account_refresh_log rl ON rl.account_id = a.account_id
        WHERE rl.account_id IS NULL
    """)
    (missing,) = cur.fetchone()
    cur.execute("SELECT count(*) FROM all_account")
    (total_accounts,) = cur.fetchone()
    pct = 100 * missing / total_accounts if total_accounts else 0
    check(
        f"accounts with no refresh_log entry: {missing}/{total_accounts} ({pct:.1f}%)",
        missing == 0 or pct < 20,
        "high % means many tweets had no updated_at field",
    )

    print()
    print("  Top 5 widest fetch windows:")
    cur.execute("""
        SELECT a.username, rl.started_at, rl.completed_at,
               rl.completed_at - rl.started_at AS duration
        FROM account_refresh_log rl
        JOIN all_account a USING (account_id)
        ORDER BY duration DESC NULLS LAST
        LIMIT 5
    """)
    rows = cur.fetchall()
    if rows:
        table_row("username", "started_at            completed_at          duration")
        for username, started, completed, duration in rows:
            table_row(username or "(no username)", f"{started}  {completed}  {duration}")
    else:
        print("  (no rows)")

    return passed


def check_fk_integrity(cur: psycopg.Cursor) -> bool:
    section("3. FK integrity")
    passed = True

    cur.execute("""
        SELECT count(*) FROM tweets t
        LEFT JOIN all_account a ON a.account_id = t.account_id
        WHERE a.account_id IS NULL
    """)
    (n,) = cur.fetchone()
    passed &= check("tweets → all_account: no orphans", n == 0, f"{n} orphan tweets")

    cur.execute("""
        SELECT count(*) FROM account_refresh_log r
        LEFT JOIN all_account a ON a.account_id = r.account_id
        WHERE a.account_id IS NULL
    """)
    (n,) = cur.fetchone()
    passed &= check("account_refresh_log → all_account: no orphans", n == 0, f"{n} orphans")

    cur.execute("""
        SELECT count(*) FROM tweet_media m
        LEFT JOIN tweets t ON t.tweet_id = m.tweet_id
        WHERE t.tweet_id IS NULL
    """)
    (n,) = cur.fetchone()
    passed &= check("tweet_media → tweets: no orphans", n == 0, f"{n} orphans")

    cur.execute("""
        SELECT count(*) FROM tweet_urls u
        LEFT JOIN tweets t ON t.tweet_id = u.tweet_id
        WHERE t.tweet_id IS NULL
    """)
    (n,) = cur.fetchone()
    passed &= check("tweet_urls → tweets: no orphans", n == 0, f"{n} orphans")

    cur.execute("""
        SELECT count(*) FROM user_mentions um
        LEFT JOIN tweets t ON t.tweet_id = um.tweet_id
        WHERE t.tweet_id IS NULL
    """)
    (n,) = cur.fetchone()
    passed &= check("user_mentions → tweets: no orphans", n == 0, f"{n} orphans")

    return passed


def check_duplicates(cur: psycopg.Cursor) -> bool:
    section("4. Duplicate check")
    passed = True

    cur.execute("""
        SELECT count(*) FROM (
            SELECT tweet_id FROM tweets GROUP BY tweet_id HAVING count(*) > 1
        ) dups
    """)
    (n,) = cur.fetchone()
    passed &= check("no duplicate tweet_ids", n == 0, f"{n} tweet_ids appear more than once")

    cur.execute("""
        SELECT count(*) FROM (
            SELECT account_id FROM all_account GROUP BY account_id HAVING count(*) > 1
        ) dups
    """)
    (n,) = cur.fetchone()
    passed &= check("no duplicate account_ids in all_account", n == 0, f"{n} duplicates")

    cur.execute("""
        SELECT count(*) FROM (
            SELECT account_id FROM account_refresh_log GROUP BY account_id HAVING count(*) > 1
        ) dups
    """)
    (n,) = cur.fetchone()
    passed &= check("no duplicate account_ids in account_refresh_log", n == 0, f"{n} duplicates")

    return passed


def check_account_spotlight(cur: psycopg.Cursor, username: str) -> None:
    section(f"5. Account spotlight — @{username}")

    cur.execute("""
        SELECT a.account_id, a.username, a.num_followers,
               rl.started_at, rl.completed_at,
               count(t.tweet_id) AS tweet_count
        FROM all_account a
        LEFT JOIN account_refresh_log rl USING (account_id)
        LEFT JOIN tweets t               USING (account_id)
        WHERE a.username = %s
        GROUP BY 1, 2, 3, 4, 5
    """, (username,))
    row = cur.fetchone()

    if not row:
        print(f"  ✗  @{username} not found in all_account")
        return

    account_id, uname, followers, started, completed, tweet_count = row
    table_row("account_id",   account_id)
    table_row("username",     uname)
    table_row("num_followers", f"{followers:,}" if followers else "—")
    table_row("tweet_count",  f"{tweet_count:,}")
    table_row("refresh started_at",   started   or "—")
    table_row("refresh completed_at", completed or "—")

    print()
    print("  Latest 5 tweets:")
    cur.execute("""
        SELECT tweet_id, created_at, left(full_text, 80) AS preview
        FROM tweets
        WHERE account_id = %s
        ORDER BY created_at DESC
        LIMIT 5
    """, (account_id,))
    for tweet_id, created_at, preview in cur.fetchall():
        print(f"    [{created_at}] {tweet_id}")
        print(f"      {preview!r}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Post-insert DB health checks.")
    parser.add_argument("--account", metavar="USERNAME",
                        help="Also run a per-account spotlight check")
    args = parser.parse_args()

    if not POSTGRES_PASSWORD:
        print("Error: POSTGRES_PASSWORD is required.")
        print("  uv run --env-file .env.local check_db.py")
        sys.exit(1)

    print(f"Connecting to {POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}...")
    with psycopg.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB,
    ) as conn:
        with conn.cursor() as cur:
            check_row_counts(cur)
            passed  = check_refresh_log(cur)
            passed &= check_fk_integrity(cur)
            passed &= check_duplicates(cur)
            if args.account:
                check_account_spotlight(cur, args.account)

    print()
    if passed:
        print("  All checks passed.")
    else:
        print("  Some checks FAILED — review output above.")
    print()


if __name__ == "__main__":
    main()
