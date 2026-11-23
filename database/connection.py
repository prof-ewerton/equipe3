from pathlib import Path
import sqlite3

DATABASE_PATH = Path(__file__).resolve().parent / "database.db"

def get_db_connection():
    return sqlite3.connect(DATABASE_PATH)
