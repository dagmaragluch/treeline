import pygame
from treeline.engine.shape import Shape
import numpy as np
from matplotlib.path import Path


class Sprite(Shape):

    def __init__(self, texture: pygame.Surface):
        self.texture = texture

    def draw(self, transform: np.array, surface: pygame.Surface) -> Path:
        middle = transform.dot((-0.5, -0.5, 1))
        middle = np.delete(middle, 2)
        surface.blit(self.texture, tuple(map(int, middle)))
        return None

    def scale(self, scale: np.array):
        self.texture = pygame.transform.scale(self.texture, scale).convert_alpha()
