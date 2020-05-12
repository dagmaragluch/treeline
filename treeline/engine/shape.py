import pygame
from typing import Tuple
import numpy as np


class Shape:
    '''
    Just an interface for shapes in /shapes folder.
    Don't use it directly.
    '''

    def draw(self, transform: np.array, surface):
        raise Exception("Shape.draw shall be overriden")
