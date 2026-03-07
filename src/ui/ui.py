from abc import ABC, abstractmethod


class UI(ABC):
    @abstractmethod
    def handle_event(self, event):
        return None

    @abstractmethod
    def update(self, dt):
        return None

    @abstractmethod
    def draw(self, screen):
        pass

