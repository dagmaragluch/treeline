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
            building_type: int,
            cost: Resources,
            valid_terrains: List[Terrain]
    ):
        self.building_type = building_type
        self.cost = cost
        self.valid_terrains = valid_terrains


class ProducesBuilding(Building):
    def __init__(
            self,
            building_type: int,
            cost: Resources,
            valid_terrains: List[Terrain],
            max_workers: int,
    ):
        Building.__init__(self, building_type, cost, valid_terrains)
        self.building_type = 1
        self.max_workers = max_workers
        self.workers = 0

    def get_resources(self) -> Resources:
        raise NotImplementedError

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


class DefensiveBuilding(Building):
    def __init__(
            self,
            building_type: int,
            cost: Resources,
            valid_terrains: List[Terrain]
    ):
        self.building_type = 2,
        self.cost = cost
        self.valid_terrains = valid_terrains


class Farm(ProducesBuilding):
    def __init__(self):
        stats = config.BUILDING_STATS["farm"]
        cost = Resources.from_dictionary(stats["cost"])
        max_workers = stats["max_workers"]
        valid_terrains = stats["valid_terrains"]
        ProducesBuilding.__init__(self, cost, max_workers, valid_terrains)

    def get_resources(self) -> Resources:
        resources = Resources()
        food_produced = self.workers * 1
        resources.add_resource(ResourceType.food, food_produced)
        return resources


class Sawmill(ProducesBuilding):
    def __init__(self):
        stats = config.BUILDING_STATS["sawmill"]
        cost = Resources.from_dictionary(stats["cost"])
        max_workers = stats["max_workers"]
        valid_terrains = stats["valid_terrains"]
        ProducesBuilding.__init__(self, cost, max_workers, valid_terrains)

    def get_resources(self) -> Resources:
        resources = Resources()
        wood_produced = self.workers * 2
        resources.add_resource(ResourceType.wood, wood_produced)
        return resources


class IronMine(ProducesBuilding):
    def __init__(self):
        stats = config.BUILDING_STATS["iron_mine"]
        cost = Resources.from_dictionary(stats["cost"])
        max_workers = stats["max_workers"]
        valid_terrains = stats["valid_terrains"]
        ProducesBuilding.__init__(self, cost, max_workers, valid_terrains)

    def get_resources(self) -> Resources:
        resources = Resources()
        iron_produced = self.workers * 1
        resources.add_resource(ResourceType.iron, iron_produced)
        return resources


class TownHall(DefensiveBuilding):
    def __init__(self):
        stats = config.BUILDING_STATS["town_hall"]
        cost = Resources.from_dictionary(stats["cost"])
        valid_terrains = stats["valid_terrains"]
        DefensiveBuilding.__init__(self, 2, cost, valid_terrains)


building_types = {
    "farm": Farm,
    "sawmill": Sawmill,
    "iron_mine": IronMine,
    "town_hall": TownHall,
}
