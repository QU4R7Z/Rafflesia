import time

from Rafflesia import AudioManager
import os

print(os.path.abspath("../lapetus.mp3"))
a = AudioManager(dev=True)
a.longload(os.path.abspath("../lapetus.mp3"))
a.longplay(infinityloop=False)
a.longbusy()
time.sleep(1)
a.longpause()
time.sleep(5)
a.longunpause()
time.sleep(5)
