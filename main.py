from openal import *
from random import randint

from Player import *

# Música de fondo
background = oalOpen("./sounds/combat-scenes.wav")

# Sonidos de efecto
win = oalOpen("./sounds/win.wav")
lose = oalOpen("./sounds/lose.wav") 
gameOver = oalOpen("./sounds/game-over.wav")
doorbell = oalOpen("./sounds/doorbell.wav")

# Comienza el juego
background.play()
player = Player()

while (True):

    # Estados generales
    if (player.state == "showing-menu"): player.showMenu()
    elif (player.state == "in-game"): player.showGame()
    elif (player.state == "in-settings"): player.showSettings()
    elif (player.state == "in-rules"): player.showRules()
    elif (player.state == "exiting-game"): break

    # Juego
    elif (player.state == "showing-stats"): player.showStats()
    elif (player.state == "showing-history"): player.showHistory()
    elif (player.state == "found-potion"): player.foundPotion()
    elif (player.state == "saving-potion"): player.savePotion()
    elif (player.state == "using-potion"): player.usePotion()
    elif (player.state == "being-attacked"): player.beAttacked()
    elif (player.state == "fighting-for-the-crown"): player.fightForTheCrown()

    # Configuraciones
    elif (player.state == "in-music-settings"): player.showMusicSettings()
    elif (player.state == "in-sound-settings"): player.showSoundSettings()

    # Comandos especiales
    if (player.input == "stats"): player.goToState("showing-stats")
    elif (player.input == "exit"): player.goToState("exiting-game")

# Libera recursos
oalQuit()