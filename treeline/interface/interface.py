from typing import Tuple

from treeline.model.game import Game
from treeline.interface.button import Button
import pygame


class Interface:
    def __init__(self, game: Game, resolution: Tuple[int, int] = (1920, 1080)):
        self.game = game
        self.resolution = resolution
        self.widgets = [self._create_end_turn_button()]

    def _create_end_turn_button(self) -> Button:
        image = pygame.image.load("./resources/graphics/buttons/end-turn.bmp")
        x = self.resolution[0] * 4 // 5
        y = self.resolution[1] * 5 // 6
        width = self.resolution[0] // 6
        height = self.resolution[0] // 8
        end_turn_button = Button(
            (x, y), (width, height), image, self.game.end_turn)
        return end_turn_button
