from openal import oalOpen

# Background music
background = oalOpen("./sounds/combat-scenes.wav")

# Game sounds
win = oalOpen("./sounds/win.wav")
lose = oalOpen("./sounds/lose.wav") 
gameOver = oalOpen("./sounds/game-over.wav")
doorbell = oalOpen("./sounds/doorbell.wav")

# Player sounds