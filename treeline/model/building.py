from random import random
from typing import (
    List,
    Tuple
)

from treeline.model.resource import (
    Resources,
)
from treeline.model.field import Terrain
from treeline.model import building_config as config
from treeline.engine.actor import Actor
from treeline.engine.shapes.sprite import Sprite
from treeline.model.sprite_config import sprites


class Building(Actor):
    def __init__(
            self,
            cost: Resources,
            valid_terrains: List[Terrain],
            position: Tuple[int, int],
            sprite: Sprite,
    ):
        self.cost = cost
        self.valid_terrains = valid_terrains
        self.workers = 0
        self.max_workers = 0
        Actor.__init__(self, position, sprite)

    def get_resources(self) -> Resources:
        return Resources()

    def add_workers(self, amount: int) -> bool:
        return False

    def subtract_workers(self, amount: int) -> bool:
        return False

    def can_make_child(self) -> bool:
        return False

    def get_number_of_workers(self) -> int:
        return 0


class ProductionBuilding(Building):
    def __init__(
            self,
            cost: Resources,
            valid_terrains: List[Terrain],
            max_workers: int,
            position: Tuple[int, int],
            sprite: Sprite,
    ):
        Building.__init__(self, cost, valid_terrains, position, sprite)
        self.max_workers = max_workers
        self.workers = 0

    def add_workers(self, amount: int) -> bool:
        total_workers = self.workers + amount
        if total_workers > self.max_workers:
            return False
        self.workers = total_workers
        return True

    def subtract_workers(self, amount: int) -> bool:
        total_workers = self.workers - amount
        if total_workers < 0:
            return False
        self.workers = total_workers
        return True

    def get_number_of_workers(self) -> int:
        return self.workers


class DefensiveBuilding(Building):
    def __init__(
            self,
            cost: Resources,
            valid_terrains: List[Terrain],
            position: Tuple[int, int],
            sprite: Sprite,
    ):
        Building.__init__(self, cost, valid_terrains, position, sprite)
        self.cost = cost
        self.valid_terrains = valid_terrains


class Farm(ProductionBuilding):
    def __init__(self, position: Tuple[int, int]):
        stats = config.BUILDING_STATS["farm"]
        ProductionBuilding.__init__(self, position=position, sprite=sprites["farm"], **stats)

    def get_resources(self) -> Resources:
        food_produced = self.workers * 1
        return Resources.from_dictionary({"food": food_produced})


class Sawmill(ProductionBuilding):
    def __init__(self, position: Tuple[int, int]):
        stats = config.BUILDING_STATS["sawmill"]
        ProductionBuilding.__init__(self, position=position, sprite=sprites["sawmill"], **stats)

    def get_resources(self) -> Resources:
        wood_produced = self.workers * 2
        return Resources.from_dictionary({"wood": wood_produced})


class IronMine(ProductionBuilding):
    def __init__(self, position: Tuple[int, int]):
        stats = config.BUILDING_STATS["iron_mine"]
        ProductionBuilding.__init__(self, position=position, sprite=sprites["iron_mine"], **stats)

    def get_resources(self) -> Resources:
        iron_produced = self.workers * 1
        return Resources.from_dictionary({"iron": iron_produced})


class House(ProductionBuilding):
    def __init__(self, position: Tuple[int, int]):
        stats = config.BUILDING_STATS["house"]
        ProductionBuilding.__init__(self, position=position, sprite=sprites["house"], **stats)

    def can_make_child(self) -> bool:
        if self.workers == 2:
            return random.choice([True, False])


class TownHall(DefensiveBuilding):
    def __init__(self, position: Tuple[int, int]):
        stats = config.BUILDING_STATS["townhall"]
        DefensiveBuilding.__init__(self, position=position, sprite=sprites["townhall"], **stats)


class Tower(DefensiveBuilding):
    def __init__(self, position: Tuple[int, int]):
        stats = config.BUILDING_STATS["tower"]
        DefensiveBuilding.__init__(self, position=position, sprite=sprites["tower"], **stats)


building_types = {
    "farm": Farm,
    "sawmill": Sawmill,
    "iron_mine": IronMine,
    "house": House,
    "townhall": TownHall,
    "tower": Tower,
}
