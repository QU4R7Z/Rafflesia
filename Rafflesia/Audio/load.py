import pygame


def long_load(filepath, dev):
    try:
        pygame.mixer.music.load(filepath)
        if dev:
            print(f"Rafflesia Audio / longload: {filepath} long에 load됨")
    except Exception as e:
        print(e)
