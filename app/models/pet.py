from datetime import datetime, timedelta
from beanie import Document
from pydantic import BaseModel
from app import utils
from app.config import constants

class Pet(Document):
    telegram_code: str
    pet_id: int
    pet_phrase: int = 1
    poop_count: int = 0
    next_poop_time: datetime | None = None
    current_background_id: int = 0
    happy_value: float = 100
    hygiene_value: float = 100
    hunger_value: float = 100
    health_value: float = 100
    target_hatching_time: datetime | None = None
    pet_level: int = 0
    pet_evolve_level: int = 0
    pet_exp: float = 0
    last_saved_time: datetime = datetime.now()
    last_sleep_time: datetime | None = None
    today_feed_exp: int = 0
    today_play_exp: int = 0
    today_clean_exp: int = 0
    today_boost_exp: int = 0

    def start_hatch(self):
        self.pet_phrase += 1
        self.target_hatching_time = datetime.now() + timedelta(minutes=constants.HATCH_DURATION)
        return self

    def claim_hatch(self):
        self.pet_phrase += 1
        self.next_poop_time = utils.next_poop_time()
        self.last_sleep_time = datetime.now()
        self.last_saved_time = datetime.now()
        return self

class QuerySinglePet(BaseModel):
    telegram_code: str
    pet_id: int
