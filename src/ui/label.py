from ui.ui import UI


class Label(UI):
    def __init__(self, position, text, font, color = (255, 255, 255)):
        self.position = position
        self.text = text
        self.font = font
        self.color = color

        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.position)

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)
