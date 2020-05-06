from typing import (
    List
)

from treeline.model.resource import (
    Resources,
    ResourceType,
)
from treeline.model.field import Terrain
from treeline.model import building_config as config


class Building:
    def __init__(
            self,
            cost: Resources,
            max_workers: int,
            valid_terrains: List[Terrain]
    ):
        self.cost = cost
        self.max_workers = max_workers
        self.valid_terrains = valid_terrains
        self.workers = 0

    def get_resources(self) -> Resources:
        raise NotImplementedError

    def add_workers(self, amount: int) -> bool:
        total_workers = self.workers + amount
        if total_workers > self.max_workers:
            return False
        return True

    def subtract_workers(self, amount: int) -> bool:
        total_workers = self.workers - amount
        if total_workers < 0:
            return False
        return True


class Farm(Building):
    def __init__(self):
        stats = config.BUILDING_STATS["farm"]
        cost = Resources.from_dictionary(stats["cost"])
        max_workers = stats["max_workers"]
        valid_terrains = stats["valid_terrains"]
        Building.__init__(self, cost, max_workers, valid_terrains)

    def get_resources(self) -> Resources:
        resources = Resources()
        food_produced = self.workers * 1
        resources.add_resource(ResourceType.food, food_produced)
        return resources


class Sawmill(Building):
    def __init__(self):
        stats = config.BUILDING_STATS["farm"]
        cost = Resources.from_dictionary(stats["cost"])
        max_workers = stats["max_workers"]
        valid_terrains = stats["valid_terrains"]
        Building.__init__(self, cost, max_workers, valid_terrains)

    def get_resources(self) -> Resources:
        resources = Resources()
        wood_produced = self.workers * 2
        resources.add_resource(ResourceType.wood, wood_produced)
        return resources


class IronMine(Building):
    def __init__(self):
        stats = config.BUILDING_STATS["farm"]
        cost = Resources.from_dictionary(stats["cost"])
        max_workers = stats["max_workers"]
        valid_terrains = stats["valid_terrains"]
        Building.__init__(self, cost, max_workers, valid_terrains)

    def get_resources(self) -> Resources:
        resources = Resources()
        iron_produced = self.workers * 1
        resources.add_resource(ResourceType.iron, iron_produced)
        return resources
