from datetime import datetime, timedelta
from beanie import Document
from pydantic import BaseModel
from app import utils
from app.config import constants, enum

class Pet(Document):
    telegram_code: str
    pet_id: int
    pet_phrase: int = 1
    poop_count: int = 0
    next_poop_time: datetime | None = None
    is_sleeping: bool = False
    current_background_id: int = 0
    happy_value: float = 0
    hygiene_value: float = 0
    hunger_value: float = 0
    health_value: float = 0
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
    sickness: bool = False

    def start_hatch(self):
        self.pet_phrase += 1
        self.target_hatching_time = datetime.now() + timedelta(minutes=constants.HATCH_DURATION)
        return self

    def claim_hatch(self):
        self.pet_phrase += 1
        self.next_poop_time = utils.next_poop_time()
        self.last_sleep_time = datetime.now() - timedelta(hours=2)
        self.last_saved_time = datetime.now()
        self.happy_value = 70
        self.hygiene_value = 70
        self.hunger_value = 70
        self.health_value = self.get_health() 
        return self
    
    def gain_exp(self, exp: int):
        self.pet_exp += exp
        return self
    
    
    def get_health(self) -> float:
        return self.happy_value * enum.HEALTH_INDICATOR.HAPPINESS + \
            self.hygiene_value * enum.HEALTH_INDICATOR.HYGIENE + \
            self.hunger_value * enum.HEALTH_INDICATOR.HUNGER
            
    
    def poop(self):
        if self.pet_phrase == 3 and datetime.now() >= self.next_poop_time and self.poop_count < 6:
            self.poop_count += 1
            self.next_poop_time = utils.next_poop_time(self.next_poop_time)
        return self
    
    def sleeping(self):
        if self.pet_phrase == 3:
            timediff = datetime.now() - self.last_sleep_time
            hours = timediff.seconds // 3600
            if hours % 8 < 2:
                self.is_sleeping = True
            else:
                self.is_sleeping = False
            sleep_period = (hours // 8) * 8
            self.last_sleep_time = self.last_sleep_time + timedelta(hours=sleep_period)
        return self.is_sleeping
    
    async def update_info(self):
        self.last_saved_time = datetime.now()
        self.poop().sleeping()
        self.health_value = 0.3 * self.happy_value + 0.3 * self.hunger_value + 0.4 * self.hygiene_value
        if self.health_value < 30:
            self.sickness = True
        else:
            self.sickness = False
        await self.save()
        

class QuerySinglePet(BaseModel):
    telegram_code: str
    pet_id: int
