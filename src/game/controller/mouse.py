import pygame
from pygame.event import Event, post


def event(event: pygame.event.Event, postFunc) -> None:
    """
    鼠标 buttonDown 处理函数，将特定区域鼠标点击事件，转换为游戏事件
    :param event: pygame.event.Event
    :param postFunc: 引发事件函数
    :return: None
    :no 11 12用于记录用户一的小节和奖励分事件
    :no 25 26用于记录用户二的小节和奖励分事件
    :no 5-18 用于记录用户一的所有选择事件
    :no 19-32 用于记录用户二的所有选择事件
    """
    print(event.__dict__.get('pos')[0], event.__dict__.get('pos')[1])
    if 720 < event.__dict__.get('pos')[0] < 797 and 597 < event.__dict__.get('pos')[1] < 678:
        postFunc("骰子事件", "投")
    elif 551 < event.__dict__.get('pos')[0] < 651 and 200 < event.__dict__.get('pos')[1] < 300:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 0}))
    elif 651 < event.__dict__.get('pos')[0] < 751 and 200 < event.__dict__.get('pos')[1] < 300:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 1}))
    elif 751 < event.__dict__.get('pos')[0] < 851 and 200 < event.__dict__.get('pos')[1] < 300:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 2}))
    elif 851 < event.__dict__.get('pos')[0] < 981 and 200 < event.__dict__.get('pos')[1] < 300:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 3}))
    elif 951 < event.__dict__.get('pos')[0] < 1051 and 200 < event.__dict__.get('pos')[1] < 300:
        post(Event(pygame.USEREVENT, {'类型': '骰子事件', '描述': '选择', 'no': 4}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 133 < event.__dict__.get('pos')[1] < 168:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 5,'用户':'1','位置':'one'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 168 < event.__dict__.get('pos')[1] < 203:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 6, '用户': '1', '位置': 'two'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 203 < event.__dict__.get('pos')[1] < 239:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 7, '用户': '1', '位置': 'three'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 239 < event.__dict__.get('pos')[1] < 273:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 8, '用户': '1', '位置': 'four'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 273 < event.__dict__.get('pos')[1] < 307:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 9, '用户': '1', '位置': 'five'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 307 < event.__dict__.get('pos')[1] < 342:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 10, '用户': '1', '位置': 'six'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 428 < event.__dict__.get('pos')[1] < 462:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 13, '用户': '1', '位置': 'totalChoose'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 470 < event.__dict__.get('pos')[1] < 504:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 14, '用户': '1', '位置': 'foursame'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 504 < event.__dict__.get('pos')[1] < 539:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 15, '用户': '1', '位置': 'calabash'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 539 < event.__dict__.get('pos')[1] < 573:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 16, '用户': '1', '位置': 'smallStraights'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 573 < event.__dict__.get('pos')[1] < 608:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 17, '用户': '1', '位置': 'largeStraights'}))
    elif 174 < event.__dict__.get('pos')[0] < 253 and 608 < event.__dict__.get('pos')[1] < 645:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 18, '用户': '1', '位置': 'speedboat'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 133 < event.__dict__.get('pos')[1] < 168:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 19,'用户':'2','位置':'one'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 168 < event.__dict__.get('pos')[1] < 203:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 20, '用户': '2', '位置': 'two'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 203 < event.__dict__.get('pos')[1] < 239:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 21, '用户': '2', '位置': 'three'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 239 < event.__dict__.get('pos')[1] < 273:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 22, '用户': '2', '位置': 'four'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 273 < event.__dict__.get('pos')[1] < 307:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 23, '用户': '2', '位置': 'five'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 307 < event.__dict__.get('pos')[1] < 342:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 24, '用户': '2', '位置': 'six'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 428 < event.__dict__.get('pos')[1] < 462:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 27, '用户': '2', '位置': 'totalChoose'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 470 < event.__dict__.get('pos')[1] < 504:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 28, '用户': '2', '位置': 'foursame'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 504 < event.__dict__.get('pos')[1] < 539:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 29, '用户': '2', '位置': 'calabash'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 539 < event.__dict__.get('pos')[1] < 573:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 30, '用户': '2', '位置': 'smallStraights'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 573 < event.__dict__.get('pos')[1] < 608:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 31, '用户': '2', '位置': 'largeStraights'}))
    elif 253 < event.__dict__.get('pos')[0] < 335 and 608 < event.__dict__.get('pos')[1] < 645:
        post(Event(pygame.USEREVENT, {'类型': '分数选择', '描述': '选择', 'no': 32, '用户': '2', '位置': 'speedboat'}))
