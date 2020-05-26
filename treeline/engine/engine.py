import pygame
import logging
from treeline.engine.actor import Actor
from treeline.engine.camera import Camera
import numpy as np
from datetime import datetime
from typing import List
import matplotlib.path
from statistics import mean

LOGGER = logging.getLogger(__name__)
BACKGROUND_COLOR = (66, 135, 245)


class Engine:

    def __init__(self):
        self.screen = None
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

        screen_size = pygame.display.get_surface().get_size()
        LOGGER.debug(f"Screen size: {screen_size}")
        self.camera.setup(screen_size)

        self.running = True

        this_frame_time = datetime.now()
        prev_frame_time = this_frame_time
        mouse_position = None

        total_frames = 0
        lag_frames = 0
        frame_times = []  # TODO: remove for release

        while self.running:
            total_frames += 1
            self.camera.frame()
            viewport = self.camera.get_viewport()
            this_frame_time = datetime.now()
            delta_time = (this_frame_time -
                          prev_frame_time).total_seconds() * 1000
            frame_times.append(delta_time)
            if delta_time > 33:
                lag_frames += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = pygame.mouse.get_pos()
                if event.type in self.events:
                    for actor in self.events[event.type]:
                        actor.on_event(event)

            keys = pygame.key.get_pressed()
            for actor in self.keyWatchers:
                actor.on_key(keys, delta_time)

            self.screen.fill(BACKGROUND_COLOR)
            for actor in self.actors:
                if actor.shape and (viewport.contains_point(actor.position, radius=1)):
                    bounds = actor.shape.draw(
                        self.camera.transform(actor.position), self.screen)
                    if mouse_position and bounds.contains_point(mouse_position):
                        actor.on_pressed()

            pygame.display.flip()
            prev_frame_time = this_frame_time
            mouse_position = None

        LOGGER.info(f"Lagged frames: {lag_frames} / {total_frames}")
        LOGGER.info(f"Average FPS: {1000 / mean(frame_times)}")

    def _quit(self):
        self.running = False
        LOGGER.info("Stopping engine on demand")

    def set_camera(self, camera: Camera):
        self.camera = camera

    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def register_for_event(self, actor: Actor, event_type: int):
        if event_type in self.events:
            self.events[event_type].append(actor)
        else:
            self.events[event_type] = [actor]

    def register_for_keys(self, actor: Actor):
        if actor not in self.keyWatchers:
            self.keyWatchers.append(actor)

    def getActorsUnderCursor(self, position) -> List[Actor]:
        return []
