from typing import (
    Optional
)

from treeline.model.player import Player
from treeline.model.board import Board
from treeline.model.field import Field


class Game:
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

        self._selected_field: Optional[Field] = None

        for field in self.board.get_all_fields():
            field.game = self

    def field_clicked(self, field: Field):
        if field is not self._selected_field:
            self._selected_field = field
        else:
            pass  # manage the click in some other way
