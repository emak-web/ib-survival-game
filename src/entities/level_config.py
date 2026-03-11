from entities.level_type import LevelType
from entities.item_type import ItemType


LEVEL_CONFIG = {
    LevelType.PRE_IB: {
        "name": "Pre-IB",
        "background": "bg_preib.png",
        "allowed_items": [ItemType.COFFEE, ItemType.SLEEP],
        "spawn_interval": 1,
        "item_speed": 100,
        "duration": 30
    },
    LevelType.IB1: {
        "name": "IB1",
        "background": "bg_ib1.png",
        "allowed_items": [ItemType.COFFEE, ItemType.SLEEP, ItemType.MOCKS],
        "spawn_interval": 0.75,
        "item_speed": 200,
        "duration": 60
    },
    LevelType.IB2: {
        "name": "IB2",
        "background": "bg_ib2.png",
        "allowed_items": [ItemType.COFFEE, ItemType.SLEEP, ItemType.GYM, ItemType.SOCIAL_MEDIA, ItemType.IB_EXAMS],
        "spawn_interval": 0.5,
        "item_speed": 300,
        "duration": 90
    },
}
