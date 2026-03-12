import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType
from entities.player import Player
from entities.item_list import ItemList
from entities.item_type import ItemType
from ui.hub import Hub
from ui.label import Label
from ui.progress_bar import ProgressBar
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

        self.energy = 100
        self.stress = 0
        self.grade = 0

        self.spawn_interval = self.config["spawn_interval"]
        self.spawn_timer = 0
        self.duration = self.config["duration"]

        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)
        self.hub = Hub(
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2), "", self.font, lambda: f"{int(self.duration)}s left"),
            ProgressBar((10, 10), 150, 30, 45, lambda: self.grade),
            ProgressBar((10, 50), 150, 30, 100, lambda: self.stress),
            ProgressBar((10, 90), 150, 30, 100, lambda: self.energy),
        )

    def generate_item_sprites(self):
        item_sprites = {}

        for item_type in self.config["allowed_items"]:
            item_sprites[item_type] = self.ctx.assets.image(ITEM_CONFIG[item_type]["path"])

        return item_sprites

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.duration = 0
            
    def update(self, dt):
        if self.duration <= 0:
            self.duration = 0
            return SceneType.GAME_OVER, self.game_over_state()
        
        self.duration -= dt

        self.spawn_timer += dt
        while self.spawn_timer >= self.spawn_interval:
            self.item_list.spawn((0, self.ctx.settings.WIDTH))
            self.spawn_timer -= self.spawn_interval

        self.player.update(dt, (0, self.ctx.settings.WIDTH))
        self.item_list.update(dt, (0, self.ctx.settings.HEIGHT))

        self.update_score()

    def update_score(self):
        item_type = self.item_list.check_collisions(self.player.rect)
        if item_type:
            self.energy += ITEM_CONFIG[item_type]["effects"]["energy"]
            self.stress += ITEM_CONFIG[item_type]["effects"]["stress"]
            self.grade += ITEM_CONFIG[item_type]["effects"]["grade"]

            self.energy = max(0, min(self.energy, 100))
            self.stress = max(0, min(self.stress, 100))
            self.grade  = max(0, min(self.grade, 45))

    def game_over_state(self):
        return {
            "level_type": self.level_type,
            "grade": self.grade,
            "stress": self.stress,
            "energy": self.energy
        }

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.item_list.draw(screen)
        self.player.draw(screen)
        self.hub.draw(screen)

