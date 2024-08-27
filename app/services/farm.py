from app.models.farm import Farm, FarmResponse

async def create_new_farm(telegram_code: str) -> FarmResponse:
    farm = Farm(telegram_code=telegram_code)
    await farm.save()
    return farm

async def get_farm_by_telegram(telegram_code: str) -> Farm:
    farm = await Farm.find(Farm.telegram_code == telegram_code).first_or_none()
    return farm

