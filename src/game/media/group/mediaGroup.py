import abc

from src.game.media.media import Media


class MediaGroup(metaclass=abc.ABCMeta):
    def __init__(self, paths: list[str]):
        self._paths = paths
        self._isLoad = False
        self._medias: list[Media] = list()

    @abc.abstractmethod
    def _load(self):
        pass

    def __len__(self) -> int:
        self._load()
        return len(self._medias)

    def __getitem__(self, k: int) -> Media:
        self._load()
        return self._medias[k]

    def __iter__(self):
        self._load()
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._medias):
            self.index += 1
            return self._medias[self.index - 1]
        raise StopIteration
