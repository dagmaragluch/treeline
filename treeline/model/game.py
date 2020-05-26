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
        self.set_start_field()

    def field_clicked(self, field: Field):
        if field is not self._selected_field:
            LOGGER.debug("Selected field (%d, %d)", field.position[0], field.position[1])
            self._selected_field = field
        else:
            pass  # manage the click in some other way

    def get_all_actors(self) -> Iterator[Actor]:
        yield from self.board.get_all_fields()

    def update_field_owner(self, field: Field):  # przy większej liczbie graczy dodać player jako parametr
        field.owner = self.player.player_number  # update ownera pola
        self.player.fields.append(field)  # dodanie pola do listy pól gracza

    def set_start_field(self):
        start_field = self.board.get_random_field()
        self.update_field_owner(start_field)

    ''' na razie sprawdza tylko czy pole, które gracz chce przejąć sąsiaduje z min 1 jego polem; 
        potem można dopisać więcej warunków, np. spr niezbędnej ilości zasobów'''

    def is_take_field_possible(self, field: Field) -> bool:
        neighbours = self.board.get_neighbours(field)
        for n in neighbours:
            if n.owner == self.player.player_number:
                return True
        return False

    def take_over_field(self, field: Field):
        if field.owner != self.player.player_number:  # pole nie należy do gracza
            if self.is_take_field_possible(field):  # pole spełnia warunki przejęcia
                self.update_field_owner(field)

    def end_turn(self):
        for player_field in self.player.fields:
            self.player.resources += player_field.get_resources()
