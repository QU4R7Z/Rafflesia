import pygame


def shortplay(filepath):
    channelname = pygame.mixer.Channel()
    print(filepath)


def long_play(loops, start, infinityloop, dev):
    try:
        if infinityloop:
            pygame.mixer.music.play(-1)
            if dev:
                print(f"Rafflesia Audio / long_play: long 무한 반복재생")
        else:
            pygame.mixer.music.play(loops, start)
            if dev:
                print(f"Rafflesia Audio / long_play: {loops} 번 반복, {start}부터 시작")
    except Exception as e:
        print(e)
