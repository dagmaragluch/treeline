from treeline.engine.shapes.polygon import Polygon
from math import sin, cos, radians
from typing import Tuple

'''
File containing handful definitions all graphics will be drawn.
'''

DEFAULT_HEX_COLOR = (26, 107, 25)
DEFAULT_HEX_SIZE = 100  # diagonal


class Hexagon(Polygon):

    def __init__(self, color: Tuple[int, int, int] = DEFAULT_HEX_COLOR, size: int = DEFAULT_HEX_SIZE):
        points = []
        for i in range(6):
            d = radians((360 / 6) * i)
            points.append((int(cos(d) * size / 2), int(sin(d) * size / 2)))

        print(points)

        Polygon.__init__(self, points, color)
