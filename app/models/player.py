from beanie import Document, Link
from pydantic import BaseModel
from typing import List
from .pet import Pet
from datetime import date

class Player(Document):
    telegram_code: str
    reminder_code: str | None = None
    milestone: int
    social_quest_completed: bool
    is_tutorial_done: bool
    tutorial_phrase: int
    game_ticket: int
    ticket: int
    diamond: int
    accumulated_point: int
    pets: List[Link[Pet]] = list[Link[Pet]]()
    selected_pet: Pet | None = None
    last_claimed_reward: date
    day_collected: int
    
class PlayerTelegramCode(BaseModel):
    telegram_code: str