from entities.abrigo_entity import Abrigo
from database.abrigo_repository import abrigoRepository

class abrigoService:

    def __init__(self, repository):
        self.repository=repository

    def add_abrigo(self, nome: str, capacidade: int, seguro: bool, localizacao: str) -> Abrigo:
        localicao_possivel = ["garanhuns", "londrina", "miami"]
        opcoes_possiveis = ["s", "n"]
        localicao_clean = localizacao.lower().strip()
        
        # Não tenho certeza se isso funciona
        if localicao_clean not in localicao_possivel:
            raise ValueError("Essa localização não se encaixa entre as disponíveis")
        if not seguro.lower() in opcoes_possiveis:
            raise ValueError("A seguridade só pode receber s ou n como valor")
        seguro_bool = True if seguro.lower() == "s" else False
        
        self.repository.create(
            nome=nome,
            capacidade=int(capacidade),
            seguro=seguro_bool,
            localizacao=localizacao
        )
        
