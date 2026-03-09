import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType
from entities.player import Player
from entities.item_list import ItemList

from ui.hub import Hub
from ui.label import Label


class LevelScene(Scene):
    def __init__(self, ctx):
        self.ctx = ctx
        self.player = Player(self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT - 30, 50, 50)
        self.item_list = ItemList()

        self.score = 0
        self.spawn_interval = self.ctx.settings.SPAWN_INTERVAL
        self.spawn_timer = 0

        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)
        self.hub = Hub(
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2), self.score, self.font, lambda: self.score)
        )

    def handle_event(self, event):
        pass
            
    def update(self, dt):
        self.spawn_timer += dt
        while self.spawn_timer >= self.spawn_interval:
            self.item_list.spawn((0, self.ctx.settings.WIDTH))
            self.spawn_timer -= self.spawn_interval

        self.player.update(dt, (0, self.ctx.settings.WIDTH))
        self.item_list.update(dt, (0, self.ctx.settings.HEIGHT))
        self.score += self.item_list.check_collisions(self.player.rect)

    def draw(self, screen):
        self.item_list.draw(screen)
        self.player.draw(screen)
        self.hub.draw(screen)

