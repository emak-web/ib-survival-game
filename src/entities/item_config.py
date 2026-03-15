from entities.item_type import ItemType


ITEM_CONFIG = {
    ItemType.MOCKS: {
        "path": "mocks.png",
        "effects": {
            "energy": -10,
            "stress": 10,
            "grade": +1,
        }
    }, 
    ItemType.IB_EXAMS: {
        "path": "ib_exams.png",
        "effects": {
            "energy": -20,
            "stress": 15,
            "grade": +2,
        }
    }, 
    ItemType.COFFEE: {
        "path": "coffee.png",
        "effects": {
            "energy": +10,
            "stress": +1,
            "grade": 0,
        }
    }, 
    ItemType.FREE_PERIODS: {
        "path": "free_period.png",
        "effects": {
            "energy": +10,
            "stress": -10,
            "grade": 0,
        }
    }, 
    ItemType.GYM: {
        "path": "gym.png",
        "effects": {
            "energy": -5,
            "stress": -20,
            "grade": 0,
        }
    }, 
    ItemType.SLEEP: {
        "path": "sleep.png",
        "effects": {
            "energy": +20,
            "stress": -10,
            "grade": 0,
        }
    }, 
    ItemType.SOCIAL_MEDIA: {
        "path": "social_media.png",
        "effects": {
            "energy": -2,
            "stress": -2,
            "grade": -1,
        }
    }, 
    ItemType.CAS: {
        "path": "cas.png",
        "effects": {
            "energy": -5,
            "stress": -5,
            "grade": 0,
        }
    }, 
    ItemType.EE: {
        "path": "ee.png",
        "effects": {
            "energy": -20,
            "stress": 20,
            "grade": 2,
        }
    },
    ItemType.HOMEWORK: {
        "path": "homework.png",
        "effects": {
            "energy": -10,
            "stress": 5,
            "grade": 1,
        }
    },  
    ItemType.IA: {
        "path": "ia.png",
        "effects": {
            "energy": -15,
            "stress": 10,
            "grade": 3,
        }
    },
    ItemType.ORALS: {
        "path": "orals.png",
        "effects": {
            "energy": -15,
            "stress": 10,
            "grade": 3,
        }
    },  
    ItemType.TOK: {
        "path": "tok.png",
        "effects": {
            "energy": -10,
            "stress": 10,
            "grade": 2,
        }
    }, 
}
