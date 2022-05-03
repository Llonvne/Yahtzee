import abc


class Playable(metaclass=abc.ABCMeta):
    """
    可播放对象接口
    """
    @abc.abstractmethod
    def play(self)->None:
        """
        播放接口
        :return: None
        """
        pass

    @abc.abstractmethod
    def pause(self)->None:
        """
        暂停接口
        :return: None
        """
        pass
