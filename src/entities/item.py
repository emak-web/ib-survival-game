import pygame

import settings

from entities.item_config import ITEM_CONFIG


class Item:
    def __init__(self, item_type, x, y, width, height):
        self.type = item_type
        self.config = ITEM_CONFIG[item_type]
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)
    
    def update(self, dt):
        self.rect.y  += dt * settings.ITEM_SPEED
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)

