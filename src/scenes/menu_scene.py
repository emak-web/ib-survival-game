from scenes.scene import Scene
from scenes.scene_type import SceneType
from ui.hub import Hub
from ui.button import Button
from ui.label import Label
from ui.progress_bar import ProgressBar


class MenuScene(Scene):
    def __init__(self, ctx):
        self.ctx = ctx
        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)
        self.grade = 20

        self.hub = Hub(
            Button([self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2], "Click me", SceneType.LEVEL, self.font),
            Label((self.ctx.settings.WIDTH//2, 50), "IB Survival Game", self.font),
            Label((self.ctx.settings.WIDTH//2, 100), "Choose your level:", self.font),
            ProgressBar((self.ctx.settings.WIDTH//2-100, 150), 200, 30, 45, lambda: self.grade)
        )

    def handle_event(self, event):
        result = self.hub.handle_event(event)
        if result:
            return result

    def update(self, dt):
        pass

    def draw(self, screen):
        self.hub.draw(screen)

