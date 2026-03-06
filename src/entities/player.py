# Player object, position, move_left(), move_right(), freeze(time)
import pygame

import settings


class Player:
    def __init__(self, position, hitbox_width, hitbox_height):
        self.position = position
        self.hitbox_width = hitbox_width
        self.hitbox_height = hitbox_height
        self.direction = (0, 0)

    def left(self):
        self.direction = (-1, 0)
    
    def right(self):
        self.direction = (1, 0)
    
    def update(self, dt, bounds):
        self.position[0] += dt * settings.PLAYER_SPEED * self.direction[0]
        self.position[0] = max(self.position[0], bounds[0] + self.hitbox_width//2)
        self.position[0] = min(self.position[0], bounds[1] - self.hitbox_width//2)
        self.position[1] += dt * settings.PLAYER_SPEED * self.direction[1]
        keys = pygame.key.get_pressed()
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.direction = (0, 0)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.position[0] - self.hitbox_width//2, self.position[1] - self.hitbox_height//2, self.hitbox_width, self.hitbox_height))




