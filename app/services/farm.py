from datetime import datetime

from app.models.farm import Farm

async def create_new_farm(telegram_code: str):
    farm = Farm(telegram_code=telegram_code, start=datetime.now())
    await farm.save()
    return farm

async def get_farm_by_telegram(telegram_code: str) -> Farm:
    farm = await Farm.find(Farm.telegram_code == telegram_code).first_or_none()
    return farm

