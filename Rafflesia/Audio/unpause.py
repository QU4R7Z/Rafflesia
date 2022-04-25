import pygame


def longunpause(dev):
    try:
        pygame.mixer.music.unpause()
        if dev:
            print("Rafflesia Audio: long 일시정지 해제")
    except Exception as e:
        print(e)
