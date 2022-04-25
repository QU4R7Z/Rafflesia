import pygame


def long_get_volume(dev):
    try:
        if dev:
            print(f"Rafflesia Audio / long_get_volume: long volume: {pygame.mixer.music.get_volume()}")
        return pygame.mixer.music.get_volume()
    except Exception as e:
        print(e)
