from database.sobrevivente_repository import SobreviventeRepository

class SobreviventeService:
    def __init__(self, repository: SobreviventeRepository):
        self.repository = repository
        
    def add_sobrevivente(self, name, age, infected, skill):
        skill_cat = ["forte", "inteligente", "rapido"]
        infected_vals = ["s", "n"]
        
        if name.strip() == "":
            raise ValueError("O nome do sobrevivente não pode ser vazio")
        if not age.isdigit():
            raise ValueError("A idade deve ser um número")
        if int(age) < 0:
            raise ValueError("A idade do sobrevivente não pode ser negativa")
        if not infected.lower() in infected_vals:
            raise ValueError("Infectado só pode receber s ou n como valor")
        if not skill in skill_cat:
            raise ValueError("A categoria da habilidade não é valida")
        
        infec_bool = True if infected.lower() == "s" else False
        
        self.repository.create_sobrevivente(
            name=name,
            age=int(age),
            infected=infec_bool,
            skill=skill
        )
        
        