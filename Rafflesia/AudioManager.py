from .Audio import play
import pygame
pygame.mixer.set_num_channels(512)


class AudioManager:
    def __init__(self):
        self.channelidlist = [0]*512
        super(AudioManager, self).__init__()

    def shortplay(self, filepath, channelname):
        play.shortplay(filepath, channelname, self.channelidlist)

    def longplay(self, filepath):
        play.longplay(filepath)
