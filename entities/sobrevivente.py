class Sobrevivente:
    def __init__(
            self,
            name:str,
            age:int,
            infected:bool,
            skill:str
        ) -> None:
        self.name = name
        self.age = age
        self.infected = infected
        self.skill = skill