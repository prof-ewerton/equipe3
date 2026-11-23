import sqlite3
from database.connection import get_db_connection
from contextlib import closing


def install():
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS produto (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    infected BOOLEAN,
                    skill TEXT
                );
            """)
