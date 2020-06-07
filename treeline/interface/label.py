import pygame
import pygame.freetype
from pygame.freetype import Font

from typing import Tuple

from treeline.model.player import Player
from treeline.engine.widget import Widget


class Label(Widget):
    def __init__(self, position: Tuple[int, int], font: Font, text: str = ""):
        Widget.__init__(self, position)
        self.font = font
        self.text = text

    def draw(self, surface) -> pygame.Rect:
        self.font.render_to(surface, self.position, self.text, (0, 0, 0))
        return pygame.Rect(1, 2, 3, 4)
