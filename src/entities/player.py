# Player object, position, move_left(), move_right(), freeze(time)
import pygame

import settings


class Player:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = (x, y)

    def update(self, dt, bounds):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x + self.rect.width < bounds[1]:
            self.rect.x += dt * settings.PLAYER_SPEED
        elif keys[pygame.K_LEFT] and self.rect.x > bounds[0]:
            self.rect.x -= dt * settings.PLAYER_SPEED
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)




