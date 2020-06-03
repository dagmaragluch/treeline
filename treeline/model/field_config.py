from treeline.misc.shapes import Hexagon
from treeline.engine.shapes.sprite import Sprite
import pygame

forest = pygame.image.load('./resources/graphics/terrain/forest.png')

hexagons = {
    "grass": Sprite(pygame.image.load('./resources/graphics/terrain/grass.png')),
    "grass_highlight": Hexagon(color=(102, 255, 72)),
    "grass_red": Hexagon(color=(255, 235, 52)),  # not red at all
    "forest": Sprite(pygame.image.load('./resources/graphics/terrain/forest.png')),
    "forest_highlight": Hexagon(color=(41, 137, 22)),
    "mountain": Sprite(pygame.image.load('./resources/graphics/terrain/mountain.png')),
    "mountain_highlight": Hexagon(color=(117, 97, 70))
}
