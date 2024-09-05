from enum import IntEnum
from typing import Mapping, Union

class ITEM_CATEGORY(IntEnum):
    FOOD = 0
    MEDICINE = 1
    TOY = 2
    BOOST = 3
    
class FOOD_CATEGORY(IntEnum):
    SWEET = 0 
    FRUIT = 1
    MAIN_COURSE = 2

class TOY_CATEGORY(IntEnum):
    SMALL = 3
    MEDIUM = 4
    BIG = 5
    NONE = 6

class ACTIVITY_CATEGORY(IntEnum):
    FEED = 0
    PLAY = 1
    CLEAN = 2
    CURE = 3
    BATH = 7
    
    
ITEM_ACT_MAP: Mapping[int, int] = {
    ACTIVITY_CATEGORY.FEED.value: ITEM_CATEGORY.FOOD.value,
    ACTIVITY_CATEGORY.PLAY.value: ITEM_CATEGORY.TOY.value,
    ACTIVITY_CATEGORY.CURE.value: ITEM_CATEGORY.MEDICINE.value
} 


ITEM_EXP_MAP = {
    FOOD_CATEGORY.SWEET.value: 5,
    FOOD_CATEGORY.FRUIT.value: 10,
    FOOD_CATEGORY.MAIN_COURSE.value: 15,
    TOY_CATEGORY.SMALL.value: 5,
    TOY_CATEGORY.MEDIUM.value: 10,
    TOY_CATEGORY.BIG.value: 15,
}

CLEAN_EXP_MAP = {
    ACTIVITY_CATEGORY.BATH.value: 5,
    ACTIVITY_CATEGORY.CLEAN.value: 2,
}


ACTIVITY_TICKET_MAP: Mapping[int, int] = {
    ACTIVITY_CATEGORY.BATH.value: 15,
    ACTIVITY_CATEGORY.CLEAN.value: 5,
}


ACTIVITY_STATS: Mapping[int, int] = {
    ACTIVITY_CATEGORY.BATH: 30,
    ACTIVITY_CATEGORY.CLEAN: 11.67,
}

    
class HEALTH_INDICATOR(IntEnum):
    HAPPINESS = 0.3
    HYGIENE = 0.4
    HUNGER = 0.3
    
class CURRENCY_MAP(IntEnum):
    DIAMOND = 1
    TICKET = 2