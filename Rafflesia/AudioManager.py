from Rafflesia.Audio import busy
from Rafflesia.Audio import load
from Rafflesia.Audio import play
from Rafflesia.Audio import pos
from Rafflesia.Audio import rewind
from Rafflesia.Audio import stop
from Rafflesia.Audio import pause
from Rafflesia.Audio import unpause
from Rafflesia.Audio import volume
import pygame

pygame.mixer.set_num_channels(2048)


class AudioManager:
    def __init__(self, dev=False):
        self.channelidlist = []
        self.dev = dev
        super(AudioManager, self).__init__()

    def shortplay(self, filepath, channelname):
        play.shortplay(filepath)

    def long_load(self, filepath):
        load.long_load(filepath, self.dev)

    def long_play(self, loops=0, start=0.0, infinityloop=False):
        play.long_play(loops, start, infinityloop, self.dev)

    def long_rewind(self):
        rewind.long_rewind(self.dev)

    def long_stop(self):
        stop.long_stop(self.dev)

    def long_pause(self):
        pause.long_pause(self.dev)

    def long_unpause(self):
        unpause.long_unpause(self.dev)

    def long_get_busy(self):
        return busy.long_get_busy(self.dev)

    def long_get_volume(self):
        return volume.long_get_volume(self.dev)

    def long_set_volume(self, value):
        volume.long_set_volume(value, self.dev)

    def long_get_pos(self):
        return pos.long_get_pos(self.dev)

    def long_set_pos(self, value):
        pos.long_set_pos(value, self.dev)
