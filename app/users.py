from __future__ import annotations

from typing import Any

from app.db import get_connection
from app.security import hash_password, verify_password


def get_user_by_username(username: str) -> dict[str, Any] | None:
    with get_connection() as conn:
        return conn.execute(
            """
            SELECT id, username, password_hash, full_name, role, is_active
            FROM users
            WHERE username = %s
            """,
            (username,),
        ).fetchone()


def authenticate_user(username: str, password: str) -> dict[str, Any] | None:
    user = get_user_by_username(username.strip())
    if not user or not user["is_active"]:
        return None
    if not verify_password(password, user["password_hash"]):
        return None

    return {
        "id": user["id"],
        "username": user["username"],
        "full_name": user["full_name"],
        "role": user["role"],
    }


def create_user(
    username: str,
    password: str,
    full_name: str,
    role: str,
    is_active: bool = True,
) -> int:
    with get_connection() as conn:
        row = conn.execute(
            """
            INSERT INTO users (username, password_hash, full_name, role, is_active)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
            """,
            (username.strip(), hash_password(password), full_name.strip(), role, is_active),
        ).fetchone()
    return int(row["id"])


def count_users() -> int:
    with get_connection() as conn:
        row = conn.execute("SELECT COUNT(*) AS total FROM users").fetchone()
    return int(row["total"])

