from datetime import datetime, timedelta
from pydantic import BaseModel
from beanie import Document
from app.config import constants

class Farm(Document):
    telegram_code: str
    start: datetime = datetime.now()
    end: datetime = datetime.now() + constants.FARM_DURATION
       
class FarmRequest(BaseModel):
    telegram_code: str
    reminder_code: str