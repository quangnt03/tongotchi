from beanie import Document
from pydantic import BaseModel
from typing import List
from datetime import date
from app.config import constants

class Player(Document):
    telegram_code: str
    reminder_code: str | None = None
    milestone: int
    social_quest_completed: List[bool] = [False, False, False, False, False]
    is_tutorial_done: bool
    tutorial_phrase: int
    game_ticket: int
    ticket: int
    diamond: int
    accumulated_point: int
    pets: List[int] = set[int]()
    pet_slot: int = constants.NORMAL_PET_SLOT
    selected_pet: int | None = None
    last_claimed_reward: date
    day_collected: int
    
    
class PlayerTelegramCode(BaseModel):
    telegram_code: str
    
class PlayerSocialQuest(PlayerTelegramCode):
    quest: int