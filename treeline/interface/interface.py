from typing import Tuple, List, Iterable, Union

from treeline.model.game import Game
from treeline.model.building import Building
from treeline.model.building_config import BUILDING_STATS
from treeline.engine.widget import Widget
from treeline.interface.button import Button
from treeline.interface.label import Label
from treeline.interface.icon import Icon
from treeline.interface.resource_bar import ResourceBar
import pygame
import pygame.freetype
from treeline.model.sprite_config import sprites


class Interface:
    def __init__(self, game: Game, resolution: Tuple[int, int] = (1920, 1080)):
        self.game = game
        game.update_interface_callback = self._on_field_selected
        game.set_interface_lock = self.set_lock
        self.locked = True
        self.resolution = resolution
        self.font = pygame.freetype.SysFont("Comic Sans MS", 24)

        self._interface_bar = self._create_interface_bar()
        self._end_turn_button = self._create_end_turn_button()
        self._take_over_button = self._create_take_over_button()
        self._worker_buttons = self._create_worker_buttons()
        self._building_buttons = self._create_building_buttons()

        self._worker_counter = self._create_worker_counter()
        self._resource_bar = ResourceBar(self.font, game.local_player)

        self.widgets = [
            self._interface_bar,
            self._end_turn_button,
            self._take_over_button,
            *self._worker_buttons,
            *self._building_buttons,
            self._resource_bar,
            self._worker_counter,
        ]

        self._on_field_selected()

    def _on_field_selected(self):
        self._hide_all_context_buttons()
        if self.locked:
            self._hide_widgets(self._end_turn_button)
            return
        self._show_widgets(self._end_turn_button)
        selected_field = self.game.selected_field
        if not selected_field:
            return

        if selected_field.owner != self.game.active_player.player_number:
            self._show_widgets(self._take_over_button)
            return

        if selected_field.building:
            self._show_widgets(self._worker_buttons)
            self._show_widgets(self._worker_counter)
            self._worker_counter.text = self._get_worker_counter_text(selected_field.building)
            return
        else:
            self._show_widgets(self._building_buttons)
            return

    def _create_interface_bar(self) -> Icon:
        x = 0
        y = self.resolution[1] * 9 // 10
        return Icon((x, y), sprites["bar_button"])

    def _create_end_turn_button(self) -> Button:
        x = self.resolution[0] * 85 // 100
        y = self.resolution[1] * 93 // 100

        return Button((x, y), sprites["end_turn_button"], self.game.end_turn)

    def _create_take_over_button(self):
        x = self.resolution[0] * 2 // 10
        y = self.resolution[1] * 93 // 100

        def take_over_callback():
            return self.game.take_over_field(self.game.selected_field)

        return Button((x, y), sprites["take_over_button"], take_over_callback)

    def _create_worker_buttons(self) -> List[Button]:
        x = self.resolution[0] * 25 // 100
        y = self.resolution[1] * 93 // 100

        def add_worker_callback():
            return self.game.add_worker(self.game.selected_field)
        add_worker_button = Button((x, y), sprites["add_worker_button"], add_worker_callback)

        x = self.resolution[0] * 3 // 10
        y = self.resolution[1] * 93 // 100

        def remove_worker_callback():
            return self.game.remove_worker(self.game.selected_field)
        remove_worker_button = Button((x, y), sprites["remove_worker_button"], remove_worker_callback)

        return [add_worker_button, remove_worker_button]

    def _create_worker_counter(self) -> Label:
        x = self.resolution[0] * 35 // 100
        y = self.resolution[1] * 95 // 100
        return Label((x, y), self.font)

    @staticmethod
    def _get_worker_counter_text(building: Building):
        return f"{building.workers} / {building.max_workers}"

    def _create_building_buttons(self) -> List[Button]:
        build_buttons = []
        for i, building_type in enumerate(BUILDING_STATS):
            if building_type == "townhall":  # cannot build townhall
                continue
            image = sprites[f"{building_type}_button"]
            x = self.resolution[0] * 1//10 + 100 * i
            y = self.resolution[1] * 95 // 100

            build_button = Button((x, y), image, self._build_callback_wrapper(building_type))
            build_buttons.append(build_button)

        return build_buttons

    def _build_callback_wrapper(self, building_type) -> callable:
        def build_callback():
            return self.game.build(self.game.selected_field, building_type)
        return build_callback

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
        self._hide_widgets(self._worker_counter)
        self._hide_widgets(self._building_buttons)

    def set_lock(self, lock: bool):
        self.locked = lock
