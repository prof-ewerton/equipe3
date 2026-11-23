from entities.abrigo_entity import Abrigo
from database.abrigo_repository import abrigoRepository

class abrigoService:

    def __init__(self):
        self.repository= abrigoRepository()

    def add_abrigo(self, nome: str, capacidade: int, seguro: bool, localizacao: str) -> Abrigo:
        localicao_possivel = ["garanhuns", "londrina", "miami"]
        opcoes_possiveis = ["s", "n"]
        localizacao_clean = localizacao.lower().strip()
        
        # Não tenho certeza se isso funciona
        if localizacao_clean not in localicao_possivel:
            raise ValueError("Essa localização não se encaixa entre as disponíveis")
        if not seguro.lower() in opcoes_possiveis:
            raise ValueError("A seguridade só pode receber s ou n como valor")
        seguro_bool = True if seguro.lower() == "s" else False
        
        self.repository.create(
            nome,
            capacidade,
            seguro_bool,
            localizacao_clean
        )
        
