from typing import (
    Tuple,
)


class Actor:

    def __init__(self, position: Tuple[int, int]):
        self.position = position

    def on_event(self, event):
        """
        Called by engine if event (e.g. key pressed) happened
        Must be registered for particular event first by calling Engine.registerForEvent
        """
        pass
