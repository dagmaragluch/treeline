from typing import Tuple

from treeline.model.game import Game
from treeline.interface.button import Button
import pygame


class Interface:
    def __init__(self, game: Game, resolution: Tuple[int, int] = (1920, 1080)):
        self.game = game
        self.resolution = resolution
        self.widgets = [
            self._create_end_turn_button(),
            self._create_add_worker_button(),
            self._create_remove_worker_button()
        ]

    def _create_end_turn_button(self) -> Button:
        image = pygame.image.load("./resources/graphics/buttons/end-turn.bmp")
        x = self.resolution[0] * 4 // 5
        y = self.resolution[1] * 5 // 6
        width = self.resolution[0] // 6
        height = self.resolution[0] // 8
        end_turn_button = Button((x, y), (width, height), image, self.game.end_turn)
        return end_turn_button

    def _create_add_worker_button(self) -> Button:
        image = pygame.image.load("./resources/graphics/buttons/add-worker.bmp")
        x = self.resolution[0] * 9 // 10
        y = self.resolution[1] * 2 // 8
        width = self.resolution[0] // 6
        height = self.resolution[0] // 8

        def add_worker_callback():
            return self.game.add_worker(self.game.selected_field)
        add_worker_button = Button((x, y), (width, height), image, add_worker_callback)
        return add_worker_button

    def _create_remove_worker_button(self) -> Button:
        image = pygame.image.load("./resources/graphics/buttons/remove-worker.bmp")
        x = self.resolution[0] * 9 // 10
        y = self.resolution[1] * 1 // 8
        width = self.resolution[0] // 6
        height = self.resolution[0] // 8

        def remove_worker_callback():
            return self.game.remove_worker(self.game.selected_field)
        remove_worker_button = Button((x, y), (width, height), image, remove_worker_callback)
        return remove_worker_button
