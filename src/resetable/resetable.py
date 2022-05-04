import abc


class Resetable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(self):
        pass
