from openal import *
import time
from GameUI import GameUI

gameUI = GameUI()

def main():
    while (True):

        # Comandos especiales
        if gameUI.state == "menu": gameUI.menuScreen()
        elif gameUI.state == "potions": gameUI.potionsScreen()
        elif gameUI.state == "weapons": gameUI.weaponsScreen()
        elif gameUI.state == "exit": break

        # Estados generales
        elif (gameUI.state == "game"): gameUI.gameScreen()
        elif (gameUI.state == "settings"): gameUI.settingsScreen()
        elif (gameUI.state == "rules"): gameUI.rulesScreen()

        # Juego
        elif (gameUI.state == "walk"): gameUI.walk()
        elif (gameUI.state == "found-potion"): gameUI.foundPotion()
        elif (gameUI.state == "battle"): gameUI.battle()
        elif (gameUI.state == "final-battle"): gameUI.finalBattle()

        # Configuraciones
        elif (gameUI.state == "music-settings"): gameUI.musicSettingsScreen()
        elif (gameUI.state == "sound-settings"): gameUI.soundSettingsScreen()

    # Se liberan recursos    
    oalQuit()

main()