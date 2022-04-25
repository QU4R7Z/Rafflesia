import time

from Rafflesia import AudioManager
import os

print(os.path.abspath("../lapetus.mp3"))
a = AudioManager(dev=True)
a.long_load(os.path.abspath("../lapetus.mp3"))
a.long_play(infinityloop=False)
a.long_get_busy()
a.long_get_volume()
time.sleep(1)
a.long_pause()
time.sleep(5)
a.long_unpause()
time.sleep(5)
