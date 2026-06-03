from __future__ import annotations

import getpass
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.db import initialize_database
from app.users import create_user, get_user_by_username


def main() -> None:
    initialize_database()

    username = input("Admin username: ").strip()
    if not username:
        raise SystemExit("Username is required.")

    existing_user = get_user_by_username(username)
    if existing_user:
        raise SystemExit(f"User '{username}' already exists.")

    full_name = input("Admin full name: ").strip()
    if not full_name:
        raise SystemExit("Full name is required.")

    password = getpass.getpass("Admin password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        raise SystemExit("Passwords do not match.")
    if len(password) < 8:
        raise SystemExit("Password must be at least 8 characters.")

    user_id = create_user(
        username=username,
        password=password,
        full_name=full_name,
        role="Administrator",
    )
    print(f"Created administrator user with id {user_id}.")


if __name__ == "__main__":
    main()
