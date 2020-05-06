from enum import Enum

from treeline.model.resource import Resources
from treeline.model.resource import ResourceType


class Terrain(Enum):
    grass = 1
    forest = 2
    mountain = 3


class Field:
    def __init__(self, terrain: Terrain):
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
