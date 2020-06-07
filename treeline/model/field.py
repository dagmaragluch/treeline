import logging
from typing import (
    Tuple,
    Optional
)

from treeline.model.terrain import Terrain
from treeline.model.resource import Resources, NegativeResourceError
from treeline.engine.actor import Actor
from treeline.model.building import Building
from treeline.model.resource_config import resources_per_turn
from treeline.model.resource_config import resources_limit
from treeline.model.resource_config import field_prices
from treeline.model.sprite_config import sprites

LOGGER = logging.getLogger(__name__)


class Field(Actor):
    def __init__(
            self,
            position: Tuple[int, int],
            terrain: Terrain,
            building: Building = None,
            owner: Optional[int] = None
    ):
        shape = sprites[terrain.name]
        Actor.__init__(self, position, shape)
        self.terrain = terrain
        self.building = building
        self._owner = owner
        self.price = Resources.from_dictionary(field_prices["neutral"])
        self.available_resources = Resources.from_dictionary(resources_limit[terrain.name])
        self.click_callback = None

    def get_resources(self) -> Resources:
        produced_resources = Resources()
        produced_resources += Resources.from_dictionary(resources_per_turn[self.terrain.name])
        if self.building:
            produced_resources += self.building.get_resources()

        try:
            self.available_resources -= produced_resources
        except NegativeResourceError:
            remaining_resources = self.available_resources.get_remaining(required=produced_resources)
            self.available_resources -= remaining_resources
            produced_resources = remaining_resources

        return produced_resources

    def change_price_when_take_over(self):
        self.price = Resources.from_dictionary(field_prices["take_over"])

    def change_price_when_neighbour_if_defensive_building(self):
        self.price = Resources.from_dictionary(field_prices["defended"])

    def on_pressed(self):
        LOGGER.debug("Field with position (%d, %d) clicked", self.position[0], self.position[1])
        self.click_callback(self)

    def highlight(self):
        self.shape = sprites[f"{self.terrain.name}_highlight"]

    def highlight_off(self):
        self.shape = sprites[self.terrain.name]

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        #self.shape = hexagons["grass_red"]  # TODO update textures here
        self._owner = owner
