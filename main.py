from openal import oalQuit
from GameUI import GameUI

gameUI = GameUI()

def main():
    while (True):

        # Estados generales
        if (gameUI.state == "menu"): gameUI.showMenu()
        elif (gameUI.state == "game"): gameUI.showGame()
        elif (gameUI.state == "settings"): gameUI.showSettings()
        elif (gameUI.state == "rules"): gameUI.showRules()
        elif (gameUI.state == "exit"): break

        # Juego
        elif (gameUI.state == "stats"): gameUI.showStats()
        elif (gameUI.state == "history"): gameUI.showHistory()
        elif (gameUI.state == "walk"): gameUI.walk()
        elif (gameUI.state == "find-potion"): gameUI.findPotion()
        elif (gameUI.state == "save-potion"): gameUI.savePotion()
        elif (gameUI.state == "use-potion"): gameUI.usePotion()
        elif (gameUI.state == "battle"): gameUI.battle()
        elif (gameUI.state == "final-battle"): gameUI.finalBattle()

        # Configuraciones
        elif (gameUI.state == "music-settings"): gameUI.showMusicSettings()
        elif (gameUI.state == "sound-settings"): gameUI.showSoundSettings()

        # Comandos especiales
        if (gameUI.input == "stats"): gameUI.goToState("stats")
        elif (gameUI.input == "exit"): gameUI.goToState("game")

main()
oalQuit()