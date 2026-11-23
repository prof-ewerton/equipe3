from entities.abrigo_entity import Abrigo
from database.abrigo_repository import abrigoRepository

class abrigoService:

    def __init__(self, repository):
        self.repository=repository

    def create(self, nome: str, capacidade: int, seguro: bool, localizacao: str) -> Abrigo:
        localicao_possivel = ["garanhuns", "londrina", "miami"]
        localicao_clean = localizacao.lower().strip()
        
        # Não tenho certeza se isso funciona
        if localicao_clean is not in localicao_possivel:
            raise ValueError("Essa localização não se encaixa entre as disponíveis")
        
        new_abrigo = (nome, capacidade, seguro, localizacao_clean)
        return self.repository.create(new_abrigo)