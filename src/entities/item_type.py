from enum import Enum


class ItemType(Enum):
    """
    List the item types and their name here
    Then define properties in item_config.py
    """
    GOOD = "good"
    BAD = "bad"
    EE = "EE"
    IA = "IA"
    TOK = "TOK"
    ORALS = "orals"
    HOMEWORK = "homework"
    MOCKS = "mock"
    IB_EXAMS = "ib exams"
    CAS = "CAS"
    COFFEE = "coffee"
    FREE_PERIODS = "free periods"
    GYM = "gym"
    SLEEP = "sleep"
    SOCIAL_MEDIA = "social media"