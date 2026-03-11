import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType
from entities.player import Player
from entities.item_list import ItemList
from entities.item_type import ItemType
from ui.hub import Hub
from ui.label import Label
from entities.item_config import ITEM_CONFIG
from entities.level_config import LEVEL_CONFIG 


class LevelScene(Scene):
    def __init__(self, ctx, level_type):
        self.ctx = ctx
        self.level_type = level_type
        self.config = LEVEL_CONFIG[level_type]

        self.player = Player(self.ctx.assets.image("player.png"), self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT - 50, 50, 50)
        self.item_list = ItemList(self.generate_item_sprites(), self.config["item_speed"])

        self.background = self.ctx.assets.image(self.config["background"])
        self.background = pygame.transform.scale(self.background, (self.ctx.settings.WIDTH, self.ctx.settings.HEIGHT))

        self.score = 0
        self.spawn_interval = self.config["spawn_interval"]
        self.spawn_timer = 0

        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)
        self.hub = Hub(
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2), self.score, self.font, lambda: self.score)
        )

    def generate_item_sprites(self):
        item_sprites = {}

        for item_type in self.config["allowed_items"]:
            item_sprites[item_type] = self.ctx.assets.image(ITEM_CONFIG[item_type]["path"])

        return item_sprites

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
        screen.blit(self.background, (0, 0))
        self.item_list.draw(screen)
        self.player.draw(screen)
        self.hub.draw(screen)

