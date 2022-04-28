import pygame


def long_stop(dev):
    try:
        pygame.mixer.music.stop()
        if dev:
            print("Rafflesia Audio / long_stop: long 멈춤")
    except Exception as e:
        print(e)
