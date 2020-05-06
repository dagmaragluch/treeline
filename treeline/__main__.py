from treeline.engine.engine import Engine
from treeline.engine.camera import Camera
from treeline.engine.actor import Actor
import pygame

class TestActor(Actor):
    def on_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Got it")

if __name__ == '__main__':
    engine = Engine()
    camera = Camera()
    camera.position = (0, 0)
    engine.set_camera(camera)
    testActor = TestActor()
    engine.add_actor(testActor)
    engine.register_for_event(testActor, pygame.KEYDOWN)
    engine.start()
