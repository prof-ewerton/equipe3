from services.sobrevivente_service import SobreviventeService 

class Ui:

    def __init__(self, sobrevivente_service: SobreviventeService):

        self.MENU_OPTIONS = [
            (1, "Sobreviventes", self.menu_entity_one),
        ]
        self.sobrevivente_service = sobrevivente_service

    def show(self):
        while True:
            print("\n===== Apocalipse Zumbi =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break
            if option == "1":
                self.menu_entity_one()

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== Apocalipse Zumbi =====")
        print("== Sobreviventes ==")
        
        print("(0) - Retornar ao menu principal")
        print("(1) - Registrar sobrevivente")
        
        option = input("\nEscolha uma opção: ")
        
        if option == "0":
            self.show()
        elif option == "1":
            try:
                name = input("Digite o nome do seu sobrevivente: ")
                age = input("Digite a idade do seu sobrevivente: ")
                infected = input("Seu sobrevivente está infectado?(s/n): ")
                skill = input("Qual a habilidade do seu sobrevivente?(forte/rapido/inteligente): ")
                self.sobrevivente_service.add_sobrevivente(name, age, infected, skill)
            except ValueError as e:
               print(e)
