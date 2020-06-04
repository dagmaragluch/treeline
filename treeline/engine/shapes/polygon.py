import pygame
from treeline.engine.shape import Shape
from typing import List, Tuple
import numpy as np
from matplotlib.path import Path


class Polygon(Shape):

    def __init__(self, points: List[Tuple[float, float, float]], color: Tuple[int, int, int] = (255, 255, 255)):
        raise DeprecationWarning
        self.points = points
        self.color = color

    def draw(self, transform: np.array, surface) -> Path:
        transformed_shape = [transform.dot(point) for point in self.points]
        raw_points = np.delete(transformed_shape, 2, 1)

        pygame.draw.polygon(surface, self.color, raw_points)
        return Path(raw_points)

    def highlight(self, transform: np.array, surface):
        transformed_shape = [transform.dot(point) for point in self.points]
        raw_points = np.delete(transformed_shape, 2, 1)

        highlight_color = np.array(self.color) + 25

        pygame.draw.polygon(surface, highlight_color, raw_points, 5)

    def highlight_off(self, transform: np.array, surface):
        transformed_shape = [transform.dot(point) for point in self.points]
        raw_points = np.delete(transformed_shape, 2, 1)

        highlight_color_off = np.array(self.color) - 25

        pygame.draw.polygon(surface, highlight_color_off, raw_points, 5)
