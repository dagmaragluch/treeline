from typing import Tuple, Callable

from treeline.engine.widget import Widget
from treeline.engine.shapes.sprite import Sprite
from treeline.engine.utils.matrices import identity
import pygame


class Button(Widget):
    def __init__(
            self,
            position: Tuple[int, int],
            sprite: pygame.Surface,
            on_click_callback: Callable = None
    ):
        Widget.__init__(self, position)
        self.sprite = sprite
        self.bounds = sprite.texture.get_rect().move(position)
        self._on_click_callback = on_click_callback

    def draw(self, surface) -> pygame.Rect:
        if self.visible:
            self.sprite.draw_static(self.position, surface)
        return self.bounds

    def on_click(self):
        self._on_click_callback()
