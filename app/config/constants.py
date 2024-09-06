from datetime import date, timedelta

DEFAULT_GAME_TICKET = 1000
HATCH_DURATION = 30
NORMAL_PET_SLOT = 3
MAX_PET_SLOT = 5
MIN_POOP_DURATION = 45
MAX_POOP_DURATION = 60
HATCH_COMPLETE_AWARD = 1000
FARM_AWARD = 30
MAX_TUTORIAL_PHRASES = 15
MAX_DAILY_STREAK = 7
BASE_TICKET_FACTOR = 5
TOY_USAGE_LIMIT = 10
EVOLVE_POTION_ID = 28
XP_BOOST_ITEM_ID = 29
XP_BOOST = 30
TICKET_BOOST_ITEM_ID = 30
SOCIAL_QUEST_TICKET_REWARD = 40
TICKET_PER_DIAMOND = 920
DIAMOND_PER_PETSLOT = 4
DAILY_XP_LIMIT = 268
SICKNESS_PERCENT = 30
STAT_DECLINE_PER_MINUTE = 100 / 2160

PET_MAX_LEVEL = 99
PET_MAX_EVOLUTION = 4
EVOLVE_LEVEL_CAP = [14, 24, 36, 42]
PET_LEVEL_UP_AWARD = [25, 37]

FARM_DURATION = timedelta(minutes=30)
AWAKE_DURATION = timedelta(hours=6)
SLEEP_DURATION = timedelta(hours=2)
DAY_RESET_CYCLE = timedelta(hours=24)
PET_UPDATE_PERIOD = timedelta(minutes=10)
SICK_ROLL_PERIOD = timedelta(minutes=20)
BOOST_DURATION = timedelta(days=3)


NEW_PLAYER = {
    "reminder_code": None,
    "game_ticket": 0,
    "ticket": 1000,
    "diamond": 0,
    "accumulated_point": 0,
    "milestone": 0,
    "last_claimed_reward": date.today(),
    "day_collected": 0,
    "is_tutorial_done": False,
    "tutorial_phrase": 0
}

