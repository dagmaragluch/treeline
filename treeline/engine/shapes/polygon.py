import pygame
from treeline.engine.shape import Shape
from typing import List, Tuple

class Polygon(Shape):

    def __init__(self, points: List[Tuple[int, int]], color: Tuple[int, int, int] = (255, 255, 255)):
        self.points = points
        self.color = color

    def draw(self, position: Tuple[int, int], surface):
        movedPoints = [tuple(map(sum, zip(point, position))) for point in self.points]
        pygame.draw.polygon(surface, self.color, movedPoints)
