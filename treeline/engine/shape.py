import pygame
from typing import Tuple
import numpy as np


class Shape:
    """
    Just an interface for shapes in /shapes folder.
    Don't use it directly.
    """

    def draw(self, transform: np.array, surface) -> Tuple[pygame.Mask, Tuple[int, int]]:
        raise NotImplementedError

    def scale(self, scale: np.array):
        pass
