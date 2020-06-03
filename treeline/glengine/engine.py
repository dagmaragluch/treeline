import pygame
import logging
import OpenGL
OpenGL.ERROR_CHECKING = False
from OpenGL.GL import *
from OpenGL.GL import shaders
from ctypes import sizeof, c_float, c_void_p
import numpy as np
from datetime import datetime
from statistics import mean
import math

from treeline.glengine.actor import Actor
from treeline.glengine.camera import Camera
from treeline.engine.widget import Widget
from treeline.glengine.shape import Shape
from treeline.glengine.matrices import identity, scale, translate

LOGGER = logging.getLogger(__name__)
WORLD_SCALE_VECTOR = np.array((1 / 4 * 3 * 2, 1 / 4 * math.sqrt(3) * 2, 1))
WORLD_SCALE = scale(WORLD_SCALE_VECTOR)

class Engine:

    def __init__(self):
        self.screen = None
        self.actors = []
        self.widgets = []
        self.camera = None
        self.shader_program = None
        self.frame_times = []
        self.render_times = []
        self.mvp_times = []
        self.screen_ratio = None
        self.tile_size = None
        self.projection = None
        pygame.quit()
        pygame.init()

    def start(self):
        self.screen = pygame.display.set_mode(
            flags=pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.OPENGL | pygame.HWSURFACE)

        size = pygame.display.get_surface().get_size()
        self.screen_ratio = scale((size[1] / size[0], 1.0))
        glViewport(0, 0, size[0], size[1])
        glClearColor(71 / 256, 95 / 256, 181 / 256, 1.0)

        self._setup()
        mvp_location = glGetUniformLocation(self.shader_program, "MVP"),

        self.tile_size = (np.array([1, 1, 0]) / self.camera.fov)
        self.projection = self.screen_ratio @ scale(self.tile_size)

        # ++DEBUG
        this_frame_time = datetime.now()
        prev_frame_time = this_frame_time
        mouse_position = None

        total_frames = 0
        lag_frames = 0
        # --DEBUG

        self.running = True
        while self.running:
            # ++DEBUG
            total_frames += 1
            this_frame_time = datetime.now()
            delta_time = (this_frame_time -
                          prev_frame_time).total_seconds() * 1000
            self.frame_times.append(delta_time)
            if delta_time > 33:
                lag_frames += 1
            # --DEBUG

            glClear(GL_COLOR_BUFFER_BIT)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

            # ++DEBUG
            frame_render_time = 0
            frame_mvp_time = 0
            # --DEBUG

            for actor in self.actors:
                if actor.shape:
                    # ++DEBUG
                    begin = datetime.now()
                    # --DEBUG

                    mvp = self._get_mvp(actor.position)
                    glUniformMatrix3fv(mvp_location[0], 1, True, np.ascontiguousarray(mvp, dtype=np.float32))

                    # ++DEBUG
                    delta_time = (datetime.now() -
                                    begin).total_seconds() * 1000
                    frame_mvp_time += delta_time
                    # --DEBUG

                    # ++DEBUG
                    begin = datetime.now()
                    # --DEBUG

                    self._render(actor.shape)

                    # ++DEBUG
                    delta_time = (datetime.now() -
                                    begin).total_seconds() * 1000
                    frame_render_time += delta_time
                    # --DEBUG
                
            # ++DEBUG
            self.render_times.append(frame_render_time)
            self.mvp_times.append(frame_mvp_time)
            # --DEBUG

            pygame.display.flip()

            # ++DEBUG
            prev_frame_time = this_frame_time
            # --DEBUG

        # ++DEBUG
        LOGGER.info(f"Lagged frames: {lag_frames} / {total_frames}")
        LOGGER.info(f"Average frame time: {mean(self.frame_times)} ({1000 / mean(self.frame_times)} FPS)")

        full_render_time = mean(self.render_times)
        full_mvp_time = mean(self.mvp_times)

        LOGGER.info(f"Average render time: {full_render_time} ({1000 / full_render_time} XPS)")
        LOGGER.info(f"Average mvp time: {full_mvp_time} ({1000 / full_mvp_time} XPS)")
        # --DEBUG

    def quit(self):
        self.running = False
        LOGGER.info("Stopping engine on demand")

    def set_camera(self, camera: Camera):
        self.camera = camera

    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def add_widget(self, widget: Widget):
        self.widgets.append(widget)

    def register_for_keys(self, actor: Actor):
        pass

    def _get_mvp(self, actor_position):
        position = WORLD_SCALE @ actor_position
        model = translate(position)

        return self.projection @ model

    def _render(self, shape):
        image_rect = shape.texture.get_rect()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_rect[2],
                     image_rect[3], 0, GL_RGBA, GL_UNSIGNED_BYTE, shape.image_data)

        glDrawArrays(GL_TRIANGLES, 0, 6)

    def _setup(self):
        vertex_shader = shaders.compileShader("""
                        #version 330
                        layout(location = 0) in vec2 pos;
                        layout(location = 1) in vec2 uvIn;
                        out vec2 uv;
                        uniform mat3 MVP;
                        void main() {
                            gl_Position = vec4(MVP * vec3(pos, 1), 1);
                            uv = uvIn;
                        }
            """, GL_VERTEX_SHADER)

        fragment_shader = shaders.compileShader("""
                        #version 330
                        out vec4 fragColor;
                        in vec2 uv;
                        uniform sampler2D tex;
                        uniform mat3 MVP;
                        void main() {
                            fragColor = texture(tex, uv);
                        }
            """, GL_FRAGMENT_SHADER)

        self.shader_program = shaders.compileProgram(vertex_shader, fragment_shader)

        glUseProgram(self.shader_program)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)

        image_texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, image_texture)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        glBufferData(GL_ARRAY_BUFFER, Shape.vertex_data, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, sizeof(c_float)*4, c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, sizeof(c_float)*4, c_void_p(sizeof(c_float)*2))
        glEnableVertexAttribArray(1)
