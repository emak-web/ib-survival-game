

class Hub:
    def __init__(self, *elements):
        self.elements = elements

    def handle_event(self, event):
        for element in self.elements:
            action = element.handle_event(event)
            if action:
                return action

    def draw(self, screen):
        for element in self.elements:
            element.draw(screen)

