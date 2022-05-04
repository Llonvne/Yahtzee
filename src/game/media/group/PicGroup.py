from src.game.media.types.pic import Pic


class PicGroup:
    def __init__(self, paths: list[str]):
        self._pics = list()
        for path in paths:
            self._pics.append(Pic(path))

    def __getitem__(self, key) -> Pic:
        return self._pics[key]

    def __len__(self):
        return len(self._pics)
