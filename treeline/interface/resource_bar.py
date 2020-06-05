import pygame
import pygame.freetype

from treeline.model.player import Player
from treeline.engine.widget import Widget


class ResourceBar(Widget):
    def __init__(self, player: Player):
        Widget.__init__(self, (0, 0))
        self.player = player
        self.font = pygame.freetype.SysFont("Comic Sans MS", 24)

    def draw(self, surface) -> pygame.Rect:
        self.font.render_to(surface, self.position, str(self.player.resources), (0, 0, 0))
        return pygame.Rect(1, 2, 3, 4)
