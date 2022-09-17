import time
from openal import *

# Música de fondo
music = oalOpen("./sounds/combat-scenes.wav")

# Efectos de sonido
sounds = {
    "win": oalOpen("./sounds/win.wav"),
    "lose": oalOpen("./sounds/lose.wav"),
    "game-over" : oalOpen("./sounds/game-over.wav")
}


class GameSound:

    def __init__(self):
        self.music = music
        self.sound = oalOpen("./sounds/win.wav")

        self.playMusic()


    def setMusicVolume(self, volume):
        self.music.set_gain(volume * 0.2)
    

    def setSoundVolume(self, volume):
        self.sound.set_gain(volume * 0.2)


    def getPosition(self, direction, distance):
        if direction == "left": return (-distance, 0, 0)
        elif direction == "right": return (distance, 0, 0)
        elif direction == "up": return (0, distance, 0)
        elif direction == "down": return (0, -distance, 0)
        elif direction == "front": return (0, 0, distance)
        elif direction == "back": return (0, 0, -distance)
    

    def playMusic(self):
        self.music.set_looping(True)
        self.music.play()
    

    def playSound(self, sound, distance = 0, direction = "front"):
        self.sound = sounds[sound]
        self.sound.set_looping(False)
        self.sound.set_position(self.getPosition(direction, distance))
        self.sound.set_gain(self.soundVolume)
        self.sound.play()

        while self.sound.get_state() == AL_PLAYING:
            time.sleep(1)

        
    def playWin(self): self.playSound("win")
    def playLose(self): self.playSound("lose")
    def playGameOver(self): self.playSound("game-over")
            
    
gameSound = GameSound()