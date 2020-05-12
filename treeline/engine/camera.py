from typing import Tuple
from treeline.engine.actor import Actor
import numpy as np
from treeline.engine.utils.matrices import *
import math


class Camera(Actor):

    def __init__(self, position: Tuple[int, int], fov: int = 16):
        Actor.__init__(self, position)
        self.fov = fov

    def setup(self, screenSize: np.array):
        self.screenSize = screenSize
        self.positionOnScreen = (screenSize[0] / 2, screenSize[1] / 2)

    def transform(self, position: np.array) -> np.array:
        tileSize = np.array([self.screenSize[0] / self.fov,
                             self.screenSize[0] / self.fov])
        tileScale = scale(np.array(tileSize))
        positionVector = tileScale.dot(
            np.array([position[0] / 4 * 3, position[1] / 4 * math.sqrt(3), 1]))  # nie pytajcie

        projection = translate(self.positionOnScreen)
        view = translate(-np.array(self.position))
        model = translate(positionVector) @ tileScale
        mvp = projection @ view @ model
        return mvp
