from scenes.scene import Scene
from scenes.scene_type import SceneType
from ui.hub import Hub
from ui.button import Button
from ui.label import Label
from entities.level_type import LevelType


class MenuScene(Scene):
    def __init__(self, ctx):
        self.ctx = ctx
        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)

        self.hub = Hub(
            Label((self.ctx.settings.WIDTH//2, 50), "IB Survival Game", self.font),
            Label((self.ctx.settings.WIDTH//2, 100), "Choose your level:", self.font),
            Button([self.ctx.settings.WIDTH//2 - 200, self.ctx.settings.HEIGHT//2], "Pre-IB", SceneType.LEVEL, {"level_type": LevelType.PRE_IB}, self.font),
            Button([self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2], "IB1", SceneType.LEVEL, {"level_type": LevelType.IB1}, self.font),
            Button([self.ctx.settings.WIDTH//2 + 200, self.ctx.settings.HEIGHT//2], "IB2", SceneType.LEVEL, {"level_type": LevelType.IB2}, self.font),
        )

    def handle_event(self, event):
        result = self.hub.handle_event(event)
        if result:
            return result

    def update(self, dt):
        pass

    def draw(self, screen):
        self.hub.draw(screen)

