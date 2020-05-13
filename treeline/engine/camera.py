from typing import Tuple
from treeline.engine.actor import Actor
import numpy as np
from treeline.engine.utils.matrices import scale, translate, identity
import math
import pygame


class Camera(Actor):

    def __init__(self, position: Tuple[float, float], fov: int = 16, speed: float = 3.0):
        Actor.__init__(self, position)
        self.fov = fov
        self.in_game_speed = speed

    def setup(self, screenSize: np.array):
        self.screenSize = screenSize
        self.positionOnScreen = (screenSize[0] / 2, screenSize[1] / 2)
        self.speed = self.in_game_speed * self.screenSize[0] / self.fov

    def transform(self, position: np.array) -> np.array:
        tileSize = [self.screenSize[0] / self.fov,
                    self.screenSize[0] / self.fov]
        tileScale = scale(tileSize)
        positionVector = tileScale.dot(
            [position[0] / 4 * 3, position[1] / 4 * math.sqrt(3), 1])  # nie pytajcie

        projection = translate(self.positionOnScreen)
        view = translate(-np.array(self.position))
        model = translate(positionVector) @ tileScale
        mvp = projection @ view @ model
        return mvp

    def on_key(self, keys, deltaTime):
        m = self.speed * deltaTime / 1000
        if keys[pygame.K_w]:
            self.position = (self.position[0], self.position[1] - m)
        if keys[pygame.K_a]:
            self.position = (self.position[0] - m, self.position[1])
        if keys[pygame.K_s]:
            self.position = (self.position[0], self.position[1] + m)
        if keys[pygame.K_d]:
            self.position = (self.position[0] + m, self.position[1])
