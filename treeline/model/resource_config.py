from treeline.model.resource import Resources, ResourceType

STARTING_RESOURCES = {
    "food": 100,
    "wood": 100,
    "iron": 50,
}
resources_per_turn = {
    "grass": {
        ResourceType.food: 2,
        ResourceType.wood: 0,
        ResourceType.iron: 0,
    },
    "forest": {
        ResourceType.food: 1,
        ResourceType.wood: 2,
        ResourceType.iron: 0,
    },
    "mountain": {
        ResourceType.food: 0,
        ResourceType.wood: 0,
        ResourceType.iron: 1,
    }
}

resources_limit = {
    "grass": {
        ResourceType.food: 100,
        ResourceType.wood: 0,
        ResourceType.iron: 0,
    },
    "forest": {
        ResourceType.food: 100,
        ResourceType.wood: 50,
        ResourceType.iron: 0,
    },
    "mountain": {
        ResourceType.food: 0,
        ResourceType.wood: 0,
        ResourceType.iron: 100,
    }
}

prices_increase = {
    "take_over": {
        ResourceType.food: 5,
        ResourceType.wood: 0,
        ResourceType.iron: 5,
    },
    "by_defense": {
        ResourceType.food: 5,
        ResourceType.wood: 0,
        ResourceType.iron: 10,
    }
}
