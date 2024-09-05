from datetime import datetime, timedelta
from beanie import Document
from pydantic import BaseModel
from app import utils
from app.config import constants, enum
from app.services import player as PlayerService

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
    last_write_db: datetime = datetime.now()
    last_sleep_time: datetime | None = None
    last_sick_roll: datetime | None = None
    last_statistic_update: datetime | None = None
    today_feed_exp: int = 0
    today_play_exp: int = 0
    today_clean_exp: int = 0
    today_boost_exp: int = 0
    sickness: bool = False
    is_alive: bool = True


    def start_hatch(self):
        self.pet_phrase += 1
        self.target_hatching_time = datetime.now() + timedelta(minutes=constants.HATCH_DURATION)
        return self


    def claim_hatch(self):
        self.pet_phrase += 1
        self.next_poop_time = utils.next_poop_time()
        self.last_sleep_time = datetime.now() - constants.SLEEP_DURATION
        self.last_saved_time = datetime.now()
        self.last_statistic_update = datetime.now()
        self.last_write_db = datetime.now()
        self.happy_value = 70
        self.hygiene_value = 70
        self.hunger_value = 70
        self.health_value = self.get_health() 
        return self

    
    def gain_exp(self, exp: int):
        self.pet_exp += exp
        return self
    
    
    def get_health(self) -> float:
        return self.happy_value * 0.3 + \
            self.hygiene_value * 0.4 + \
            self.hunger_value * 0.3
            
    
    def poop(self):
        if datetime.now() >= self.next_poop_time and self.poop_count < 6:
            self.poop_count += 1
            self.next_poop_time = utils.next_poop_time(self.next_poop_time)
        return self
    
    
    def sleeping(self):
        timediff = datetime.now() - self.last_sleep_time
        hours = timediff.seconds // 3600
        if hours % 8 < 2:
            self.is_sleeping = True
        else:
            self.is_sleeping = False
        sleep_period = (hours // 8) * 8
        self.last_sleep_time = self.last_sleep_time + timedelta(hours=sleep_period)
        return self

    
    def reset_stat(self):
        if datetime.now() - self.last_saved_time >= constants.DAY_RESET_CYCLE:
            self.today_feed_exp = 0
            self.today_play_exp = 0
            self.today_clean_exp = 0
            self.today_boost_exp = 0
            self.last_saved_time = datetime.now()
        
        statistic_update_period = datetime.now() - self.last_statistic_update
        statistic_update_by_mins = statistic_update_period.total_seconds() // 60
        
        if statistic_update_period >= constants.PET_UPDATE_PERIOD:
            self.happy_value -= constants.STAT_DECLINE_PER_MINUTE * statistic_update_by_mins
            self.hygiene_value -= constants.STAT_DECLINE_PER_MINUTE * statistic_update_by_mins
            self.hunger_value -= constants.STAT_DECLINE_PER_MINUTE * statistic_update_by_mins
            self.last_statistic_update = datetime.now()
        
        return self
    

    def sickroll(self):
        if self.health_value < 30 and not self.sickness:
            if self.last_sick_roll == None \
                or datetime.now() - self.last_sick_roll >= constants.SICK_ROLL_PERIOD:
                self.sickness = utils.is_sickness()
                self.last_sick_roll = datetime.now()
        return self

    
    async def update_info(self):
        if self.pet_phrase == 3 and self.is_alive:
            self.reset_stat().poop().sleeping().sickroll()
            self.health_value = self.get_health()
            if self.health_value <= 0:
                return await self.die()
            else:
                self.last_write_db = datetime.now()
                await self.save()
        return self
    
    async def die(self):
        self.is_alive = False
        player = await PlayerService.find_player_by_telegram_code(self.telegram_code)        
        player.pets.remove(self.pet_id)
        if len(player.pets) == 0:
            player.ticket += 1000
        await self.delete()
        await player.save()
        return None

class QuerySinglePet(BaseModel):
    telegram_code: str
    pet_id: int
