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
            
            INSERT INTO produto (name, age, infected, skill)
            VALUES
                ('Marcos', 23, 0, 'rapido'),
                ('Julia', 53, 0, 'forte'),
                ('Murilo', 27, 0, 'inteligente'),
                ('Mateus', 29, 1, 'forte'),
                ('João', 34, 0, 'inteligente');
            
        """)
        
        conn.commit()
