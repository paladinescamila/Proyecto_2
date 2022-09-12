from openal import *
from random import randint

from Player import *

# Sounds
win = oalOpen("./sounds/win.wav")
lose = oalOpen("./sounds/lose.wav") 
gameOver = oalOpen("./sounds/game-over.wav")
doorbell = oalOpen("./sounds/doorbell.wav")
combatScenes = oalOpen("./sounds/combat-scenes.wav")

# Start the game
player = Player()
combatScenes.play()

print("---------------------------")
print("     NOMBRE DEL JUEGO      ")
print("---------------------------")
print("1. Jugar (play)")
print("2. Salir (exit)")

while (True):

    pressedKey = input("> ")

    if (pressedKey == "play"):
        print("Mensaje largo de bienvenida...")
        print("Mensaje con las reglas del juego...")
        player.beAttacked()
    
    elif (pressedKey == "exit"):
        print("Saliendo del juego...")
        break

    else:
        print("Por favor, elige una opción válida")

# Release resources
oalQuit()