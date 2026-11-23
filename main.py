from interface.ui import Ui
from database.sobrevivente_repository import SobreviventeRepository
from services.sobrevivente_service import SobreviventeService
from database.abrigo_repository import abrigoRepository
from services.abrigo_service import abrigoService
from install import install

def main():
    sobrevivente_repository = SobreviventeRepository()
    sobrevivente_service = SobreviventeService(sobrevivente_repository)
    
    abrigo_repository = AbrigoRepository()
    abrigo_service = AbrigoService(abrigo_repository)
    ui = Ui(sobrevivente_service,abrigo_service)
    ui.show()

if __name__ == "__main__":
    install()
    main()