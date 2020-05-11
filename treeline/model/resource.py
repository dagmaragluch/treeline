from __future__ import annotations
from enum import Enum
from typing import (
    Dict,
)


class ResourceType(Enum):
    food = 1
    wood = 2
    iron = 3


ResourceDict = Dict[ResourceType, int]


class Resources:
    def __init__(self, res_dict=None):
        if res_dict is None:
            self._resource_dict = {resource_type: 0 for resource_type in ResourceType}
        else:
            self._resource_dict = res_dict

    def __add__(self, other: Resources) -> Resources:
        res_dict = {
            res_type: self._resource_dict[res_type] + other._resource_dict[res_type]
            for res_type in ResourceType
        }
        return Resources(res_dict=res_dict)

    def __sub__(self, other: Resources) -> Resources:
        res_dict = {
            res_type: self._resource_dict[res_type] - other._resource_dict[res_type]
            for res_type in ResourceType
        }
        for resource_amount in res_dict.values():
            if resource_amount < 0:
                raise NegativeResourceError

        return Resources(res_dict=res_dict)

    def __eq__(self, other: Resources):
        return self._resource_dict == other._resource_dict

    def __str__(self) -> str:
        return ", ".join([f"{res_type.name}: {res_amount}" for res_type, res_amount in self._resource_dict.items()])

    def get_resource(self, resource_type: ResourceType) -> int:
        return self._resource_dict[resource_type]

    def add_resource(self, resource_type: ResourceType, amount: int):
        self._resource_dict[resource_type] += amount

    def subtract_resource(self, resource_type: ResourceType, amount: int):
        difference = self._resource_dict[resource_type] - amount
        if difference < 0:
            raise NegativeResourceError
        self._resource_dict[resource_type] = difference

    @staticmethod
    def from_dictionary(dictionary: Dict[str, int]) -> Resources:
        res = Resources()
        for resource_name, amount in dictionary.items():
            res.add_resource(ResourceType[resource_name], amount)

        return res


class NegativeResourceError(Exception):
    pass
