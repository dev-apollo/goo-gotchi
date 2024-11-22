import os
import tkinter
from tkinter import messagebox, simpledialog
import game_interface
import pet_class
from datetime import datetime

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Iniciando...")
    root.geometry("230x20")

    # Se não houver o arquivo de informações do Pet, ele é criado
    if not os.path.exists("./pet_infos.txt"):
        with open("pet_infos.txt", "x") as pet_infos:
            pass

    # Verifica se já há um Pet criado ou não
    if(os.path.getsize("./pet_infos.txt") == 0):
        owner = simpledialog.askstring("Goo-Gootchi","Seja bem-vindo(a) ao Goo-Gotchi! O Tamagotchi de Gelecas.\nQual o seu nome?\n")
        name = simpledialog.askstring("Goo-Gootchi", f"Bem, {owner}, você sabe muito bem o que vem agora né?\nQual vai ser o nome da sua gelatinosa Geleca?\n")
        messagebox.showinfo("Goo-Gootchi", f"{name} é o nome perfeito para essa Geleca! Combina bastante com ela.")
        userPet = pet_class.Pet(owner, name, datetime.today().strftime("%d-%m-%Y"))
        userPet.writeInfos()
    else:
        userPet = pet_class.Pet.getInfos()
        messagebox.showinfo("Goo-Gootchi", f"Bem-vindo novamente {userPet.owner}!\n{userPet.name} estava te esperando.")
        userPet.updateOfflineStats()
    root.destroy()

    gui = game_interface.GameInterface(userPet)
    # Protocolo para quando uma janela do Windows é fechada
    gui.root.protocol("WM_DELETE_WINDOW", gui.save_exit)
    gui.root.mainloop()