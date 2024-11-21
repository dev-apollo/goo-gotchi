import os
import asyncio
import pet_class
from datetime import datetime

if __name__ == "__main__":
    # Se não houver o arquivo de informações do Pet, ele é criado
    if not os.path.exists("./pet_infos.txt"):
        with open("pet_infos.txt", "x") as pet_infos:
            pass

    # Verifica se já há um Pet criado ou não
    if(os.path.getsize("./pet_infos.txt") == 0):
        owner = input("Seja bem-vindo(a) ao Goo-Gotchi! O Tamagotchi de Gelecas.\nQual o seu nome?\n")
        name = input(f"Bem, {owner}, você sabe muito bem o que vem agora né?\nQual vai ser o nome da sua gelatinosa Geleca?\n")
        print(f"{name} é o nome perfeito para essa Geleca! Combina bastante com ela.")
        userPet = pet_class.Pet(owner, name, datetime.today().strftime("%d-%m-%Y"))
        userPet.writeInfos()
    else:
        userPet = pet_class.Pet.getInfos()
        print(f"Seja bem-vindo novamente {userPet.owner}, {userPet.name} estava te esperando!")
    userPet.updateOfflineStats()

    # Loop de Gameplay
    async def main():
        stats_verify = asyncio.create_task(userPet.updateInGameStatus())
        running = True
        while(running):
            await asyncio.sleep(301)
            running = False
        stats_verify.cancel()
        try:
            await stats_verify
        except asyncio.CancelledError:
            pass
        userPet.writeInfos()

    asyncio.run(main())