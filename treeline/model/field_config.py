from treeline.misc.shapes import Hexagon
from treeline.engine.shapes.sprite import Sprite
import pygame

forest = pygame.image.load('./resources/graphics/terrain/forest.png')

hexagons = {
    "grass": Hexagon(color=(82, 235, 52)),
    "grass_highlight": Hexagon(color=(102, 255, 72)),
    "grass_red": Hexagon(color=(255, 235, 52)),  # not red at all
    "forest": Sprite(forest),
    "forest_highlight": Hexagon(color=(41, 137, 22)),
    "mountain": Hexagon(color=(97, 77, 50)),
    "mountain_highlight": Hexagon(color=(117, 97, 70))
}
