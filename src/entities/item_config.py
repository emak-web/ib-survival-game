from item_type import ItemType


ITEM_CONFIG = {
    # TODO: Add asset file reference
    ItemType.GOOD: {
        "effects": {
            "energy": +1,
            "stress": -1,
            "grade": +1
        }
    },
    ItemType.BAD: {
        "effects": {
            "energy": -1,
            "stress": +1,
            "grade": -1
        }
    }
}
