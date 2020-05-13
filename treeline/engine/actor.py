from typing import (
    Tuple,
)
from treeline.engine.shape import Shape


class Actor:

    def __init__(self, position: Tuple[float, float] = None, shape: Shape = None):
        self.position = position
        self.shape = shape

    def on_event(self, event):
        """
        Called by engine if event (e.g. key pressed) happened (only once!).
        Must be registered for particular event first by calling Engine.registerForEvent.
        """
        pass

    def on_key(self, keys, deltaTime):
        """
        Called by engine **every frame** if this actor is registered for key listening.
        """
        pass
