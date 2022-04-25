import pygame


def longbusy(dev):
    try:
        if dev:
            if pygame.mixer.music.get_busy():
                print("Rafflesia Audio / longbusy: long 재생 중")
            else:
                print("Rafflesia Audio / longbusy: long 재생 중 x")
        return pygame.mixer.music.get_busy()
    except Exception as e:
        print(e)
