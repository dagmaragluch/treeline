from typing import Tuple

from treeline.engine.actor import Actor


class Camera(Actor):

    def __init__(self, position: Tuple[int, int]):
        Actor.__init__(self, position)
