from openal import *

# Sounds
win = oalOpen("./sounds/win.wav")
lose = oalOpen("./sounds/lose.wav") 
gameOver = oalOpen("./sounds/game-over.wav")
doorbell = oalOpen("./sounds/doorbell.wav")
combatScenes = oalOpen("./sounds/combat-scenes.wav")

# Keys to press
actions = {
    "start-game": "s",
    "exit-game": "x",
    "take-gun": "tg",
    "shoot-gun": "sg",
    "drop-gun": "dg",
}

# Start the game
combatScenes.play()
pressedKey = actions["start-game"]


while (pressedKey != actions["exit-game"]):

    if (pressedKey == actions["start-game"]):
        print("---------------------------")
        print("         BIENVENIDO        ")
        print("---------------------------")

    pressedKey = input("> ")

# Release resources
oalQuit()