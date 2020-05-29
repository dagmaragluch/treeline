from typing import Tuple, Callable

from treeline.engine.widget import Widget
import pygame
import matplotlib.path


class Button(Widget):
    def __init__(
            self,
            position: Tuple[int, int],
            dimensions: Tuple[int, int],
            image: pygame.Surface,
            on_click_callback: Callable = None
    ):
        Widget.__init__(self, position, dimensions)
        self.image = image
        self.bounds = image.get_rect().move(position)
        self._on_click_callback = on_click_callback

    def draw(self, surface) -> pygame.Rect:
        if self.visible:
            surface.blit(self.image, self.position)
        return self.bounds

    def on_click(self):
        self._on_click_callback()
