import pygame
from typing import Tuple


class Shape:
    '''
    Just an interface for shapes in /shapes folder.
    Don't use it directly.
    '''

    def draw(self, position: Tuple[int, int], surface):
        raise Exception("Shape.draw shall be overriden")
