import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType
from entities.player import Player
from entities.item_list import ItemList
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

        self.energy = 0
        self.stress = 0
        self.grade = 0

        self.spawn_interval = self.config["spawn_interval"]
        self.spawn_timer = 0
        self.duration = self.config["duration"]

        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 20)

        self.freeze_internal = 0

        self.hub = Hub(
            Label((75, 65), "Grade:", self.font, color = (0, 0, 0)),
            Label((75, 105), "Stress:", self.font, color = (0, 0, 0)),
            Label((75, 145), "Energy:", self.font, color = (0, 0, 0)),
            ProgressBar((130, 50), 150, 30, 45, lambda: self.grade, (0, 0, 255)),
            ProgressBar((130, 90), 150, 30, 100, lambda: self.stress, (255, 0, 0)),
            ProgressBar((130, 130), 150, 30, 100, lambda: self.energy, (0, 255, 0)),
            ProgressBar((0, 0), (self.ctx.settings.WIDTH), 25, self.duration, lambda: self.duration)
        )
        self.burnout_hub = Hub(
            ProgressBar((self.ctx.settings.WIDTH//2-75, self.ctx.settings.HEIGHT//2-15), 150, 30, self.ctx.settings.STRESS_BURNOUT_TIME_INTERVAL, lambda: self.freeze_internal, (0, 0, 0)),
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2-30), "Burnout", self.font, color = (0, 0, 0)),
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

        if self.freeze_internal > 0:
            self.freeze_internal -= dt
        else:
            self.freeze_internal = 0

        self.spawn_timer += dt

        while self.spawn_timer >= self.spawn_interval:
            self.item_list.spawn((0, self.ctx.settings.WIDTH))
            self.spawn_timer -= self.spawn_interval

        if self.stress_burnout() and self.freeze_internal == 0:
            self.freeze_internal = self.ctx.settings.STRESS_BURNOUT_TIME_INTERVAL
        
        if self.freeze_internal > 0:
            self.stress = self.ctx.settings.BASE_STRESS
        else:
            self.player.update(dt, (0, self.ctx.settings.WIDTH), self.get_player_speed())
        
        self.item_list.update(dt, (0, self.ctx.settings.HEIGHT))

        if self.freeze_internal <= 0:
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

            self.ctx.assets.sound("collision.mpeg").play()

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

        if self.freeze_internal > 0:
            self.burnout_hub.draw(screen)

    def get_player_speed(self):
        return self.ctx.settings.PLAYER_SPEED_MIN + (self.energy/100) * (self.ctx.settings.PLAYER_SPEED_MAX - self.ctx.settings.PLAYER_SPEED_MIN)

    def stress_burnout(self):
        return self.stress >= self.ctx.settings.STRESS_BURNOUT
