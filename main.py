from interface.ui import Ui
from database.sobrevivente_repository import SobreviventeRepository
from services.sobrevivente_service import SobreviventeService
from install import install

def main():
    sobrevivente_repository = SobreviventeRepository()
    sobrevivente_service = SobreviventeService(sobrevivente_repository)
    
    #ui = Ui(sobrevivente_service)
    ui = Ui()
    ui.show()

if __name__ == "__main__":
    install()
    main()