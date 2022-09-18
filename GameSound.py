import time
from openal import *

class GameSound:

    def __init__(self):

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

        self.playMenuMusic()


    def setMusicVolume(self, volume):
        self.menuMusic.set_gain(volume * 0.01)
    

    def setSoundVolume(self, volume):
        self.winSound.set_gain(volume * 0.01)
        self.loseSound.set_gain(volume * 0.01)
        self.gameOverSound.set_gain(volume * 0.01)
        self.openDoorSound.set_gain(volume * 0.01)
        self.openChestSound.set_gain(volume * 0.01)
        self.walkSound.set_gain(volume * 0.01)
        self.openPotionSound.set_gain(volume * 0.01)


    def getPosition(self, direction, distance):
        if direction == "left": return (-distance, 0, 0)
        elif direction == "right": return (distance, 0, 0)
        elif direction == "up": return (0, distance, 0)
        elif direction == "down": return (0, -distance, 0)
        elif direction == "front": return (0, 0, distance)
        elif direction == "back": return (0, 0, -distance)
    

    def playMusic(self, source):
        source.set_looping(True)
        source.play()
    

    def playSound(self, source, distance = 0, direction = "front"):
        source.set_position(self.getPosition(direction, distance))
        source.set_looping(False)
        source.play()

        while source.get_state() == AL_PLAYING:
            time.sleep(1)


    def playMenuMusic(self): self.playMusic(self.menuMusic)
    def playWin(self): self.playSound(self.winSound)
    def playLose(self): self.playSound(self.loseSound)
    def playGameOver(self): self.playSound(self.gameOverSound)
    def playOpenDoor(self): self.playSound(self.openDoorSound)
    def playOpenChest(self): self.playSound(self.openChestSound)
    def playWalk(self): self.playSound(self.walkSound)
    def playOpenPotion(self): self.playSound(self.openPotionSound)
            
    
gameSound = GameSound()