import pygame
from treeline.engine.shape import Shape
import numpy as np
from typing import Tuple


class Sprite(Shape):

    def __init__(self, texture: pygame.Surface, scale: np.array, keep_proportions: bool=False):
        Shape.__init__(self)
        if keep_proportions:
            scale_normalized = scale / np.linalg.norm(scale)
            scale = np.array(texture.get_rect().size) * scale_normalized
        scale = tuple(map(int, scale))
        self.texture = pygame.transform.scale(texture, scale).convert_alpha()
        self.mask = pygame.mask.from_surface(self.texture)

    def draw(self, transform: np.array, surface: pygame.Surface) -> Tuple[pygame.Mask, Tuple[int, int]]:
        middle = transform.dot((-0.5, -0.5, 1))
        middle = tuple(map(int, np.delete(middle, 2)))
        surface.blit(self.texture, middle)
        return self.mask, middle

    def draw_static(self, positon: Tuple[int, int], surface: pygame.Surface):
        surface.blit(self.texture, positon)

    def scale(self, scale: np.array):
        raise DeprecationWarning
        self.texture = pygame.transform.scale(self.texture, scale).convert_alpha()
        self.mask = pygame.mask.from_surface(self.texture)
