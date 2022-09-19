from openal import oalQuit
from GameUI import GameUI

def main():
    # Se ejecuta el juego
    game = GameUI()

    # Se liberan recursos    
    oalQuit()

main()
