import pygame
import logging
from treeline.engine.actor import Actor
from treeline.engine.camera import Camera

class Engine:

    def __init__(self):
        self.logger = logging.getLogger("ENGINE")
        self.logger.setLevel(logging.DEBUG)
        pygame.init()
        pygame.display.set_caption("Treeline")
        self.running = False
        self.camera = None
        self.actors = []
        self.events = {}

    def start(self):
        self.screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        if not self.camera:
            self.logger.error("No camera set before engine started: aborting")
            return

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._quit()
                if event.type in self.events:
                    for actor in self.events[event.type]:
                        actor.onEvent(event)

    def _quit(self):
        self.running = False
        self.logger.info("Stopping engine on demand")

    def setCamera(self, camera: Camera):
        self.camera = camera

    def addActor(self, actor: Actor):
        self.actors.append(actor)

    def registerForEvent(self, actor: Actor, eventType: int):
        if eventType in self.events:
            self.events[eventType].append(actor)
        else:
            self.events[eventType] = [actor]