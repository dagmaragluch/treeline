from typing import (
    Tuple,
)

from treeline.model.terrain import Terrain
from treeline.model.resource import Resources
from treeline.model.resource import ResourceType
from treeline.engine.actor import Actor
from treeline.model.building import Building


class Field(Actor):
    def __init__(
            self,
            position: Tuple[int, int],
            terrain: Terrain,
            building: Building = None,
            game=None
    ):
        Actor.__init__(self, position)
        self.terrain = terrain
        self.building = building
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
        self.game.field_clicked(self)
