import numpy
from OpenGL.GL import *
import OpenGL.GL.shaders


def draw_triangle(dev):
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


