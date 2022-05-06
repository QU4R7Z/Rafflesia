from Rafflesia.Graphics import td_shapes_square
from Rafflesia.Graphics import td_shapes_triangle
from Rafflesia.Graphics import td_windows
import glfw


class GraphicsManager:
    def __init__(self, dev=False):
        self.dev = dev
        glfw.init()
        super(GraphicsManager, self).__init__()

    def create_window(self, x=1280, y=720, window_title="Rafflesia_window", fullscreen=False):
        window = td_windows.create_window(x, y, window_title, fullscreen, self.dev)
        return window

    def draw_triangle(self):
        td_shapes_triangle.draw_triangle(self.dev)

    def draw_square(self):
        td_shapes_square.draw_square(self.dev)

    def make_context_current(self, window):
        td_windows.make_context_current(window, self.dev)

    def window_should_close(self, window):
        w = td_windows.window_should_close(window, self.dev)
        return w

    def swap_buffers(self, window):
        td_windows.swap_buffers(window, self.dev)

    def poll_events(self):
        td_windows.poll_events(self.dev)

    def terminate(self):
        td_windows.terminate(self.dev)
