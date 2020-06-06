from typing import Tuple
from treeline.engine.shape import Shape


class Actor:

    def __init__(self, position: Tuple[float, float] = None, shape: Shape = None):
        self.position = position
        self.shape = shape
        self.primitive = not shape or shape.primitive

    def on_event(self, event):
        """
        Called by engine if event (e.g. key pressed) happened (only once!).
        Must be registered for particular event first by calling Engine.registerForEvent.
        """
        pass

    def on_key(self, keys, delta_time):
        """
        Called by engine **every frame** if this actor is registered for key listening.
        """
        pass

    def on_pressed(self):
        """
        Called by engine if this actor was pressed.
        """
        pass
