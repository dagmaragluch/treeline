import logging
from typing import (
    Optional,
    Iterator,
    Callable
)

from treeline.engine.actor import Actor
from treeline.model.player import Player
from treeline.model.board import Board
from treeline.model.field import Field
from treeline.Network.receiver import Receiver

LOGGER = logging.getLogger(__name__)


class Game:
    def __init__(self, board: Board, player: Player):
        self.board = board
        self.player = player

        self._selected_field: Optional[Field] = None

        for field in self.board.get_all_fields():
            field.game = self
        self.set_start_field()

        self.decorators = Game.Decorators(self.board.get_field)

    def field_clicked(self, field: Field):
        if field is not self._selected_field:
            LOGGER.debug("Selected field (%d, %d)", field.position[0], field.position[1])
            field.highlight()
            if self._selected_field:
                self._selected_field.highlight_off()
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
        LOGGER.info("End turn")
        for player_field in self.player.fields:
            self.player.resources += player_field.get_resources()

    class Decorators:
        def __init__(self, get_field_function: Callable):
            self._get_field_function = get_field_function

        def coords_to_field(self, function: Callable):
            """Wrap function requiring field parameter into a function requiring (x,y) coordinates"""
            def wrapper(x: int, y: int):
                field = self._get_field_function(x, y)
                return function(field)
            return wrapper

    def add_receiver_callbacks(self, receiver: Receiver):
        receiver.callbacks["TAKE"] = self.decorators.coords_to_field(self.take_over_field)
