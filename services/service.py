from entities.abrigo_entity import Abrigo
from database.abrigo_repository import abrigoRepository

class abrigoService:

    def __init__(self, repository):
        self.repository=repository

    def create(self, nome: str, capacidade: int, seguro: bool, localizacao: str) -> Abrigo:
        new_abrigo = (nome, capacidade, seguro, localizacao)
        return self.repository.create(new_abrigo)