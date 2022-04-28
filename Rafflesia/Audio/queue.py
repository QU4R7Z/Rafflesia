import pygame


def long_queue(filepath, dev):
    try:
        pygame.mixer.music.queue(filepath)
        if dev:
            print(f"Rafflesia Audio /long_queue: {filepath} long에 queue")
    except Exception as e:
        print(e)
