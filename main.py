from openal import *
from random import randint

from Player import *

from gameUI import *
from gameSettings import *
from gameSounds import *

# Player game states
# - starting-game
# - changing-settings
# - exiting-game
# - attacking
# - being-attacked
# - picking-weapon
# - picking-potion
# - saving-weapon
# - saving-potion
# - fighting-for-the-crown
# - wining
# - losing
# - game-over
playerState = "in-game-menu"

# Start the game
background.play()

player = Player()
printWelcomeMessage(player.lifes, player.points)
printPlayerState(player)

while (playerState != "exiting-game"):
    # player.beAttacked()
    printWithTime("¿Qué quieres hacer?", "question")

# Release resources
oalQuit()