from time import sleep
from math import ceil

GAME_NAME = "BATTLE GAME 1.0"
LENGTH = 100


def printWithTime(message, type="info"):
    if (type == "info"): symbol = ">"
    elif (type == "warning"): symbol = "⚠️"
    elif (type == "error"): symbol = "❌"
    elif (type == "success"): symbol = "✅"
    else:
        userInput = input("❓ " + message + " ")
        return userInput

    print(symbol, message)
    sleep(0.04 * len(message))


def printWelcomeMessage(lifes, points):
    # Print the game name
    spaces = LENGTH - len(GAME_NAME)
    spacesLeft = spaces // 2
    spacesRight = spaces - spacesLeft

    print("-" * LENGTH)
    print(" " * spacesLeft + GAME_NAME + " " * spacesRight)
    print("-" * LENGTH)

    # Print the game description
    printWithTime(f'¡Bienvenido a {GAME_NAME}!')
    printWithTime("En esta aventura deberás enfrentarte a diferentes enemigos para sobrevivir en el juego.")
    printWithTime("Tu objetivo principal es buscar la corona perdida, que se encuentra en el castillo de la montaña.") 
    printWithTime("Pero para llegar allí deberás vencer a los enemigos que se encuentran en el camino.")
    printWithTime("Cada vez que ganes una batalla podrás tomar el arma del enemigo.")
    printWithTime("Puedes guardar hasta 2 armas y 50 pociones. Cada arma tiene un daño diferente.")
    printWithTime(f'Comienzas el juego con {lifes} vidas, {points} puntos, un arma y una pocion aleatorias.')
    printWithTime("Qué quieres hacer ahora?", "question")

def printPlayerState(player):
    lifes = player.lifes
    points = player.points
    wonnedBattles = player.wonnedBattles
    weapons = player.weapons
    potions = player.potions 

    print("-" * LENGTH)

    print("❤️ ", "Vidas:", lifes)
    print("⭐", "Puntos:", points)
    print("⚔️ ", "Partidas ganadas:", wonnedBattles)

    print("\n🗡️  Armas", f'({len(weapons)}/2):')
    for i in range(len(weapons)):
        weapon = weapons[i]
        print(f' [{i + 1}] {weapon.emoji} {weapon.name} (daño: {weapon.damage})')
    
    print("\n🧪 Pociones", f'({len(potions)}/50):')
    for i in range(len(potions)):
        potion = potions[i]
        print(f' [{i + 1}] {potion.name}')

    print("-" * LENGTH)