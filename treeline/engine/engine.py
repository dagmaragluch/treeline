import pygame
import logging
from treeline.engine.actor import Actor
from treeline.engine.camera import Camera

LOGGER = logging.getLogger(__name__)
BACKGROUND_COLOR = (66, 135, 245)


class Engine:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Treeline")
        self.running = False
        self.camera = None
        self.actors = []
        self.events = {}

    def start(self):
        self.screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        self.screen.fill(BACKGROUND_COLOR)

        if not self.camera:
            LOGGER.error("No camera set before engine started: aborting")
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
                        actor.on_event(event)
            for actor in self.actors:
                actor.shape.draw(actor.position, self.screen)
            pygame.display.flip()

    def _quit(self):
        self.running = False
        LOGGER.info("Stopping engine on demand")

    def set_camera(self, camera: Camera):
        self.camera = camera

    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def register_for_event(self, actor: Actor, eventType: int):
        if eventType in self.events:
            self.events[eventType].append(actor)
        else:
            self.events[eventType] = [actor]
