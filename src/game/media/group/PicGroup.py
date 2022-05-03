from src.game.media.types.pic import Pic


class PicGroup:
    def __init__(self, paths: list[str]):
        self._paths = paths
        self._isLoad = False
        self._medias: list[Pic] = list()

    def _load(self):
        for path in self._paths:
            self._medias.append(Pic(path))
        self._isLoad = True

    def __getitem__(self, key) -> Pic:
        self._load()
        return self._medias[key]
