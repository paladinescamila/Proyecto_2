from time import sleep
from openal import oalOpen, AL_PLAYING

class GameSound:

    def __init__(self):
        # Volumen inicial
        self.musicVolume = 100
        self.soundVolume = 100

        # Música de fondo
        self.playingMusic = oalOpen("./sounds/playing-music.wav")
        self.menuMusic = oalOpen("./sounds/menu-music.wav")
        self.finalBattleMusic = oalOpen("./sounds/final-battle-music.wav")
        self.winGameMusic = oalOpen("./sounds/win-game-music.wav")
        self.loseGameMusic = oalOpen("./sounds/lose-game-music.wav")

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


    # Establece el volumen de la música de fondo (%)
    def setMusicVolume(self, volume):
        self.musicVolume = int(volume)
        self.playingMusic.set_gain(self.musicVolume * 0.001)
        self.menuMusic.set_gain(self.musicVolume * 0.0017)
        self.finalBattleMusic.set_gain(self.musicVolume * 0.001)
        self.winGameMusic.set_gain(self.musicVolume * 0.001)
        self.loseGameMusic.set_gain(self.musicVolume * 0.001)


    # Establece el volumen de los efectos de sonido (%)
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


    # Devuelve una posición según la dirección y la distancia
    def getPosition(self, direction, distance):
        if direction == "left": return (-distance, 0, 0)
        elif direction == "right": return (distance, 0, 0)
        elif direction == "up": return (0, distance, 0)
        elif direction == "down": return (0, -distance, 0)
        elif direction == "front": return (0, 0, distance)
        elif direction == "back": return (0, 0, -distance)
        else: return (0, 0, 0)
    

    # Reproduce una canción de fondo
    def playMusic(self, source):
        # Detiene la música actual
        if (self.playingMusic.get_state() == AL_PLAYING): self.playingMusic.stop()
        if (self.menuMusic.get_state() == AL_PLAYING): self.menuMusic.stop()
        if (self.finalBattleMusic.get_state() == AL_PLAYING): self.finalBattleMusic.stop()
        if (self.winGameMusic.get_state() == AL_PLAYING): self.winGameMusic.stop()
        if (self.loseGameMusic.get_state() == AL_PLAYING): self.loseGameMusic.stop()

        # Reproduce la nueva música
        source.set_looping(True)
        source.play()
    

    # Reproduce un efecto de sonido
    def playSound(self, source, direction = "front", distance = 0):
        # Reproduce el sonido
        source.set_position(self.getPosition(direction, distance))
        source.set_looping(False)
        source.play()

        # Espera a que termine de reproducirse
        while source.get_state() == AL_PLAYING: sleep(1)


    # Reproducción de música de fondo
    def playPlayingMusic(self): self.playMusic(self.playingMusic)
    def playMenuMusic(self): self.playMusic(self.menuMusic)
    def playFinalBattleMusic(self): self.playMusic(self.finalBattleMusic)
    def playWinGameMusic(self): self.playMusic(self.winGameMusic)
    def playLoseGameMusic(self): self.playMusic(self.loseGameMusic)


    # Reproducción de efectos de sonido
    def playWin(self): self.playSound(self.winSound)
    def playLose(self): self.playSound(self.loseSound)
    def playGameOver(self): self.playSound(self.gameOverSound)
    def playOpenDoor(self): self.playSound(self.openDoorSound)
    def playOpenChest(self): self.playSound(self.openChestSound)
    def playWalk(self): self.playSound(self.walkSound)
    def playOpenPotion(self): self.playSound(self.openPotionSound)
    def playScream(self, direction): self.playSound(self.screamSound, direction, 15)
            
    
sound = GameSound()
