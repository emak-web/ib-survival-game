from item_config import ITEM_CONFIG


class Item:
    def __init__(self, item_type, position):
        self.type = item_type
        self.config = ITEM_CONFIG[item_type]
        self.position = position

