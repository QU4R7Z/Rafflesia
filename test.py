import time

from Rafflesia import AudioManager
from Rafflesia import GraphicsManager
import os

window = GraphicsManager.GraphicsManager()
window.createwindow(1280, 720)
window.draw_triangle()

print(os.path.abspath("../lapetus.mp3"))
Rafflesia_audio = AudioManager(dev=True)
Rafflesia_audio.long_load(os.path.abspath("../lapetus.mp3"))
Rafflesia_audio.long_play(infinityloop=False)
Rafflesia_audio.long_get_busy()
Rafflesia_audio.long_get_volume()
time.sleep(1)
Rafflesia_audio.long_get_volume()
time.sleep(1)
Rafflesia_audio.long_get_pos()
time.sleep(1)
Rafflesia_audio.long_queue("../marble.mp3")
Rafflesia_audio.long_set_pos(100)
Rafflesia_audio.long_get_pos()
Rafflesia_audio.long_fadeout(3000)
time.sleep(3)
Rafflesia_audio.long_rewind()
Rafflesia_audio.long_play()
Rafflesia_audio.long_set_pos(130)
