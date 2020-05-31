import logging
from typing import (
    Optional,
    Iterator,
    Callable,
    List
)

from treeline.engine.actor import Actor
from treeline.model.player import Player
from treeline.model.board import Board
from treeline.model.field import Field
from treeline.Network.receiver import Receiver

LOGGER = logging.getLogger(__name__)


class Game:
    def __init__(self, board: Board, players: List[Player]):
        self.board = board
        self.players = players
        self._active_player = players[0]
        self._active_player_index = 0

        self._selected_field: Optional[Field] = None

        for field in self.board.get_all_fields():
            field.click_callback = self._field_clicked
        self._set_start_fields()

        self.decorators = Game.Decorators(self.board.get_field)

    def _field_clicked(self, field: Field):
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

    @staticmethod
    def _update_field_owner(field: Field, player: Player):
        field.owner = player.player_number  # update ownera pola
        player.fields.append(field)  # dodanie pola do listy pól gracza

    def _set_start_fields(self):
        taken_fields = []
        for player in self.players:
            start_field = self.board.get_random_field()
            while start_field in taken_fields:
                start_field = self.board.get_random_field()
            taken_fields.append(start_field)
            self._update_field_owner(start_field, player)

    ''' na razie sprawdza tylko czy pole, które gracz chce przejąć sąsiaduje z min 1 jego polem; 
        potem można dopisać więcej warunków, np. spr niezbędnej ilości zasobów'''

    def _is_take_field_possible(self, field: Field, player: Player) -> bool:
        if field.owner == player.player_number:  # pole należy do gracza
            return False

        neighbours = self.board.get_neighbours(field)
        for n in neighbours:
            if n.owner == player.player_number:
                return True
        return False

    def take_over_field(self, field: Field):
        if self._is_take_field_possible(field, self._active_player):  # pole spełnia warunki przejęcia
            self._update_field_owner(field, self._active_player)

    def end_turn(self):
        LOGGER.info("End turn for player %d", self._active_player.player_number)
        for player_field in self._active_player.fields:
            self._active_player.resources += player_field.get_resources()

        self._active_player_index = (self._active_player_index + 1) % len(self.players)
        self._active_player = self.players[self._active_player_index]
        LOGGER.info("Next turn for player %d", self._active_player.player_number)

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
