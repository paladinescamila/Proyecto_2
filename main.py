from openal import *
import time
from GameUI import GameUI

gameUI = GameUI()

def main():
    while (True):

        # Comandos especiales
        if (gameUI.input == "menu"): gameUI.goToState("menu")
        elif (gameUI.input == "exit"): gameUI.goToState("exit")
        elif (gameUI.input == "stats"): gameUI.goToState("stats")
        elif (gameUI.input == "potions"): gameUI.goToState("drink-potion")

        # Estados generales
        if (gameUI.state == "menu"): gameUI.MenuScreen()
        elif (gameUI.state == "game"): gameUI.GameScreen()
        elif (gameUI.state == "settings"): gameUI.SettingsScreen()
        elif (gameUI.state == "rules"): gameUI.RulesScreen()
        elif (gameUI.state == "exit"): break

        # Juego
        elif (gameUI.state == "stats"): gameUI.StatsScreen()
        elif (gameUI.state == "history"): gameUI.HistoryScreen()
        elif (gameUI.state == "walk"): gameUI.walk()
        elif (gameUI.state == "find-potion"): gameUI.findPotion()
        elif (gameUI.state == "drink-potion"): gameUI.drinkPotion()
        elif (gameUI.state == "battle"): gameUI.battle()
        elif (gameUI.state == "final-battle"): gameUI.finalBattle()

        # Configuraciones
        elif (gameUI.state == "music-settings"): gameUI.MusicSettingsScreen()
        elif (gameUI.state == "sound-settings"): gameUI.SoundSettingsScreen()

    # Se liberan recursos    
    oalQuit()

main()