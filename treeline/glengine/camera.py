from treeline.glengine.actor import Actor
from typing import Tuple

class Camera(Actor):

    def __init__(self, position: Tuple[float, float], fov: int = 16, speed: float = 5.0):
        Actor.__init__(self, position)
        self.fov = fov
        self.speed = speed
