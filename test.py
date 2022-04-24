import time

from Rafflesia import AudioManager
import os

print(os.path.abspath("../lapetus.mp3"))
a = AudioManager()
a.shortplay(os.path.abspath("../lapetus.mp3"))
