import pygame
from treeline.engine.shape import Shape
from typing import List, Tuple
import numpy as np
from matplotlib.path import Path

class Polygon(Shape):

    def __init__(self, points: List[Tuple[int, int]], color: Tuple[int, int, int] = (255, 255, 255)):
        self.points = points
        self.color = color

    def draw(self, transform: np.array, surface) -> Path:
        transformedShape = [transform.dot(point) for point in self.points]
        rawPoints = np.delete(transformedShape, 2, 1)

        pygame.draw.polygon(surface, self.color, rawPoints)
        return Path(rawPoints)
