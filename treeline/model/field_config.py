from treeline.engine.shapes.sprite import Sprite
import pygame

forest = pygame.image.load('./resources/graphics/terrain/forest.png')

hexagons = {
    "grass": Sprite(pygame.image.load('./resources/graphics/terrain/grass.png')),
    "grass_highlight": Sprite(pygame.image.load('./resources/graphics/terrain/grass.png')), # TODO
    "grass_red": Sprite(pygame.image.load('./resources/graphics/terrain/grass.png')), # TODO
    "forest": Sprite(pygame.image.load('./resources/graphics/terrain/forest.png')),
    "forest_highlight": Sprite(pygame.image.load('./resources/graphics/terrain/forest.png')), # TODO
    "mountain": Sprite(pygame.image.load('./resources/graphics/terrain/mountain.png')),
    "mountain_highlight": Sprite(pygame.image.load('./resources/graphics/terrain/mountain.png')) # TODO
}
