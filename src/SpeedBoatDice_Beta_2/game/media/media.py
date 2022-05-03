import abc


class Media(metaclass=abc.ABCMeta):
    """
    视频，音乐，图片，基本类型
    """

    def __init__(self, path: str):
        self._path = path

    @abc.abstractmethod
    def __pygameLoad(self):
        pass
