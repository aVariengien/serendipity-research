# /// script
# requires-python = ">=3.11"
# dependencies = ["psycopg[binary]"]
# ///
"""Create the account_refresh_log table in the local (or remote) Supabase DB.

Usage:
    uv run --env-file .env.local migrate_add_refresh_log.py
    uv run --env-file .env.prod  migrate_add_refresh_log.py
"""

import os
import sys

import psycopg

POSTGRES_HOST     = os.environ.get("POSTGRES_HOST", "db.fabxmporizzqflnftavs.supabase.co")
POSTGRES_USER     = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_DB       = os.environ.get("POSTGRES_DB",   "postgres")
POSTGRES_PORT     = int(os.environ.get("POSTGRES_PORT", "5432"))
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")

CREATE_SQL = """
CREATE TABLE IF NOT EXISTS account_refresh_log (
    id           bigint      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_id   text        NOT NULL,
    started_at   timestamptz NOT NULL,
    completed_at timestamptz NOT NULL,
    CONSTRAINT account_refresh_log_account_id_fkey
        FOREIGN KEY (account_id) REFERENCES all_account(account_id),
    CONSTRAINT account_refresh_log_account_id_key
        UNIQUE (account_id)
);
"""

COMMENT_SQL = """
COMMENT ON TABLE account_refresh_log IS
  'Tracks the time window of each tweet-fetch run per account.
   started_at  = earliest fetched_at/updated_at seen across all tweets for this account.
   completed_at = latest  fetched_at/updated_at seen across all tweets for this account.
   Upserted on each insert run via LEAST/GREATEST so the window only ever widens.';
"""

# Block access from the Supabase REST API (anon + authenticated roles).
# The table is only accessible via direct Postgres connection (used by our scripts).
REVOKE_SQL = """
REVOKE ALL ON TABLE account_refresh_log FROM anon, authenticated;
"""


def main() -> None:
    if not POSTGRES_PASSWORD:
        print("Error: POSTGRES_PASSWORD is required.")
        print("  uv run --env-file .env.local migrate_add_refresh_log.py")
        sys.exit(1)

    print(f"Connecting to {POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB} as {POSTGRES_USER}...")
    with psycopg.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DB,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_SQL)
            cur.execute(COMMENT_SQL)
            cur.execute(REVOKE_SQL)
        conn.commit()

    print("✓  account_refresh_log created (or already existed) — REST API access revoked.")
    print()
    print("Columns:")
    print("  id           bigint  GENERATED ALWAYS AS IDENTITY  PK")
    print("  account_id   text    NOT NULL  UNIQUE  FK → all_account.account_id")
    print("  started_at   timestamptz  NOT NULL")
    print("  completed_at timestamptz  NOT NULL")


if __name__ == "__main__":
    main()
