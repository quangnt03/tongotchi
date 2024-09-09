from datetime import datetime
from pydantic import BaseModel
from beanie import Document

class Farm(Document):
    telegram_code: str
    start: datetime 
    end: datetime 
       
class FarmRequest(BaseModel):
    telegram_code: str
    reminder_code: str