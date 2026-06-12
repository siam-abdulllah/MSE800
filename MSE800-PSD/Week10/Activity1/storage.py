"""Save and load user accounts from a SQLite database."""

import sqlite3
from datetime import date
from pathlib import Path
from typing import Dict, Optional

DB_PATH = Path(__file__).parent / "users.db"

_USERS_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL
    )
"""


def init_db() -> None:
    """Create users.db on first run (called once when the app starts)."""
    created = not DB_PATH.exists()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(_USERS_TABLE_SQL)
    if created:
        print(f"Database not found. Created automatically at {DB_PATH}")


def create_database() -> None:
    """Create the database file and users table."""
    init_db()
    print(f"Database ready at {DB_PATH}")


def username_exists(username: str) -> bool:
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT 1 FROM users WHERE username = ? COLLATE NOCASE", (username,)
        ).fetchone()
    return row is not None


def email_exists(email: str) -> bool:
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute(
            "SELECT 1 FROM users WHERE email = ? COLLATE NOCASE", (email.lower(),)
        ).fetchone()
    return row is not None


def create_user(username: str, email: str, password_hash: str, full_name: str, dob: date) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO users (username, email, password_hash, full_name, date_of_birth)
            VALUES (?, ?, ?, ?, ?)
            """,
            (username, email.lower(), password_hash, full_name, dob.isoformat()),
        )


def get_user_by_username(username: str) -> Optional[Dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM users WHERE username = ? COLLATE NOCASE", (username,)
        ).fetchone()
    return dict(row) if row else None


def get_user_by_email(email: str) -> Optional[Dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM users WHERE email = ? COLLATE NOCASE", (email.lower(),)
        ).fetchone()
    return dict(row) if row else None


def update_user(user_id: int, full_name: str, dob: date, email: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            UPDATE users SET full_name = ?, date_of_birth = ?, email = ?
            WHERE id = ?
            """,
            (full_name, dob.isoformat(), email.lower(), user_id),
        )


def update_password(user_id: int, password_hash: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "UPDATE users SET password_hash = ? WHERE id = ?",
            (password_hash, user_id),
        )


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "create":
        create_database()
    else:
        print("Usage: python storage.py create")
