from openal import Listener

def setMusicVolume(volume):
    """
    Description: Set the volume of the background music.
    Input: volume (float)
    Output: None
    """

    Listener().set_gain(volume)

def setSoundVolume(sound, volume):
    """
    Description: Set the volume of a sound.
    Input: sound (oalOpen), volume (float)
    Output: None
    """

    sound.set_gain(volume)