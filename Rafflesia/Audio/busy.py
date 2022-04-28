import pygame


def long_get_busy(dev):
    try:
        if dev:
            if pygame.mixer.music.get_busy():
                print("Rafflesia Audio / long_busy: long 재생 중")
            else:
                print("Rafflesia Audio / long_busy: long 재생 중 x")
        return pygame.mixer.music.get_busy()
    except Exception as e:
        print(e)
