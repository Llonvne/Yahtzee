import pygame

event_type = 'event_type'
sub_type = 'sub_type'

GameControllerEvent = "游戏程序控制事件"
Game_Start = "游戏开始事件"
Game_End = "游戏结束事件"
Round_Start = "回合开始"
Round_End = "回合结束"

RollControllerEvent = "骰子控制事件"
Roll = "投"
Roll_Start = "开始骰子事件"
Roll_End = '结束骰子事件'

UserInputEvent = "用户输入事件"
RemainEvent = "骰子保留事件"
ChooseEvent = "分数选择事件"

RemainK = pygame.USEREVENT + 6

RemainKEnd = pygame.USEREVENT + 10

ChooseK = pygame.USEREVENT + 7

ChooseKEnd = pygame.USEREVENT + 13


def StartGameEvent():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 1, {event_type: GameControllerEvent, sub_type: Game_Start}))


def EndGameEvent():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 12, {event_type: GameControllerEvent, sub_type: Game_End}))


def RoundStartEvent():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 11, {event_type: GameControllerEvent, sub_type: Round_Start}))


def RoundEndEvent():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 8, {event_type: GameControllerEvent, sub_type: Round_End}))


def RollEvent(k: int):
    for i in range(k):
        rollEvent = pygame.event.Event(pygame.USEREVENT + 14, {event_type: RollControllerEvent, sub_type: Roll})
        pygame.event.post(rollEvent)


def RollStartEvent():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 5, {event_type: RollControllerEvent, sub_type: Roll_Start}))


def RollEndEvent():
    pygame.event.post(pygame.event.Event(pygame.USEREVENT + 9, {event_type: RollControllerEvent, sub_type: Roll_End}))


def remainEvent(k: int) -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 6, {event_type: UserInputEvent, sub_type: RemainEvent, "remain": k}))


def chooseEvent(k: int) -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 7, {event_type: UserInputEvent, sub_type: ChooseEvent, "remain": k}))
