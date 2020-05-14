import logging
from typing import (
    Optional,
    Iterator
)

from treeline.engine.actor import Actor
from treeline.model.player import Player
from treeline.model.board import Board
from treeline.model.field import Field

LOGGER = logging.getLogger(__name__)


class Game:
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

        self._selected_field: Optional[Field] = None

        for field in self.board.get_all_fields():
            field.game = self

    def field_clicked(self, field: Field):
        if field is not self._selected_field:
            LOGGER.debug("Selected field (%d, %d)", field.position[0], field.position[1])
            self._selected_field = field
        else:
            pass  # manage the click in some other way

    def get_all_actors(self) -> Iterator[Actor]:
        yield from self.board.get_all_fields()
