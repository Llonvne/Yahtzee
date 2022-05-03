import abc


class Media(metaclass=abc.ABCMeta):
    """
    外部资源对象抽象包装类
    """

    def __init__(self, path: str):
        self._path = path

    @abc.abstractmethod
    def _pygameLoad(self):
        pass
