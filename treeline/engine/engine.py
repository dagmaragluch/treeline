import pygame
import logging
from treeline.engine.actor import Actor
from treeline.engine.camera import Camera
import numpy as np
from datetime import datetime
from typing import List
import matplotlib.path

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
        self.keyWatchers = []
        self.screen = None

    def start(self):
        self.screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        if not self.camera:
            LOGGER.error("No camera set before engine started: aborting")
            return

        screenSize = pygame.display.get_surface().get_size()
        LOGGER.debug(f"Screen size: {screenSize}")
        self.camera.setup(screenSize)

        self.running = True

        thisFrameTime = datetime.now()
        prevFrameTime = thisFrameTime
        mousePosition = None

        while self.running:
            thisFrameTime = datetime.now()
            deltaTime = (thisFrameTime -
                         prevFrameTime).total_seconds() * 1000.0
            if deltaTime > 33:
                LOGGER.warn(f"FPS dropped below 30 (deltaTime: {deltaTime})")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePosition = pygame.mouse.get_pos()
                if event.type in self.events:
                    for actor in self.events[event.type]:
                        actor.on_event(event)

            keys = pygame.key.get_pressed()
            for actor in self.keyWatchers:
                actor.on_key(keys, deltaTime)

            self.screen.fill(BACKGROUND_COLOR)
            for actor in self.actors:
                if actor.shape:
                    bounds = actor.shape.draw(
                        self.camera.transform(actor.position), self.screen)
                    if mousePosition and bounds.contains_point(mousePosition):
                        actor.on_pressed()

            pygame.display.flip()
            prevFrameTime = thisFrameTime
            mousePosition = None

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

    def register_for_keys(self, actor: Actor):
        if actor not in self.keyWatchers:
            self.keyWatchers.append(actor)

    def getActorsUnderCursor(self, position) -> List[Actor]:
        return []
