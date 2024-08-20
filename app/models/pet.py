from beanie import Document
from datetime import datetime
class Pet(Document):
    pet_pharse: int
    poop_count: int
    next_poop_time: int
    poop_elapsed_time: float
    current_background_id: int
    happy_value: float
    hygiene_value: float
    hunger_value: float
    health_value: float
    target_hatching_time: datetime
    pet_level: int
    pet_evolve_level: int
    pet_exp: float
    last_saved_time: datetime
    last_sleep_time: datetime
    today_feed_exp: int
    today_play_exp: int
    today_clean_exp: int
    today_boost_exp: int