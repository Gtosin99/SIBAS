from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

import psycopg
from psycopg.rows import dict_row

from app.config import DATABASE_URL


class DatabaseConfigError(RuntimeError):
    """Raised when the database connection is not configured."""


def _require_database_url() -> str:
    if not DATABASE_URL:
        raise DatabaseConfigError(
            "DATABASE_URL is not set. Copy .env.example to .env and update it."
        )
    return DATABASE_URL


@contextmanager
def get_connection() -> Iterator[psycopg.Connection]:
    conn = psycopg.connect(_require_database_url(), row_factory=dict_row)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def initialize_database() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(80) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                full_name VARCHAR(160) NOT NULL,
                role VARCHAR(20) NOT NULL CHECK (role IN ('Administrator', 'Lecturer', 'Student')),
                is_active BOOLEAN NOT NULL DEFAULT TRUE,
                created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
            """
        )

