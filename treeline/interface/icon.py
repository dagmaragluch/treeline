from typing import Tuple, Callable

from treeline.engine.widget import Widget
import pygame


class Icon(Widget):
    def __init__(
            self,
            position: Tuple[int, int],
            image: pygame.Surface,
    ):
        Widget.__init__(self, position)
        self.image = image
        self.bounds = image.get_rect().move(position)

    def draw(self, surface) -> pygame.Rect:
        if self.visible:
            surface.blit(self.image, self.position)
        return self.bounds
