import pygame

from entities.item_config import ITEM_CONFIG


class Item:
    def __init__(self, item_type, sprite, speed, x, y, width, height):
        self.type = item_type
        self.config = ITEM_CONFIG[item_type]
        self.image = pygame.transform.scale(sprite, (width*3, height*3))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        # self.rect = pygame.Rect(0, 0, width, height)
        # self.rect.center = (x, y)

    def update(self, dt):
        self.rect.y += dt * self.speed
    
    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 0, 0), self.rect)
        screen.blit(self.image, self.rect)

