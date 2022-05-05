import glfw
from Rafflesia.Graphics.td.Shapes import triangle
from Rafflesia.Graphics.td.Windows import windows
import threading


class GraphicsManager:
    def __init__(self, dev=False):
        self.dev = dev
        self.drawer = []
        glfw.init()
        super(GraphicsManager, self).__init__()

    def createwindow(self, x=1280, y=720, window_title="Rafflesia_window", fullscreen=False):
        w = threading.Thread(target=windows.create_window, name="worker_0", args=(x, y, window_title, fullscreen, self.drawer,
                                                                                  self.dev))
        w.start()

    def draw_triangle(self):
        triangle.draw_triangle(self.drawer, self.dev)