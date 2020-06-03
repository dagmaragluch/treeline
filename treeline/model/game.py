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
from treeline.model.building import building_types
from treeline.model.resource import NegativeResourceError
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
        self.build("sawmill", board.get_field(0, 0))

    def build(self, building_type: str, field: Field) -> bool:
        if field not in self._active_player.fields:
            LOGGER.debug("Cannot build. Field (%d, %d) does not belong to active player",
                         field.position[0], field.position[1])
            return False

        building = building_types[building_type]()
        try:
            self._active_player.resources -= building.cost
        except NegativeResourceError:
            LOGGER.debug("Not enough resources to build %s", building_type)
            return False

        field.building = building
        self.update_fields_price(building_type, field)
        LOGGER.debug("%s built on field (%d, %d)", building_type, field.position[0], field.position[1])
        return True

    # increase in the price of field with tower and its neighbours
    def update_fields_price(self, building_type: str, field: Field):
        if building_type == "tower" or building_type == "town_hall":
            fields_to_update = self.board.get_neighbours(field)
            fields_to_update.append(field)
            for f in fields_to_update:
                f.change_price_when_neighbour_if_defensive_building()

    def add_worker(self, field: Field) -> bool:
        if not field.building:
            LOGGER.debug("Cannot add workers to field with no building")
            return False
        if self._active_player.available_workers <= 0:
            LOGGER.debug("No available workers")
            return False
        successful = field.building.add_workers(1)
        if not successful:
            LOGGER.debug("Cannot add worker to field (%d, %d)", field.position[0], field.position[1])
            return False
        self._active_player.available_workers -= 1
        LOGGER.debug("Added worker to field (%d, %d)", field.position[0], field.position[1])
        return True

    def remove_worker(self, field: Field) -> bool:
        if not field.building:
            LOGGER.debug("Cannot remove workers to field with no building")
            return False
        successful = field.building.subtract_workers(1)
        if not successful:
            LOGGER.debug("Cannot remove worker from field (%d, %d)", field.position[0], field.position[1])
            return False
        self._active_player.available_workers += 1
        LOGGER.debug("Removed worker from field (%d, %d)", field.position[0], field.position[1])
        return True

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
            start_field.building = building_types["town_hall"]()  # build town hall on start field
            self.update_fields_price("town_hall", start_field)
            LOGGER.debug("town_hall built on field (%d, %d)", start_field.position[0], start_field.position[1])

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

    def take_over_field(self, field: Field) -> bool:
        if self._is_take_field_possible(field, self._active_player):  # field borders with 1 player's field
            try:
                for r, p in field.price.items():  # check player resources
                    self._active_player.resources.subtract_resource(r, p)
            except NegativeResourceError:
                LOGGER.debug("Not enough resources to take over field %d, %d", field.position[0], field.position[1])
                return False

            if field.owner == 0:  # if before field had not owner -> change price
                field.change_price_when_take_over()

            self._update_field_owner(field, self._active_player)
            LOGGER.debug("Player %d take over field %d, %d", self._active_player.player_number, field.position[0],
                         field.position[1])
            return True

    def end_turn(self):
        LOGGER.info("End turn for player %d", self._active_player.player_number)
        for player_field in self._active_player.fields:
            self._active_player.resources += player_field.get_resources()

            if player_field.building.can_make_child():  # try to make new worker
                self._active_player.total_workers += 1
                self._active_player.available_workers += 1

        self._active_player_index = (self._active_player_index + 1) % len(self.players)
        self._active_player = self.players[self._active_player_index]
        LOGGER.info("Next turn for player %d", self._active_player.player_number)

    @property
    def selected_field(self):
        return self._selected_field

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
