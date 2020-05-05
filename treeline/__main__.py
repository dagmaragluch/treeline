from treeline.engine.engine import Engine
from treeline.engine.camera import Camera
from treeline.engine.actor import Actor
import pygame

class TestActor(Actor):
    def onEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print("Got it")

if __name__ == '__main__':
    engine = Engine()
    camera = Camera()
    camera.position = (0, 0)
    engine.setCamera(camera)
    testActor = TestActor()
    engine.addActor(testActor)
    engine.registerForEvent(testActor, pygame.KEYDOWN)
    engine.start()
