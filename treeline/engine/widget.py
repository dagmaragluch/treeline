from typing import Tuple
import pygame


class Widget:
    def __init__(self, position: Tuple[int, int]):
        self.position = position
        self.visible = True

    def draw(self, surface) -> pygame.Rect:
        raise NotImplementedError

    def on_click(self):
        pass
