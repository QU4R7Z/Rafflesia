import pygame


def longload(filepath, dev):
    try:
        pygame.mixer.music.load(filepath)
        if dev:
            print(f"Rafflesia Audio: {filepath} long에 load됨")
    except Exception as e:
        print(e)