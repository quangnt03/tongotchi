import random
from datetime import datetime, timedelta

from app.config.constants import SICKNESS_PERCENT

def next_poop_time(start_time: datetime = datetime.now()) -> datetime:
    return start_time + timedelta(minutes=random.randint(45, 60))


def is_sickness() -> bool:  
    choices = []
    for i in range(100):
        if i < SICKNESS_PERCENT:
            choices.append(True)
        else:
            choices.append(False)
    return random.choice(choices)

