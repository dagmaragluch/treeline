from __future__ import annotations
from enum import Enum
from typing import (
    Dict,
)


class ResourceType(Enum):
    food = 1
    wood = 2
    iron = 3


class Resources:
    def __init__(self, res_dict: Dict[ResourceType, int] = None):
        self._res = res_dict if res_dict is not None \
            else {resource_type: 0 for resource_type in ResourceType}

    def __add__(self, other: Resources) -> Resources:
        res_dict = {res_type: self._res[res_type] + other._res[res_type] for res_type in ResourceType}
        return Resources(res_dict=res_dict)

    def __sub__(self, other: Resources) -> Resources:
        res_dict = {res_type: self._res[res_type] - other._res[res_type] for res_type in ResourceType}
        for resource_amount in res_dict.values():
            if resource_amount < 0:
                raise NegativeResourceError

        return Resources(res_dict=res_dict)

    def __eq__(self, other: Resources):
        return self._res == other._res

    def __str__(self) -> str:
        return ", ".join([f"{res_type.name}: {res_amount}" for res_type, res_amount in self._res.items()])

    def get_resource(self, resource_type: ResourceType) -> int:
        return self._res[resource_type]

    def add_resource(self, resource_type: ResourceType, amount: int):
        self._res[resource_type] += amount

    def subtract_resource(self, resource_type: ResourceType, amount: int):
        difference = self._res[resource_type] - amount
        if difference < 0:
            raise NegativeResourceError
        self._res[resource_type] = difference


class NegativeResourceError(Exception):
    pass
