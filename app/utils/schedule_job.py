from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app.controller.activity import activate_robot
from app.models.pet import Pet

async def update_pet():
    pets = await Pet.find_all().to_list()
    for pet in pets:
        await pet.update_info()
        await activate_robot(pet)
    print("INFO:\t", f" Pet updated at {datetime.now().isoformat()}")


async def init_schedule() -> AsyncIOScheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_pet, trigger=IntervalTrigger(minutes=1))
    return scheduler
