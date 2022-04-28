import pygame


def long_unpause(dev):
    try:
        pygame.mixer.music.unpause()
        if dev:
            print("Rafflesia Audio / long_unpause: long 일시정지 해제")
    except Exception as e:
        print(e)
