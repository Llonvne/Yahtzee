import os

import pygame


def play():
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join('Media', 'Music', 'BGM.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(100000)


def pause():
    pygame.mixer.music.pause()
