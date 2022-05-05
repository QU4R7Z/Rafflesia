from Rafflesia.Graphics.td.Windows import windows
import threading


class GraphicsManager():
    def __init__(self, dev=False):
        self.dev = dev
        super(GraphicsManager, self).__init__()

    def createwindow(self, x=1280, y=720, window_title="Rafflesia_window"):
        w = threading.Thread(target=windows.create_window, name="worker_0", args=(x, y, window_title, self.dev))
        w.start()
