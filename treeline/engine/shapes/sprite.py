import pygame
from treeline.engine.shape import Shape
import numpy as np
from typing import Tuple


class Sprite(Shape):

    def __init__(self, texture: pygame.Surface):
        self.texture = texture
        self.mask = pygame.mask.from_surface(self.texture)

    def draw(self, transform: np.array, surface: pygame.Surface) -> Tuple[pygame.Mask, Tuple[int, int]]:
        middle = transform.dot((-0.5, -0.5, 1))
        middle = tuple(map(int, np.delete(middle, 2)))
        surface.blit(self.texture, middle)
        return self.mask, middle

    def scale(self, scale: np.array):
        self.texture = pygame.transform.scale(self.texture, scale).convert_alpha()
        self.mask = pygame.mask.from_surface(self.texture)
