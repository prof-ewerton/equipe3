
from database.connection import get_db_connection
from contextlib import closing


def install():
    with closing(get_db_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produto (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                infected BOOLEAN,
                skill TEXT
            );
        """)

        cursor.execute("""
            INSERT INTO produto (name, age, infected, skill)
            VALUES
                ('Marcos', 23, 0, 'rapido'),
                ('Julia', 53, 0, 'forte'),
                ('Murilo', 27, 0, 'inteligente'),
                ('Mateus', 29, 1, 'forte'),
                ('João', 34, 0, 'inteligente');
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS abrigo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                capacidade INTEGER,
                seguro BOOLEAN,
                localizacao TEXT
            );
        """)

        cursor.execute("""
            INSERT INTO abrigo (nome, capacidade, seguro, localizacao)
            VALUES
                ('Abrigo do Norte', 50, 0, 'miami'),
                ('Abrigo do Sul', 100, 0, 'miami'),
                ('Abrigo do Leste', 70, 0, 'londrina'),
                ('Abrigo do Oeste', 30, 1, 'garanhuns'),
                ('Abrigo do Noroeste', 80, 0, 'londrina');
        """)

        conn.commit()
