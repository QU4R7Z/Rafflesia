import pygame


def long_get_volume(dev):
    try:
        if dev:
            print(f"Rafflesia Audio / long_get_volume: long volume {pygame.mixer.music.get_volume()*100}%")
        return pygame.mixer.music.get_volume()
    except Exception as e:
        print(e)


def long_set_volume(value, dev):
    try:
        pygame.mixer.music.set_volume(value)
        if dev:
            print(f"Rafflesia Audio / long_set_volume: long volume을 {value}으로 세팅")
    except Exception as e:
        print(e)
