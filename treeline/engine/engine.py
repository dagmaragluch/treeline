import pygame


class Engine:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Treeline")
        self.running = False

    def start(self):
        self.screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self._quit()

    def _quit(self):
        self.running = False
