import abc


class Playable(metaclass=abc.ABCMeta):
    """
    可播放对象对象接口

    必须提供 play 接口
    pause 可选择提供，也可以实现为空
    """

    @abc.abstractmethod
    def play(self) -> None:
        """
        播放接口
        :return: None
        """
        pass

    @abc.abstractmethod
    def pause(self) -> None:
        """
        暂停接口
        :return: None
        """
        pass
