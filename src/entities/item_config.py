from item_type import ItemType


ITEM_CONFIG = {
    # TODO: Add asset file reference
    ItemType.IA: {
        "effects": {
            "energy": -5,
            "stress": +5,
            "grade": +1
        }
    },
    ItemType.TOK: {
        "effects": {
            "energy": -4,
            "stress": +2,
            "grade": +1
        }
    },
    ItemType.EE: {
        "effects": {
            "energy": -10,
            "stress": +10,
            "grade": +1  
        }
    },
    ItemType.CAS: {
        "effects": {
            "energy": -3,
            "stress": 0,
            "grade": 0  
        }
    },
    ItemType.COFFEE: {
        "effects": {
            "energy": +10,
            "stress": +1,
            "grade": 0  
        }
    },
    ItemType.FREE_PERIODS: { #RANDOm????
        "effects": {
            "energy": -10,
            "stress": +10,
            "grade": +1  
        }
    },
    ItemType.GYM: {
        "effects": {
            "energy": -10,
            "stress": 0,
            "grade": 0  
        }
    },
    ItemType.HOMEWORK: {
        "effects": {
            "energy": -2,
            "stress": +4,
            "grade": +2  
        }
    },
    ItemType.IB_EXAMS: {
        "effects": {
            "energy": -20,
            "stress": +20,
            "grade": 0  
        }
    },
    ItemType.MOCKS: {
        "effects": {
            "energy": -10,
            "stress": +10,
            "grade": +2  
        }
    },
    ItemType.ORALS: {
        "effects": {
            "energy": -5,
            "stress": +5,
            "grade": +1  
        }
    },
    ItemType.SLEEP: {
        "effects": {
            "energy": +10,
            "stress": -10,
            "grade": 0  
        }
    },
    ItemType.SOCIAL_MEDIA: {
        "effects": {
            "energy": 0,
            "stress": 0,
            "grade": -1  
        }
    }
}
