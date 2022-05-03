import pygame.event


class Event:
    """
    pygame Event 封装对象
    """

    def __init__(self, event: pygame.event.Event):
        self.event: pygame.event.Event = event
        self.isUserEvent = (event.type == pygame.USEREVENT)

    def isQuit(self):
        return self.event.type == pygame.QUIT

    def getType(self):
        return self.__dict__.get("类型")

    def get_sub_type(self):
        return self.__dict__.get("描述")
