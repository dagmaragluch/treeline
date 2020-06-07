from treeline.model.field import Terrain
from treeline.model.resource import Resources
from treeline.engine.shapes.sprite import Sprite
import pygame

BUILDING_STATS = {
    "farm": {
        "cost": Resources.from_dictionary({
            "wood": 10,
        }),
        "max_workers": 10,
        "valid_terrains": [Terrain.grass],
    },
    "sawmill": {
        "cost": Resources.from_dictionary({
            "wood": 10,
        }),
        "max_workers": 5,
        "valid_terrains": [Terrain.forest],
    },
    "iron_mine": {
        "cost": Resources.from_dictionary({
            "wood": 10,
        }),
        "max_workers": 8,
        "valid_terrains": [Terrain.mountain],
    },
    "house": {
        "cost": Resources.from_dictionary({
            "wood": 10,
        }),
        "max_workers": 2,
        "valid_terrains": [Terrain.grass, Terrain.forest, Terrain.mountain],
    },
    "townhall": {
        "cost": Resources(),
        "valid_terrains": [Terrain.grass, Terrain.forest, Terrain.mountain],
    },
    "tower": {
        "cost": Resources.from_dictionary({
            "wood": 10,
        }),
        "valid_terrains": [Terrain.grass, Terrain.forest, Terrain.mountain],
    },
}
