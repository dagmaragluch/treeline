from enum import Enum
from typing import (
    Tuple,
)

from treeline.model.resource import Resources
from treeline.model.resource import ResourceType
from treeline.engine.actor import Actor


class Terrain(Enum):
    grass = 1
    forest = 2
    mountain = 3


class Field(Actor):
    def __init__(
            self,
            position: Tuple[int, int],
            terrain: Terrain
    ):
        Actor.__init__(self, position)
        self.terrain = terrain

    def get_resources(self) -> Resources:
        produced_resources = Resources()
        if self.terrain == Terrain.grass:
            produced_resources.add_resource(ResourceType.food, 2)
        elif self.terrain == Terrain.forest:
            produced_resources.add_resource(ResourceType.food, 1)
            produced_resources.add_resource(ResourceType.wood, 2)
        elif self.terrain == Terrain.mountain:
            produced_resources.add_resource(ResourceType.iron, 1)

        return produced_resources
