import random

from entities.item import Item
from entities.item_type import ItemType
import settings


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
        self.items.append(Item(item_type, self.item_sprites[item_type], self.item_speed, random.randint(bounds[0]+settings.ITEM_WIDTH//2, bounds[1]-settings.ITEM_WIDTH//2), 0, settings.ITEM_WIDTH, settings.ITEM_HEIGHT))

    def check_collisions(self, player_rect):
        for item in self.items:
            if player_rect.colliderect(item.hitbox_rect):
                item_type = item.type
                self.items.remove(item)
                return item_type

