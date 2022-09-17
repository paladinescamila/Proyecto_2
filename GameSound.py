import time
from openal import *

# Música de fondo
music = oalOpen("./sounds/music.wav")

# Efectos de sonido
sounds = {
    "win": oalOpen("./sounds/win.wav"),
    "lose": oalOpen("./sounds/lose.wav"),
    "game-over" : oalOpen("./sounds/game-over.wav"),
    "open-door": oalOpen("./sounds/open-door.wav"),
    "open-chest": oalOpen("./sounds/open-chest.wav"),
    "river": oalOpen("./sounds/river.wav"),
    "walk": oalOpen("./sounds/walk.wav"),
    "open-potion": oalOpen("./sounds/open-potion.wav"),
}


class GameSound:

    def __init__(self):
        self.musicVolume = 0.01 * 5
        self.soundVolume = 0.2 * 5

        self.playMusic()


    def setMusicVolume(self, volume):
        self.musicVolume = volume * 0.01
        music.set_gain(self.musicVolume)
    

    def setSoundVolume(self, volume):
        self.soundVolume = volume * 0.2


    def getPosition(self, direction, distance):
        if direction == "left": return (-distance, 0, 0)
        elif direction == "right": return (distance, 0, 0)
        elif direction == "up": return (0, distance, 0)
        elif direction == "down": return (0, -distance, 0)
        elif direction == "front": return (0, 0, distance)
        elif direction == "back": return (0, 0, -distance)
    

    def playMusic(self):
        music.set_looping(True)
        music.set_gain(self.musicVolume)
        music.play()
    

    def playSound(self, sound, distance = 0, direction = "front"):
        sounds[sound].set_position(self.getPosition(direction, distance))
        sounds[sound].set_looping(False)
        sounds[sound].set_gain(self.soundVolume)
        sounds[sound].play()

        while sounds[sound].get_state() == AL_PLAYING:
            time.sleep(1)

        
    def playWin(self): self.playSound("win")
    def playLose(self): self.playSound("lose")
    def playGameOver(self): self.playSound("game-over")
    def playOpenDoor(self): self.playSound("open-door")
    def playOpenChest(self): self.playSound("open-chest")
    def playRiver(self): self.playSound("river", 100, "left")
    def playWalk(self): self.playSound("walk")
    def playOpenPotion(self): self.playSound("open-potion")
            
    
gameSound = GameSound()