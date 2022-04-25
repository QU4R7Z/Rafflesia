import pygame


def longpause(dev):
    try:
        pygame.mixer.music.pause()
        if dev:
            print("Rafflesia Audio: long 일시정지")
    except Exception as e:
        print(e)
