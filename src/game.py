import pygame

from scenes.menu_scene import MenuScene
from scenes.level_scene import LevelScene
from scenes.scene_type import SceneType
from assets import Assets
import settings


class Context:
    """
    Context data for each scene, settings with width/height etc, assets loader
    """
    def __init__(self, settings, assets):
        self.settings = settings
        self.assets = assets


class Game:
    def __init__(self):
        pygame.init()

        self.width, self.height = settings.WIDTH, settings.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(settings.CAPTION)
        self.clock = pygame.time.Clock()
        self.running = True

        self.assets = Assets()
        self.ctx = Context(settings, self.assets)
        self.scene = MenuScene(self.ctx)

    def run(self):
        while self.running:
            dt = min(self.clock.tick(settings.FPS)/1000, 0.1)

            for event in pygame.event.get():
                request = self.handle_event(event)
                if request:
                    self.switch(request)

            request = self.update(dt)
            if request:
                self.switch(request)
                print(self.scene)
            self.draw()

        pygame.quit()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False

        return self.scene.handle_event(event)
    
    def update(self, dt):
        return self.scene.update(dt)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.scene.draw(self.screen)
        pygame.display.flip()

    def switch(self, request):
        if request == SceneType.MENU:
            self.scene = MenuScene(self.ctx)
        elif request == SceneType.LEVEL:
            self.scene = LevelScene(self.ctx)



