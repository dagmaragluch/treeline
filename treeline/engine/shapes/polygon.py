import pygame
from treeline.engine.shape import Shape
from typing import List, Tuple
import numpy as np

class Polygon(Shape):

    def __init__(self, points: List[Tuple[int, int]], color: Tuple[int, int, int] = (255, 255, 255)):
        self.points = np.array(points)
        self.color = color

    def draw(self, transform: np.array, surface):
        transformedShape = [transform.dot(point) for point in self.points]
        
        pygame.draw.polygon(surface, self.color, np.delete(transformedShape, 2, 1))
