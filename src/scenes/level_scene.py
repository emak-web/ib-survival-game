import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType


class LevelScene(Scene):
    def __init__(self, ctx):
        self.ctx = ctx

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                return SceneType.MENU

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (0, 0, 100, 100))

