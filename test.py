from openal import * 
import time


def playSound(source):
    source.set_position((0, 0, 0))
    print(source.position)
    source.play()

    while source.get_state() == AL_PLAYING:
        time.sleep(1)
        
source = oalOpen("./sounds/Battle.wav")
playSound(source)

oalQuit()