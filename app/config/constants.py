from datetime import date, timedelta
DEFAULT_GAME_TICKET = 1000
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
HATCH_DURATION = 30
NORMAL_PET_SLOT = 3
MAX_PET_SLOT = 5
MIN_POOP_DURATION = 45
MAX_POOP_DURATION = 60
HATCH_COMPLETE_AWARD = 1000
FARM_DURATION = timedelta(minutes=2)
FARM_AWARD = 30
MAX_TUTORIAL_PHRASES = 15
MAX_DAILY_STREAK = 7
BASE_TICKET_FACTOR = 5