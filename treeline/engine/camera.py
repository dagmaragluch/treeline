from typing import Tuple
from treeline.engine.actor import Actor
import numpy as np
from treeline.engine.utils.matrices import scale, translate, identity
import math
import pygame
from matplotlib.path import Path

WORLD_SCALE = np.array((1 / 4 * 3, 1 / 4 * math.sqrt(3), 1))

class Camera(Actor):

    def __init__(self, position: Tuple[float, float], fov: int = 16, speed: float = 5.0):
        Actor.__init__(self, position)
        self.fov = fov
        self.speed = speed

        self.screenSize = None
        self.positionOnScreen = None

    def setup(self, screenSize: np.array):
        self.screenSize = screenSize
        self.positionOnScreen = (screenSize[0] / 2, screenSize[1] / 2)

    def transform(self, position: np.array) -> np.array:
        tileSize = self._get_tile_size()
        tileScale = scale(tileSize)
        worldScale = scale(WORLD_SCALE)
        positionVector = worldScale @ np.append(position, 1)

        projection = translate(self.positionOnScreen) @ tileScale
        view = translate(worldScale @ np.append(-np.array(self.position), 1))
        model = translate(positionVector)
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

    def _get_tile_size(self):
        return np.array([self.screenSize[0] / self.fov,
                self.screenSize[0] / self.fov])

    def get_viewport(self):
        fx = self.fov / 2
        fy = fx * self.screenSize[1] / self.screenSize[0]
        fx, fy, w = scale(1/WORLD_SCALE) @ (fx, fy, 1)
        rect = [np.array(c) for c in [(-fx, -fy), (fx, -fy), (fx, fy), (-fx, fy)]]
        viewport = [(c + self.position) for c in rect]
        return Path(viewport)

    def on_event(self, event):
        # For debug purposes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.position = (self.position[0] - 1, self.position[1])
            if event.key == pygame.K_e:
                self.position = (self.position[0] + 1, self.position[1])
            if event.key == pygame.K_SPACE:
                self.position = (0, 0)
