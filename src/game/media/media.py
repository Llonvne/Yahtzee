import abc


class Media(metaclass=abc.ABCMeta):
    """
    外部资源公共父类
    所有外部资源必须由 path 路径初始化
    且提供 _pygameLoad 函数用于初始化
    """

    def __init__(self, path: str):
        """
        初始化对象路径
        :param path:
        """
        self._path = path

    @abc.abstractmethod
    def _pygameLoad(self):
        """
        转换为pygame格式的函数
        :return:
        """
        pass

    def getPath(self) -> str:
        """
        该方法将会返回地址
        :return:
        """
        return self._path