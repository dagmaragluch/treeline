from typing import Tuple
from treeline.engine.actor import Actor
import numpy as np
from treeline.engine.utils.matrices import scale, translate, identity
import math
import pygame
from matplotlib.path import Path

WORLD_SCALE_VECTOR = np.array((1 / 4 * 3, 1 / 4 * math.sqrt(3), 1))
WORLD_SCALE = scale(WORLD_SCALE_VECTOR)


class Camera(Actor):

    def __init__(self, position: Tuple[float, float], fov: int = 16, speed: float = 5.0):
        Actor.__init__(self, position)
        self.fov = fov
        self.projection = None
        self.positionOnScreen = None
        self.screenSize = None
        self.speed = speed
        self.tile_scale = None
        self.view = None

    def setup(self, screen_size: np.array):
        self.screenSize = screen_size
        self.positionOnScreen = (screen_size[0] / 2, screen_size[1] / 2)
        tile_size = self.get_scale()
        self.tile_scale = scale(tile_size)

    def frame(self):
        self.projection = translate(self.positionOnScreen) @ self.tile_scale
        self.view = translate(WORLD_SCALE @ np.append(-np.array(self.position), 1))

    def transform(self, position: np.array) -> np.array:
        position_vector = WORLD_SCALE @ np.append(position, 1)
        model = translate(position_vector)
        mvp = self.projection @ self.view @ model
        return mvp

    def on_key(self, keys, delta_time):
        m = self.speed * delta_time / 1000
        if keys[pygame.K_w]:
            self.position = (self.position[0], self.position[1] - m)
        if keys[pygame.K_a]:
            self.position = (self.position[0] - m, self.position[1])
        if keys[pygame.K_s]:
            self.position = (self.position[0], self.position[1] + m)
        if keys[pygame.K_d]:
            self.position = (self.position[0] + m, self.position[1])

    def get_scale(self):
        return np.array([self.screenSize[0] / self.fov,
                         self.screenSize[0] / self.fov])

    def get_viewport(self):
        fx = self.fov / 2
        fy = fx * self.screenSize[1] / self.screenSize[0]
        fx, fy, w = scale(1 / WORLD_SCALE_VECTOR) @ (fx, fy, 1)
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
