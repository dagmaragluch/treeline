from treeline.engine.shapes.polygon import Polygon
from math import sin, cos, radians
from typing import Tuple

DEFAULT_HEX_COLOR = (26, 107, 25)

class Hexagon(Polygon):

    def __init__(self, color: Tuple[int, int, int] = DEFAULT_HEX_COLOR):
        points = []
        for i in range(6):
            d = radians((360 / 6) * i)
            points.append((cos(d) / 2, sin(d) / 2, 1))

        Polygon.__init__(self, points, color)
