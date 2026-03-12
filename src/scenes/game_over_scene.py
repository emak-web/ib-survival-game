from scenes.scene import Scene
from scenes.scene_type import SceneType
from ui.hub import Hub
from ui.button import Button
from ui.label import Label
from entities.level_type import LevelType


class GamOverScene(Scene):
    def __init__(self, ctx, game_state):
        self.ctx = ctx
        self.font = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 20)
        self.font_title = self.ctx.assets.font(self.ctx.settings.DEFAULT_FONT, 30)
        self.game_state = game_state

        title = "YOU SURVIVED THE IB" if game_state["grade"] >= 25 else "YOU DID NOT SURVIVE THE IB"
        self.hub = Hub(
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2-200), title, self.font_title),
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2-80), f"Final grade: {game_state['grade']}", self.font),
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2-40), f"Stress: {game_state['stress']}", self.font),
            Label((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2), f"Energy: {game_state['energy']}", self.font),
            Button((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2+100), "Play again", SceneType.LEVEL, {"level_type": game_state["level_type"]}, self.font_title),
            Button((self.ctx.settings.WIDTH//2, self.ctx.settings.HEIGHT//2+200), "Main menu", SceneType.MENU, None, self.font_title),
        )

    def handle_event(self, event):
        result = self.hub.handle_event(event)
        if result:
            return result

    def update(self, dt):
        pass

    def draw(self, screen):
        self.hub.draw(screen)

