import pygame


def long_pause(dev):
    try:
        pygame.mixer.music.pause()
        if dev:
            print("Rafflesia Audio / long_pause: long 일시정지")
    except Exception as e:
        print(e)
