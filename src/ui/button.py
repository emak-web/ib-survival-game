import pygame

from ui.ui import UI


class Button(UI):
    def __init__(self, position, text, action, data, font):
        self.position = position
        self.text = text
        self.font = font
        self.action = action
        self.data = data

        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.position)

        self.rect = self.text_surface.get_rect(center=self.position).inflate(20, 10)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return self.action, self.data

    def update(self, dt):
        pass

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = (0, 255, 0)

        if self.rect.collidepoint(mouse_pos):
            color = (255, 0, 0)

        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.text_surface, self.text_rect)
