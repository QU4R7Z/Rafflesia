import pygame
pygame.init()

def shortplay(filepath, channelname):
    channelname = pygame.mixer.Channel()
    print(filepath)


def longplay(filepath):
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    print(filepath)
