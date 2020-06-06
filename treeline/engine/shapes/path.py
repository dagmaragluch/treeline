import pygame
from treeline.engine.shape import Shape
from typing import List, Tuple
import numpy as np
from matplotlib.path import Path

"""
Not deprecated anymore but not tested, don't use.
"""

class Path(Shape):

    def __init__(self, color: Tuple[int, int, int] = (255, 255, 255)):
        self.lines = []
        self.color = color
        self.primitive = True

    def draw(self, transform: np.array, surface) -> Path:
        for line in self.lines:
            transformed = [tuple(map(int, transform.dot((*point, 1)))) for point in line]
            raw = list(map(tuple, np.delete(transformed, 2, 1)))
            pygame.draw.line(surface, self.color, *raw, 5)            

        return None # Not clickable
