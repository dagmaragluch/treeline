from typing import Tuple, List, Iterable, Union

from treeline.model.game import Game
from treeline.model.building_config import BUILDING_STATS
from treeline.engine.widget import Widget
from treeline.interface.button import Button
import pygame


class Interface:
    def __init__(self, game: Game, resolution: Tuple[int, int] = (1920, 1080)):
        self.game = game
        game.selected_field_interface_callback = self._on_field_selected
        self.resolution = resolution

        self._end_turn_button = self._create_end_turn_button()
        self._take_over_button = self._create_take_over_button()
        self._worker_buttons = self._create_worker_buttons()
        self._building_buttons = self._create_building_buttons()

        self.widgets = [
            self._end_turn_button,
            self._take_over_button,
            *self._worker_buttons,
            *self._building_buttons,
        ]

        self._on_field_selected()

    def _on_field_selected(self):
        self._hide_all_context_buttons()
        selected_field = self.game.selected_field
        if not selected_field:
            return

        if selected_field.owner != self.game.active_player.player_number:
            self._show_widgets(self._take_over_button)
            return

        if selected_field.building:
            self._show_widgets(self._worker_buttons)
            return
        else:
            self._show_widgets(self._building_buttons)
            return

    def _create_end_turn_button(self) -> Button:
        image = pygame.image.load("./resources/graphics/buttons/end-turn.bmp")
        x = self.resolution[0] * 4 // 5
        y = self.resolution[1] * 9 // 10

        return Button((x, y), image, self.game.end_turn)

    def _create_take_over_button(self):
        image = pygame.image.load("./resources/graphics/buttons/take_over.bmp")
        x = self.resolution[0] * 7 // 10
        y = self.resolution[1] * 9 // 10

        def take_over_callback():
            return self.game.take_over_field(self.game.selected_field)

        return Button((x, y), image, take_over_callback)

    def _create_worker_buttons(self) -> List[Button]:
        add_image = pygame.image.load("./resources/graphics/buttons/add-worker.bmp")
        x = self.resolution[0] * 9 // 10
        y = self.resolution[1] * 2 // 8

        def add_worker_callback():
            return self.game.add_worker(self.game.selected_field)
        add_worker_button = Button((x, y), add_image, add_worker_callback)

        remove_image = pygame.image.load("./resources/graphics/buttons/remove-worker.bmp")
        x = self.resolution[0] * 9 // 10
        y = self.resolution[1] * 1 // 8

        def remove_worker_callback():
            return self.game.remove_worker(self.game.selected_field)
        remove_worker_button = Button((x, y), remove_image, remove_worker_callback)

        return [add_worker_button, remove_worker_button]

    def _create_building_buttons(self) -> List[Button]:
        build_buttons = []
        for i, building_type in enumerate(BUILDING_STATS):
            image = pygame.image.load(f"./resources/graphics/buttons/{building_type}.png")
            x = self.resolution[0] * 1//10 + 100 * i
            y = self.resolution[1] * 9 // 10

            def build_callback():
                return self.game.build(self.game.selected_field, building_type)

            build_button = Button((x, y), image, build_callback)
            build_buttons.append(build_button)

        return build_buttons

    @staticmethod
    def _show_widgets(widgets: Union[Widget, Iterable[Widget]]):
        try:
            iter(widgets)
            for widget in widgets:
                widget.visible = True
        except TypeError:
            widgets.visible = True

    @staticmethod
    def _hide_widgets(widgets: Union[Widget, Iterable[Widget]]):
        try:
            iter(widgets)
            for widget in widgets:
                widget.visible = False
        except TypeError:
            widgets.visible = False

    def _hide_all_context_buttons(self):
        self._hide_widgets(self._take_over_button)
        self._hide_widgets(self._worker_buttons)
        self._hide_widgets(self._building_buttons)
