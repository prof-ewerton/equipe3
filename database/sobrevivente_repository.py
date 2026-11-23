from .connection import get_db_connection
from contextlib import closing

class SobreviventeRepository:
    def create_sobrevivente(self, name, age, infected, skill):
        with closing(get_db_connection()) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO produto (name, age, infected, skill)
                VALUES (?, ?, ?, ?);
            """, (name, age, infected, skill)
            )
            
            conn.commit()
