from typing import Tuple
from treeline.glengine.shape import Shape
import numpy as np


class Actor:

    def __init__(self, position: Tuple[float, float] = None, shape: Shape = None):
        self.position = np.append(position, 1)
        self.shape = shape

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
