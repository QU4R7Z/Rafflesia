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
a.long_set_volume(0.3)
a.long_get_volume()
time.sleep(1)
a.long_pause()
time.sleep(1)
a.long_unpause()
a.long_set_volume(1)
time.sleep(1)
a.long_get_pos()
time.sleep(1)
a.long_set_pos(50)
time.sleep(2)
a.long_queue("../marble.mp3")
a.long_set_pos(1700)
time.sleep(10)
