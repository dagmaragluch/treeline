from treeline.engine.engine import Engine
from treeline.engine.camera import Camera
from treeline.engine.actor import Actor
from treeline.misc.shapes import Hexagon
import pygame

if __name__ == '__main__':
    engine = Engine()
    camera = Camera((0, 0))
    engine.set_camera(camera)
    engine.register_for_keys(camera)
    for i, j in [(0, 0), (1, 1), (0, 2), (2, 0)]:
        actor = Actor((i, j), Hexagon(color=(50 + i*100, 100, 100)))
        engine.add_actor(actor)
    engine.start()
