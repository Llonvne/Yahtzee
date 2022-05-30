import pygame.event
from pygame.event import Event

from src.player.Player import Player


def chooseScore(player: Player, event: Event):
    # 获得选择分数的用户ID
    userId: int = int(event.__dict__.get("用户"))
    # 如果等于当前玩家ID
    if (userId - 1) == player.no:
        # 如果分数不存在的话
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'one':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.countK(1))
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'two':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.countK(2))
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'three':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.countK(3))
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'four':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.countK(4))
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'five':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.countK(5))
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'six':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.countK(6))
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'totalChoose':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.total())
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'foursame':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.fourSame())
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'calabash':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.calabash())
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'smallStraights':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.smallStraights())
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'largeStraights':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.largeStraights())
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
        if not player.board.isChoose[event.__dict__.get('位置')]:
            if event.__dict__.get('位置') == 'speedboat':
                player.board.addScore(event.__dict__.get('位置'), player.diceBoard.speedboat())
                player.board.isChoose[event.__dict__.get('位置')] = True
                pygame.event.post(
                    pygame.event.Event(
                        pygame.USEREVENT, {"类型": "游戏流程控制事件", "描述": "玩家选择分数完毕"}
                    )
                )
