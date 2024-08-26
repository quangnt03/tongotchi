import random
from datetime import datetime, timedelta

def next_poop_time() -> datetime:
    return datetime.now() + timedelta(minutes=random.randint(45, 60))