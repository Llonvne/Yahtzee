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

ScoreUpdateEvent = '分数更新事件'
ChooseScoreUpdateEvent = "用户选择分数更新事件"
smallCountUpdatedEvent = '奖励分小记更新事件'
rewardUpdatedEvent = '奖励分更新事件'
totalUpdateEvent = '总分更新事件'

ChooseKEvent = "选择第K个分数事件"
ChooseKEndEvent = '选择第K个分数结束事件'

ScreenControlEvent = "屏幕控制事件"
ScreenRefreshEvent = "屏幕刷新事件"
DisplayBackgroundEvent = "显示背景事件"
DisplayInfoEvent = '显示信息事件'
DisplayDicesEvent = '显示骰子事件'

TimeControlEvent = "事件控制事件"
WaitEvent = '等待事件'

RemainK = pygame.USEREVENT + 10

RemainKEnd = pygame.USEREVENT + 11

ChooseK = pygame.USEREVENT + 12

ChooseKEnd = pygame.USEREVENT + 13


def chooseKEvent(k: int):
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 12, {event_type: ChooseEvent, sub_type: ChooseKEvent, "no": k})
    )


def StartGameEvent():
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 1, {event_type: GameControllerEvent, sub_type: Game_Start}))


def EndGameEvent():
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 2, {event_type: GameControllerEvent, sub_type: Game_End}))


def RoundStartEvent():
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 3, {event_type: GameControllerEvent, sub_type: Round_Start}))


def RoundEndEvent():
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 3, {event_type: GameControllerEvent, sub_type: Round_End}))


def RollEvent(k: int):
    rollEvent = pygame.event.Event(pygame.USEREVENT + 4,
                                   {event_type: RollControllerEvent, sub_type: Roll, 'times': k})
    pygame.event.post(rollEvent)


def RollStartEvent():
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 6, {event_type: RollControllerEvent, sub_type: Roll_Start}))


def RollEndEvent():
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 7, {event_type: RollControllerEvent, sub_type: Roll_End}))


def remainEvent(k: int) -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 8, {event_type: UserInputEvent, sub_type: RemainEvent, "remain": k}))


def chooseEvent(k: int) -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 9, {event_type: UserInputEvent, sub_type: ChooseEvent, "remain": k}))


def updateSmallCountEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 14, {event_type: ScoreUpdateEvent, sub_type: smallCountUpdatedEvent})
    )


def updateRewardEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 15, {event_type: ScoreUpdateEvent, sub_type: rewardUpdatedEvent})
    )


def chooseScoreUpdateEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 16, {event_type: ScoreUpdateEvent, sub_type: ChooseScoreUpdateEvent})
    )


def screenRefreshEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 17, {event_type: ScreenControlEvent, sub_type: ScreenRefreshEvent})
    )


def displayBackgroundEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 18,
                           {event_type: ScreenControlEvent, sub_type: DisplayBackgroundEvent})
    )


def displayInfoEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 19, {event_type: ScreenControlEvent, sub_type: DisplayInfoEvent})
    )


def displayDicesEvent() -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 20, {event_type: ScreenControlEvent, sub_type: DisplayDicesEvent})
    )


def wait(ms: int) -> None:
    pygame.event.post(
        pygame.event.Event(pygame.USEREVENT + 21, {event_type: TimeControlEvent, sub_type: WaitEvent, 'ms': ms})
    )
