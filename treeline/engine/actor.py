from typing import (
    Tuple,
)
from treeline.engine.shape import Shape


class Actor:

    def __init__(self, position: Tuple[int, int] = None, shape: Shape = None):
        self.position = position
        self.shape = shape

    def on_event(self, event):
        """
        Called by engine if event (e.g. key pressed) happened
        Must be registered for particular event first by calling Engine.registerForEvent
        """
        pass
