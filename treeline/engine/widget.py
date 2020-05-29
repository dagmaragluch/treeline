from typing import Tuple
import pygame

class Widget:
    def __init__(self, position: Tuple[int, int], dimensions: Tuple[int, int]):
        self.position = position
        self.dimensions = dimensions
        self.visible = True

    def draw(self, surface) -> pygame.Rect:
        raise NotImplementedError

    def on_click(self):
        pass
