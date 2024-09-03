import random
from app.config.constants import SICKNESS_PERCENT

def is_sickness() -> bool:  
    choices = []
    for i in range(100):
        if i < SICKNESS_PERCENT:
            choices.append(True)
        else:
            choices.append(False)
    return random.choice(choices)