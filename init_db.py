import sqlite3
from pathlib import Path

DB_PATH = "users.db"

def init_db():
    db_exists = Path(DB_PATH).exists()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if not db_exists:
        print("Initializing database...")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
        """)

        conn.commit()
        print("Database initialized.")

    conn.close()
