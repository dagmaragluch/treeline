from typing import Tuple


class Widget:
    def __init__(self, position: Tuple[int, int], dimensions: Tuple[int, int]):
        self.position = position
        self.dimensions = dimensions
        self.visible = True

    def draw(self):
        raise NotImplementedError
