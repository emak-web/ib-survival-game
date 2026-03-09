import pygame

from scenes.scene import Scene
from scenes.scene_type import SceneType
from entities.player import Player
from entities.item_list import ItemList



class LevelScene(Scene): #playing scene
    def __init__(self, ctx):
        self.ctx = ctx
        self.player = Player(self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT - 100, 50, 100)
        self.item_list = ItemList()
        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)
        self.score = 0
        
        self.spawn_interval = self.ctx.settings.SPAWN_INTERVAL 
        self.spawn_timer = 0

    def handle_event(self, event):
        pass

    def update(self, dt):
        self.spawn_timer += dt
        while self.spawn_timer >= self.spawn_interval:
            self.item_list.spawn((0, self.ctx.settings.WIDTH))
            self.spawn_timer -= self.spawn_interval

        self.player.update(dt, (0, self.ctx.settings.WIDTH))
        self.item_list.update(dt, (0, self.ctx.settings.HEIGHT))
        self.score += self.item_list.check_collision_falling_object(self.player.rect)

    def draw(self, screen):
        self.player.draw(screen)
        self.item_list.draw(screen)
        text_score = self.font.render(str(self.score), True, (255, 255, 255))
        score_rect = text_score.get_rect(center=(self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2))
        screen.blit(text_score, score_rect)
    
