import logging
from typing import (
    Tuple,
)

from treeline.model.terrain import Terrain
from treeline.model.resource import Resources
from treeline.model.resource import ResourceType
from treeline.engine.actor import Actor
from treeline.model.building import Building
from treeline.model.field_config import hexagons
from treeline.model.resource_config import resources_per_turn as config_per_turn
from treeline.model.resource_config import resources_limit as config_limit
from treeline.model.resource_config import prices_increase as config_prices

LOGGER = logging.getLogger(__name__)


class Field(Actor):
    def __init__(
            self,
            position: Tuple[int, int],
            terrain: Terrain,
            building: Building = None,
            owner: int = 0
    ):
        shape = hexagons[terrain.name]
        Actor.__init__(self, position, shape)
        self.terrain = terrain
        self.building = building
        self._owner = owner
        self.price = {ResourceType.food: 5, ResourceType.wood: 0, ResourceType.iron: 1}
        self.limit = config_limit[terrain.name]
        self.click_callback = None

    def get_resources(self) -> Resources:
        produced_resources = Resources()
        for res_type in ResourceType:
            produced_resources.add_resource(res_type, config_per_turn[self.terrain.name][res_type])

        if self.building:
            produced_resources += self.building.get_resources()
        return produced_resources

    def change_price_when_take_over(self):
        for res_type in ResourceType:
            self.price[res_type] += config_prices["take_over"][res_type]

    def change_price_when_neighbour_if_defensive_building(self):
        for res_type in ResourceType:
            self.price[res_type] += config_prices["by_defense"][res_type]

    def on_pressed(self):
        LOGGER.debug("Field with position (%d, %d) clicked", self.position[0], self.position[1])
        self.click_callback(self)

    def highlight(self):
        self.shape = hexagons[f"{self.terrain.name}_highlight"]

    def highlight_off(self):
        self.shape = hexagons[self.terrain.name]

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self.shape = hexagons["grass_red"]  # TODO update textures here
        self._owner = owner
