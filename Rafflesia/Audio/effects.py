import pygame


def long_fadeout(time, dev):
    try:
        pygame.mixer.music.fadeout(time)
        if dev:
            print(f"Rafflesia Audio / long_fadeout: long {time} fade out")
    except Exception as e:
        print(e)
