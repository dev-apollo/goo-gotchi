import tkinter
from datetime import datetime

class GameInterface:
    def __init__(self, pet):
        self.pet = pet
        self.root = tkinter.Tk()
        self.root.title("Goo-Gotchi")
        self.root.geometry("400x400")

        self.name_label = tkinter.Label(self.root, text=f"{self.pet.name}")
        self.name_label.pack()

        self.stats_label = tkinter.Label(self.root, text=self.stats_text())
        self.stats_label.pack()

        # Botões de cuidado do Pet
        self.play_button = tkinter.Button(self.root, text="Brincar", command=self.play_with_pet)
        self.play_button.pack()
        self.feed_button = tkinter.Button(self.root, text="Alimentar", command=self.feed_pet)
        self.feed_button.pack()
        self.heal_button = tkinter.Button(self.root, text="Curar", command=self.heal_pet)
        self.heal_button.pack()

        # Atualização de status
        self.last_update_time = datetime.now()
        self.update_stats()

    def stats_text(self):
        return (f"Felicidade: {self.pet.happiness}\nFome: {self.pet.food}\nSaúde: {self.pet.health}")
        
    # Funções de cuidado do Pet
    def feed_pet(self):
        self.pet.food = min(self.pet.food + 10, 100)
        self.stats_label.config(text=self.stats_text())
    def play_with_pet(self):
        self.pet.happiness = min(self.pet.happiness + 10, 100)
        self.stats_label.config(text=self.stats_text())
    def heal_pet(self):
        self.pet.health = min(self.pet.health + 10, 100)
        self.stats_label.config(text=self.stats_text())

    # Método que atualiza os status a cada 1 minuto
    def update_stats(self):
        time_passed = (datetime.now() - self.last_update_time).total_seconds() / 60
        if time_passed >= 1:
            self.last_update_time = datetime.now()
            self.pet.updateInGameStatus(time_passed)
            self.stats_label.config(text=self.stats_text())
        self.root.after(1000, self.update_stats)

    # Método para salvar as informações do Pet e destruir a janela
    def save_exit(self):
        self.pet.writeInfos()
        self.root.destroy()