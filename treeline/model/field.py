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

terrain_shape_mapping = {
    Terrain.grass: Hexagon(color=(82, 235, 52)),
    Terrain.forest: Hexagon(color=(21, 117, 2)),
    Terrain.mountain: Hexagon(color=(97, 77, 50))
}


class Field(Actor):
    def __init__(
            self,
            position: Tuple[int, int],
            terrain: Terrain,
            building: Building = None,
            owner: int = 0,
            game=None
    ):
        shape = terrain_shape_mapping[terrain]
        Actor.__init__(self, position, shape)
        self.terrain = terrain
        self.building = building
        self.owner = owner
        self.game = game

    def get_resources(self) -> Resources:
        produced_resources = Resources()
        if self.terrain == Terrain.grass:
            produced_resources.add_resource(ResourceType.food, 2)
        elif self.terrain == Terrain.forest:
            produced_resources.add_resource(ResourceType.food, 1)
            produced_resources.add_resource(ResourceType.wood, 2)
        elif self.terrain == Terrain.mountain:
            produced_resources.add_resource(ResourceType.iron, 1)

        produced_resources += self.building.get_resources()
        return produced_resources

    def on_pressed(self):
        LOGGER.debug("Field with position (%d, %d) clicked", self.position[0], self.position[1])
        self.game.field_clicked(self)
