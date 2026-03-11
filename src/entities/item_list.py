import random

from entities.item import Item
from entities.item_type import ItemType


class ItemList:
    def __init__(self, item_sprites, item_speed):
        self.items = []
        self.item_sprites = item_sprites
        self.item_speed = item_speed
    
    def draw(self, screen):
        for item in self.items:
            item.draw(screen)

    def update(self, dt, bounds):
        for item in self.items:
            item.update(dt)

            if item.rect.y >= bounds[1]:
                self.items.remove(item)

    def spawn(self, bounds):
        item_type = random.choice(list(self.item_sprites.keys()))
        self.items.append(Item(item_type, self.item_sprites[item_type], self.item_speed, random.randint(*bounds), 0, 50, 50))

    def check_collisions(self, player_rect):
        n = 0
        for item in self.items:
            if player_rect.colliderect(item.rect):
                self.items.remove(item)
                n += 1
        return n

