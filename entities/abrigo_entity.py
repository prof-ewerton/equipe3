class Abrigo:

    def __init__(
        self, nome: str, capacidade: int, seguro: bool, localizacao: str, id=None
    ):
        self.nome = nome
        self.capacidade = capacidade
        self.seguro = seguro
        self.localizacao = localizacao
        self.id = id
