from typing import Tuple, Callable

from treeline.engine.widget import Widget


class Button(Widget):
    def __init__(
            self,
            position: Tuple[int, int],
            dimensions: Tuple[int, int],
            image,  # TODO image type
            on_click_callback: Callable = None
    ):
        Widget.__init__(self, position, dimensions)
        self.image = image
        self._on_click_callback = on_click_callback

    def draw(self):
        if self.visible:
            pass  # TODO drawing

    def on_click(self):
        self._on_click_callback()
