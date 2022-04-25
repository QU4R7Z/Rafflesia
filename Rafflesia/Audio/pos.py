import pygame


def long_get_pos(dev):
    try:
        if dev:
            print(f"Rafflesia Audio / long_get_pos: long pos {pygame.mixer.music.get_pos()}")
        return pygame.mixer.music.get_pos()
    except Exception as e:
        print(e)


def long_set_pos(value, dev):
    try:
        pygame.mixer.music.set_pos(value)
        if dev:
            print(f"Rafflesia Audio / long_set_pos: long pos를 {value}으로 세팅")
    except Exception as e:
        print(e)
