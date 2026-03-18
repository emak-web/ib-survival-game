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
        self.credits_font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 15)
        self.click_sound = self.ctx.assets.sound("click.ogg")

        self.hub = Hub(
            Label((self.ctx.settings.WIDTH//2, 150), "IB Survival Game", self.font),
            Label((self.ctx.settings.WIDTH//2, 220), "Choose your level:", self.font),
            Button([self.ctx.settings.WIDTH//2 - 150, self.ctx.settings.HEIGHT//2], "PIB", SceneType.LEVEL, {"level_type": LevelType.PRE_IB}, self.font, self.click_sound),
            Button([self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2], "IB1", SceneType.LEVEL, {"level_type": LevelType.IB1}, self.font, self.click_sound),
            Button([self.ctx.settings.WIDTH//2 + 150, self.ctx.settings.HEIGHT//2], "IB2", SceneType.LEVEL, {"level_type": LevelType.IB2}, self.font, self.click_sound),
            Label((self.ctx.settings.WIDTH//2, 400), "By Egor and Laura", self.credits_font),
        )

    def handle_event(self, event):
        result = self.hub.handle_event(event)
        if result:
            return result

    def update(self, dt):
        pass

    def draw(self, screen):
        self.hub.draw(screen)

