import random
from datetime import datetime, timedelta

def next_poop_time(start_time: datetime = datetime.now()) -> datetime:
    return start_time + timedelta(minutes=random.randint(45, 60))