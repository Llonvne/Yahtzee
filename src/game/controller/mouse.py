import pygame
from pygame.event import Event, post


def event(event, postFunc) -> None:
    print(event.__dict__.get('pos')[0], event.__dict__.get('pos')[1])
    if 768 < event.__dict__.get('pos')[0] < 858 and 621 < event.__dict__.get('pos')[1] < 664:
        postFunc("骰子事件", "投")
    elif 551 < event.__dict__.get('pos')[0] < 651 and 64 < event.__dict__.get('pos')[1] < 157:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 0}))
    elif 651 < event.__dict__.get('pos')[0] < 751 and 64 < event.__dict__.get('pos')[1] < 157:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 1}))
    elif 751 < event.__dict__.get('pos')[0] < 851 and 64 < event.__dict__.get('pos')[1] < 157:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 2}))
    elif 851 < event.__dict__.get('pos')[0] < 981 and 64 < event.__dict__.get('pos')[1] < 157:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 3}))
    elif 951 < event.__dict__.get('pos')[0] < 1051 and 64 < event.__dict__.get('pos')[1] < 157:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 4}))