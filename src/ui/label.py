from ui.ui import UI


class Label(UI):
    def __init__(self, position, text, font, text_getter = None, color = (255, 255, 255)):
        self.position = position
        self.text = text
        self.font = font
        self.color = color
        self.text_getter = text_getter
        self.render()

    def render(self):
        if self.text_getter:
            self.text = str(self.text_getter())
        self.text_surface = self.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.position)

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        if self.text_getter:
            self.render()
        screen.blit(self.text_surface, self.text_rect)
