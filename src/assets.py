import os

import pygame

import settings


class Assets:
    def __init__(self):
        self.image_cache = {}
        self.sound_cache = {}
        self.font_cache = {}

    def image(self, path):
        if path not in self.image_cache:
            self.image_cache[path] = pygame.image.load(os.path.join(settings.IMAGE_DIR, path)).convert_alpha()

        return self.image_cache[path]

    def sound(self, path):
        if path not in self.sound_cache:
            self.sound_cache[path] = pygame.mixer.Sound(os.path.join(settings.SOUND_DIR, path))

        return self.sound_cache[path]

    def font(self, path, size):
        if (path, size) not in self.font_cache:
            self.font_cache[(path, size)] = pygame.font.Font(os.path.join(settings.FONT_DIR, path), size)

        return self.font_cache[(path, size)]

