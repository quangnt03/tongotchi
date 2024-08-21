from datetime import date
DEFAULT_GAME_TICKET = 1000
NEW_PLAYER = {
    "reminder_code": None,
    "game_ticket": 0,
    "ticket": 1000,
    "diamond": 0,
    "accumulated_point": 0,
    "milestone": 0,
    "last_claimed_reward": date.today(),
    "day_collected": 1,
    "is_tutorial_done": False,
    "tutorial_phrase": 0
}