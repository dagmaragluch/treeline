import logging
from typing import (
    Tuple,
)

from treeline.model.terrain import Terrain
from treeline.model.resource import Resources
from treeline.model.resource import ResourceType
from treeline.engine.actor import Actor
from treeline.model.building import Building
from treeline.misc.shapes import Hexagon

LOGGER = logging.getLogger(__name__)

hexagons = {
    "grass": Hexagon(color=(82, 235, 52)),
    "grass_highlight": Hexagon(color=(102, 255, 72)),
    "forest": Hexagon(color=(21, 117, 2)),
    "forest_highlight": Hexagon(color=(41, 137, 22)),
    "mountain": Hexagon(color=(97, 77, 50)),
    "mountain_highlight": Hexagon(color=(117, 97, 70))
}


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
        self.owner = owner
        self.click_callback = None

    def get_resources(self) -> Resources:
        produced_resources = Resources()
        if self.terrain == Terrain.grass:
            produced_resources.add_resource(ResourceType.food, 2)
        elif self.terrain == Terrain.forest:
            produced_resources.add_resource(ResourceType.food, 1)
            produced_resources.add_resource(ResourceType.wood, 2)
        elif self.terrain == Terrain.mountain:
            produced_resources.add_resource(ResourceType.iron, 1)

        if self.building:
            produced_resources += self.building.get_resources()
        return produced_resources

    def on_pressed(self):
        LOGGER.debug("Field with position (%d, %d) clicked", self.position[0], self.position[1])
        self.click_callback(self)

    def highlight(self):
        self.shape = hexagons[f"{self.terrain.name}_highlight"]

    def highlight_off(self):
        self.shape = hexagons[self.terrain.name]
