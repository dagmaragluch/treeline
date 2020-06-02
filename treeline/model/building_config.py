from treeline.model.field import Terrain


BUILDING_STATS = {
    "farm": {
        "cost": {
            "wood": 10,
        },
        "max_workers": 10,
        "valid_terrains": [Terrain.grass],
    },
    "sawmill": {
        "cost": {
            "wood": 10,
        },
        "max_workers": 5,
        "valid_terrains": [Terrain.forest],
    },
    "iron_mine": {
        "cost": {
            "wood": 20,
        },
        "max_workers": 8,
        "valid_terrains": [Terrain.mountain],
    },
    "town_hall": {
        "cost": {
            "wood": 0,
        },
        "max_workers": 0,
        "valid_terrains": [Terrain.grass, Terrain.forest, Terrain.mountain],
    },
    "house": {
        "cost": {
            "food": 10,
        },
        "max_workers": 2,
        "valid_terrains": [Terrain.grass, Terrain.forest, Terrain.mountain],
    },
}
