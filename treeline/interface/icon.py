from typing import Tuple, Callable

from treeline.engine.widget import Widget
import pygame


class Icon(Widget):
    def __init__(
            self,
            position: Tuple[int, int],
            sprite: pygame.Surface
    ):
        Widget.__init__(self, position)
        self.sprite = sprite
        self.bounds = sprite.texture.get_rect().move(position)

    def draw(self, surface) -> pygame.Rect:
        if self.visible:
            self.sprite.draw_static(self.position, surface)
        return self.bounds
