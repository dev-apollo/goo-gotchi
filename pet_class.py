import asyncio
from datetime import datetime

class Pet:
    # Método de criação do Objeto quando a classe é instanciada
    def __init__(self, owner, name, birthday, happiness=100, health=100, food=100, last_record=datetime.today().strftime("%d-%m-%Y %H:%M:%S"), start_time=datetime.now()):
        self.name = name
        self.owner = owner
        self.birthday = birthday
        self.happiness = happiness
        self.health = health
        self.food = food
        self.last_record = last_record
        self.start_time = start_time

    # Método assíncrono que verifica o tempo passado para então descontar dos Status
    async def updateInGameStatus(self):
        last_happiness_check = 0
        last_food_check = 0
        last_health_check = 0
        while(True):
            time_passed = ((datetime.now() - self.start_time).total_seconds()) / 60
            if(int(time_passed) >= 5 and int(time_passed) % 5 == 0 and int(time_passed) != last_happiness_check):
                self.happiness = max(self.happiness-1, 0)
                last_happiness_check = int(time_passed)
            if(int(time_passed) >= 10 and int(time_passed) % 10 == 0 and int(time_passed) != last_food_check):
                self.food = max(self.food-1, 0)
                last_food_check = int(time_passed)
            if(int(time_passed) >= 15 and int(time_passed) % 15 == 0 and int(time_passed) != last_health_check):
                self.health = max(self.health-1, 0)
                last_health_check = int(time_passed)
            print(f"{self.name} - Felicidade: {self.happiness} | Fome: {self.food} | Saúde: {self.health}")
            self.last_record = datetime.today().strftime("%d-%m-%Y %H:%M:%S")
            await asyncio.sleep(300)

    # Método de escrita das informações atuais do Pet no arquivo
    def writeInfos(self):
        with open("./pet_infos.txt", "w") as pet_infos:
            pet_infos.write(f"{self.owner}, {self.name}, {self.birthday}, {self.happiness}, {self.health}, {self.food}, {self.last_record}")

    # Método que pega as informações atuais do Pet e retorna um Objeto da própria Classe
    @classmethod
    def getInfos(cls):
        with open("./pet_infos.txt", "r") as pet_infos:
            infos = pet_infos.readline().strip().split(", ")
            owner, name, birthday, happiness, health, food, last_record = infos
            return cls(owner=owner, name=name, birthday=birthday, happiness=int(happiness), health=int(health), food=int(food), last_record=last_record)
        
    # Método que atualiza os status do Pet baseado no tempo fora de uso do aplicativo
    def updateOfflineStats(self):
        time_passed = datetime.now()-datetime.strptime(self.last_record, "%d-%m-%Y %H:%M:%S")
        time_passed = round(time_passed.total_seconds()/60)
        if(time_passed >= 5):
            self.happiness -= round(time_passed/5)
            self.happiness = max(self.happiness,0)
        if(time_passed >= 10): 
            self.food -= round(time_passed/10)
            self.food = max(self.food,0)
        if(time_passed >= 15):
            self.health -= round(time_passed/15)
            self.health = max(self.health,0)
        self.last_record = datetime.today().strftime("%d-%m-%Y %H:%M:%S")