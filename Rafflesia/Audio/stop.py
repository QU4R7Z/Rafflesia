import pygame


def longstop(dev):
    try:
        pygame.mixer.music.stop()
        if dev:
            print("Rafflesia Audio: long 멈춤")
    except Exception as e:
        print(e)
