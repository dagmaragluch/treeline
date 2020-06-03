import logging
from typing import (
    Tuple,
)

from treeline.model.terrain import Terrain
from treeline.model.resource import Resources
from treeline.model.resource import ResourceType
from treeline.glengine.actor import Actor
from treeline.model.building import Building
from treeline.glengine.shape import Splash
import pygame

LOGGER = logging.getLogger(__name__)
hexagons = {
    "grass": Splash(pygame.image.load("./resources/graphics/terrain/grass.png")),
    "grass_highlight": None,
    "grass_red": None,
    "forest": Splash(pygame.image.load("./resources/graphics/terrain/forest.png")),
    "forest_highlight": None,
    "mountain": Splash(pygame.image.load("./resources/graphics/terrain/mountain.png")),
    "mountain_highlight": None
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
        self._owner = owner
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

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        self.shape = hexagons["grass_red"]  # TODO update textures here
        self._owner = owner
