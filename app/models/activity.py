from .pet import QuerySinglePet
from app.config.enum import *

class Activity(QuerySinglePet):
    activity_type: ACTIVITY_CATEGORY
    item_id: int
