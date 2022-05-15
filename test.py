import sys
from Rafflesia import AudioManager
from Rafflesia import GraphicsManager
import os
import time
import numpy
from OpenGL.GL import *
import OpenGL.GL.shaders

Rafflesia_audio = AudioManager(dev=True)
Rafflesia_audio.long_load(os.path.abspath("../heathens_shi3do_edit.mp3"))
Rafflesia_audio.long_play(infinityloop=True)

Graphics = GraphicsManager(dev=True)
testwindow = Graphics.create_window(1280, 720)
Graphics.make_context_current(testwindow)
Graphics.draw_triangle()


if not testwindow:
    Graphics.terminate()

mainLoop = True
while mainLoop:
    Graphics.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    Graphics.swap_buffers(testwindow)
    if Graphics.window_should_close(testwindow):
        mainLoop = False

Graphics.terminate()
sys.exit()
