import pygame
from treeline.engine.shape import Shape
from typing import List, Tuple
import numpy as np
from matplotlib.path import Path

"""
Not deprecated anymore but not tested, don't use.
"""

class Polygon(Shape):

    def __init__(self, color: Tuple[int, int, int] = (255, 255, 255)):
        self.points = []
        self.color = color

    def draw(self, transform: np.array, surface) -> Path:
        transformed_shape = [transform.dot(point) for point in self.points]
        raw_points = np.delete(transformed_shape, 2, 1)

        pygame.draw.polygon(surface, self.color, raw_points, 10)
        return None # Not clickable
