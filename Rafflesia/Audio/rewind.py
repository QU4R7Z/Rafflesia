import pygame


def longrewind(dev):
    try:
        pygame.mixer.music.rewind()
        if dev:
            print("Rafflesia Audio / longrewind: long 다시 재생")
    except Exception as e:
        print(e)
