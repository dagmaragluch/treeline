from treeline.model.resource import Resources, ResourceType

STARTING_RESOURCES = {
    "food": 100,
    "wood": 100,
    "iron": 50,
}
resources_per_turn = {
    "grass": {
        "food": 2,
    },
    "forest": {
        "food": 1,
        "wood": 2,
    },
    "mountain": {
        "iron": 1,
    }
}

resources_limit = {
    "grass": {
        "food": 100,
    },
    "forest": {
        "food": 100,
        "wood": 50,
    },
    "mountain": {
        "iron": 100,
    }
}

field_prices = {
    "neutral": {
        "food": 5,
    },
    "take_over": {
        "food": 5,
        "iron": 5,
    },
    "defended": {
        "food": 5,
        "iron": 10,
    }
}
