import glfw
from Rafflesia.Graphics.td.Windows import windows


class GraphicsManager:
    def __init__(self, dev=False):
        self.dev = dev
        glfw.init()
        super(GraphicsManager, self).__init__()

    def create_window(self, x=1280, y=720, window_title="Rafflesia_window", fullscreen=False):
        window = windows.create_window(x, y, window_title, fullscreen, self.dev)
        return window

    def make_context_current(self, window):
        windows.make_context_current(window, self.dev)

    def window_should_close(self, window):
        w = windows.window_should_close(window, self.dev)
        return w

    def swap_buffers(self, window):
        windows.swap_buffers(window, self.dev)

    def poll_events(self):
        windows.poll_events(self.dev)

    def terminate(self):
        windows.terminate(self.dev)
