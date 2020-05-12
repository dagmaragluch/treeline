from treeline.engine.engine import Engine
from treeline.engine.camera import Camera
from treeline.engine.actor import Actor
from treeline.misc.shapes import Hexagon
import pygame


class TestActor(Actor):
    def on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Got it")


if __name__ == '__main__':
    engine = Engine()
    camera = Camera((0, 0))
    engine.set_camera(camera)
    for i, j in [(0, 0), (1, 1)]:
        testActor = TestActor((i, j), Hexagon(color=(100 + i*100, 100, 100)))
        engine.add_actor(testActor)
    engine.start()
