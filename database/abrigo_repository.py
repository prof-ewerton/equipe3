from database.connection import get_db_connection
from entities.abrigo_entity import Abrigo

class abrigoRepository:

    def create(self, nome, capacidade, seguro, localizacao) -> Abrigo:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO abrigos (nome, capacidade, seguro, localizacao) VALUES (?,?,?,?)"
        valores = (nome, capacidade,seguro,localizacao)
        cursor.execute(sql, valores)
        conn.commit()
        abrigo.id = cursor.lastrowid
        conn.close()
        return abrigo