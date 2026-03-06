import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType
from entities.player import Player


class LevelScene(Scene): #playing scene
    def __init__(self, ctx):
        self.ctx = ctx
        self.player = Player([self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT - 100], 50, 100)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.left()
            elif event.key == pygame.K_RIGHT:
                self.player.right()   
            
    def update(self, dt):
        self.player.update(dt, (0, self.ctx.settings.WIDTH))

    def draw(self, screen):
        self.player.draw(screen)

