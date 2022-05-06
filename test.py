import sys
from Rafflesia import AudioManager
from Rafflesia import GraphicsManager
import os
import time
import numpy
from OpenGL.GL import *
import OpenGL.GL.shaders

Rafflesia_audio = AudioManager(dev=True)
Rafflesia_audio.long_load(os.path.abspath("../lapetus.mp3"))
Rafflesia_audio.long_play(infinityloop=False)

Graphics = GraphicsManager.GraphicsManager(dev=True)
testwindow = Graphics.create_window(1280, 720)
Graphics.make_context_current(testwindow)


triangle = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0]

triangle = numpy.array(triangle, dtype=numpy.float32)

VERTEX_SHADER = """
        #version 330

        in vec4 position;
        void main() {
        gl_Position = position;
    }
    """

FRAGMENT_SHADER = """
        #version 330

        void main() {
        gl_FragColor = 
        vec4(1.0f, 1.0f, 1.0f,1.0f);
        }
    """

shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(VERTEX_SHADER, GL_VERTEX_SHADER),
                                          OpenGL.GL.shaders.compileShader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER))

VBO = glGenBuffers(1)

glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, 36, triangle, GL_STATIC_DRAW)

position = glGetAttribLocation(shader, 'position')
glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0, None)
glEnableVertexAttribArray(position)

glUseProgram(shader)

glClearColor(0.0, 0.0, 0.0, 1.0)



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
