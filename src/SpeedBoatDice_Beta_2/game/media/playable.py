import abc


class Playable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @abc.abstractmethod
    def pause(self):
        pass
