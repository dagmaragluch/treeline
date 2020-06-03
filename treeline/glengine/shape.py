import pygame
from typing import Tuple
import numpy as np
import matplotlib.path


class Shape:

    vertex_data = np.array([-1, -1, 0, 0, -1, 1, 0, 1, 1, 1, 1, 1, -1, -1, 0, 0, 1, 1, 1, 1, 1, -1, 1, 0], np.float32)  # Just a square

    def __init__(self):
        self.texture = None
        self.image_data = None


class Splash(Shape):

    def __init__(self, image: pygame.Surface):
        self.texture = image
        self.image_data = pygame.image.tostring(self.texture, "RGBA", True)
