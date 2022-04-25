from .Audio import busy
from .Audio import load
from .Audio import play
from .Audio import rewind
from .Audio import stop
from .Audio import pause
from .Audio import unpause
import pygame

pygame.mixer.set_num_channels(2048)


class AudioManager:
    def __init__(self, dev=False):
        self.channelidlist = []
        self.dev = dev
        super(AudioManager, self).__init__()

    def shortplay(self, filepath, channelname):
        play.shortplay(filepath)

    def longload(self, filepath):
        load.longload(filepath, self.dev)

    def longplay(self, loops=0, start=0.0, infinityloop=False):
        play.longplay(loops, start, infinityloop, self.dev)

    def longrewind(self):
        rewind.longrewind(self.dev)

    def longstop(self):
        stop.longstop(self.dev)

    def longpause(self):
        pause.longpause(self.dev)

    def longunpause(self):
        unpause.longunpause(self.dev)

    def longbusy(self):
        return busy.longbusy(self.dev)
