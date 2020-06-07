from treeline.engine.actor import Actor
from treeline.engine.shapes.path import Path
from treeline.model.field import Field
from typing import List, Tuple
import numpy as np
from math import sin, cos, radians, sqrt

d30 = radians(30)

_ROTATE_RIGHT = np.array([[cos(d30), -sin(d30)], [sin(d30), cos(d30)]])
_ROTATE_LEFT = np.array([[cos(-d30), -sin(-d30)], [sin(-d30), cos(-d30)]])


class Border(Actor):

    def __init__(self, color: Tuple[int, int, int]):
        Actor.__init__(self, (0, 0), Path(color))

    def advanced_calculations(self, border_fields: List[Field]):
        border = []
        for inside, outside in border_fields:
            x = np.array(inside.position)
            y = np.array(outside.position)
            offset = (x - np.array(self.position)) / 4 * np.array((sqrt(3), 1)) * sqrt(3)
            direction = (y - x) / 4 * np.array((sqrt(3), 1))

            border.append((
                tuple(_ROTATE_LEFT @ direction + offset),
                tuple(_ROTATE_RIGHT @ direction + offset)
            ))

        self.shape.lines = border
