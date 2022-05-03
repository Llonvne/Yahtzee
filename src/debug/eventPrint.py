import pygame

from src.events import events


def eventPrint(event: pygame.event.Event):
    # 只显示用户事件
    if event.type > pygame.USEREVENT:
        print(event)
