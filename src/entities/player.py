import pygame

import settings


class Player:
    def __init__(self, sprite, x, y, width, height):
        self.image = sprite
        self.rect = sprite.get_rect(center=(x, y))
        # self.rect = pygame.Rect(0, 0, width, height)
        # self.rect.center = (x, y)
    
    def update(self, dt, bounds):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x + self.rect.width < bounds[1]:
            self.rect.x += dt * settings.PLAYER_SPEED
        elif keys[pygame.K_LEFT] and self.rect.x > bounds[0]:
            self.rect.x -= dt * settings.PLAYER_SPEED
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

