from abc import ABC, abstractmethod


class Scene(ABC):
    """
    Base class for scenes
    Each scene must implement the following methods
    To switch scenes return SceneType in eather handle_event or update
    """
    @abstractmethod
    def handle_event(self, event):
        return None

    @abstractmethod
    def update(self, dt):
        return None

    @abstractmethod
    def draw(self, screen):
        pass

