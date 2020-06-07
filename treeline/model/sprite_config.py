import pygame
import numpy as np
from typing import Dict
from treeline.engine.shapes.sprite import Sprite

GRAPHICS_PATH = "./resources/graphics"
TERRAIN_PATH = f"{GRAPHICS_PATH}/terrain"
BUILDING_PATH = f"{GRAPHICS_PATH}/buildings"

_paths = {
    "grass": f"{TERRAIN_PATH}/grass.png",
    "grass_highlight": f"{TERRAIN_PATH}/grass_highlight.png",
    "grass_red": f"{TERRAIN_PATH}/forest_red.png",  # TODO
    "forest": f"{TERRAIN_PATH}/forest.png",
    "forest_highlight": f"{TERRAIN_PATH}/forest_highlight.png",
    "mountain": f"{TERRAIN_PATH}/mountain.png",
    "mountain_highlight": f"{TERRAIN_PATH}/mountain_highlight.png",

    "farm": f"{BUILDING_PATH}/farm.png",
    "sawmill": f"{BUILDING_PATH}/sawmill.png",
    "iron_mine": f"{BUILDING_PATH}/iron_mine.png",
    "house": f"{BUILDING_PATH}/house.png",
    "townhall": f"{BUILDING_PATH}/townhall.png",
    "tower": f"{BUILDING_PATH}/tower.png",
}

sprites: Dict[str, Sprite] = {}


def load_sprites(scale: np.array):
    """Loads sprite defined in _paths dict. Needs pygame display mode to be set before this call."""
    for key, path in _paths.items():
        sprites[key] = Sprite(pygame.image.load(path).convert_alpha(), scale)
