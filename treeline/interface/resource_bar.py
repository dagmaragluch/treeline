import pygame
import pygame.freetype
from pygame.freetype import Font

from treeline.model.player import Player
from treeline.interface.label import Label


class ResourceBar(Label):
    def __init__(self, font: Font, player: Player):
        Label.__init__(self, (0, 0), font)
        self.player = player

    def draw(self, surface) -> pygame.Rect:
        self.text = str(self.player.resources)
        return Label.draw(self, surface)
