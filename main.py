from openal import *
from random import randint

from Game import *

# Música de fondo
background = oalOpen("./sounds/combat-scenes.wav")

# Efectos de sonido
win = oalOpen("./sounds/win.wav")
lose = oalOpen("./sounds/lose.wav") 
gameOver = oalOpen("./sounds/game-over.wav")
doorbell = oalOpen("./sounds/doorbell.wav")

# Comienza el juego
background.play()
game = Game()

while (True):

    # Estados generales
    if (game.state == "menu"): game.showMenu()
    elif (game.state == "game"): game.showGame()
    elif (game.state == "settings"): game.showSettings()
    elif (game.state == "rules"): game.showRules()
    elif (game.state == "exit"): break

    # Juego
    elif (game.state == "stats"): game.showStats()
    elif (game.state == "history"): game.showHistory()
    elif (game.state == "walk"): game.walk()
    elif (game.state == "find-potion"): game.findPotion()
    elif (game.state == "save-potion"): game.savePotion()
    elif (game.state == "use-potion"): game.usePotion()
    elif (game.state == "battle"): game.battle()
    elif (game.state == "final-battle"): game.finalBattle()

    # Configuraciones
    elif (game.state == "music-settings"): game.showMusicSettings()
    elif (game.state == "sound-settings"): game.showSoundSettings()

    # Comandos especiales
    if (game.input == "stats"): game.goToState("stats")
    elif (game.input == "exit"): game.goToState("game")

# Libera recursos
oalQuit()