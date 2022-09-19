from time import sleep
from openal import *

class GameSound:

    def __init__(self):
        # Volumen
        self.musicVolume = 100
        self.soundVolume = 100

        # Música de fondo
        self.menuMusic = oalOpen("./sounds/menu-music.wav")

        # Efectos de sonido
        self.winSound = oalOpen("./sounds/win.wav")
        self.loseSound = oalOpen("./sounds/lose.wav")
        self.gameOverSound = oalOpen("./sounds/game-over.wav")
        self.openDoorSound = oalOpen("./sounds/open-door.wav")
        self.openChestSound = oalOpen("./sounds/open-chest.wav")
        self.walkSound = oalOpen("./sounds/walk.wav")
        self.openPotionSound = oalOpen("./sounds/open-potion.wav")
        self.screamSound = oalOpen("./sounds/scream.wav")

        # Inicialización
        self.setMusicVolume(self.musicVolume)
        self.setSoundVolume(self.soundVolume)
        self.playMenuMusic()


    def setMusicVolume(self, volume):
        self.musicVolume = int(volume)
        self.menuMusic.set_gain(self.musicVolume * 0.0001)
    

    def setSoundVolume(self, volume):
        self.soundVolume = int(volume)
        self.winSound.set_gain(self.soundVolume * 0.01)
        self.loseSound.set_gain(self.soundVolume * 0.01)
        self.gameOverSound.set_gain(self.soundVolume * 0.01)
        self.openDoorSound.set_gain(self.soundVolume * 0.01)
        self.openChestSound.set_gain(self.soundVolume * 0.01)
        self.walkSound.set_gain(self.soundVolume * 0.01)
        self.openPotionSound.set_gain(self.soundVolume * 0.01)
        self.screamSound.set_gain(self.soundVolume * 0.01)


    def getPosition(self, direction, distance):
        if direction == "left": return (-distance, 0, 0)
        elif direction == "right": return (distance, 0, 0)
        elif direction == "up": return (0, distance, 0)
        elif direction == "down": return (0, -distance, 0)
        elif direction == "front": return (0, 0, distance)
        elif direction == "back": return (0, 0, -distance)
        else: return (0, 0, 0)
    

    def playMusic(self, source):
        source.set_looping(True)
        source.play()
    

    def playSound(self, source, direction = "front", distance = 0):
        source.set_position(self.getPosition(direction, distance))
        source.set_looping(False)
        source.play()

        while source.get_state() == AL_PLAYING: sleep(1)


    def playMenuMusic(self): self.playMusic(self.menuMusic)

    def playWin(self): self.playSound(self.winSound)
    def playLose(self): self.playSound(self.loseSound)
    def playGameOver(self): self.playSound(self.gameOverSound)
    def playOpenDoor(self): self.playSound(self.openDoorSound)
    def playOpenChest(self): self.playSound(self.openChestSound)
    def playWalk(self): self.playSound(self.walkSound)
    def playOpenPotion(self): self.playSound(self.openPotionSound)
    def playScream(self, direction): self.playSound(self.screamSound, direction, 15)
            
    
gameSound = GameSound()