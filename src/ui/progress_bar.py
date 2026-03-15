import pygame

from ui.ui import UI


class ProgressBar(UI):
    def __init__(self, position, width, height, max_value, value_getter, color = (0, 0, 0)):
        self.position = position
        self.width = width
        self.height = height
        self.max_value = max_value
        self.value_getter = value_getter
        self.color = color

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        outer_rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)
        inner_rect = pygame.Rect(self.position[0], self.position[1], min(self.width*(self.value_getter()/self.max_value), self.width), self.height).inflate(-4, -4)
        pygame.draw.rect(screen, (255, 255, 255), outer_rect)
        pygame.draw.rect(screen, self.color, inner_rect)
