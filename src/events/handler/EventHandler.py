import abc

from src.data.GameData import GameData
from src.events.events import *


class EventHandler:
    """
    事件处理抽象类
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, data: GameData):
        """
        构造方法，默认构造data到事件处理库
        :param data:
        """
        self.data = data

    @abc.abstractmethod
    def event(self, event: pygame.event.Event):
        """
        提供抽象接口
        :param event:
        :return:
        """
        pass

    @staticmethod
    def getType(event: pygame.event.Event) -> str:
        return event.__dict__.get(event_type)

    @staticmethod
    def get_sub_type(event: pygame.event.Event) -> str:
        return event.__dict__.get(sub_type)
