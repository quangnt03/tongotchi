from datetime import datetime

from app.models.farm import Farm
from app.config import constants

async def create_new_farm(telegram_code: str):
    start = datetime.now()
    end = start + constants.FARM_DURATION
    farm = Farm(
        telegram_code=telegram_code, 
        start=start, 
        end=end
    )
    await farm.save()
    return farm

async def get_farm_by_telegram(telegram_code: str) -> Farm:
    farm = await Farm.find(Farm.telegram_code == telegram_code).first_or_none()
    return farm

