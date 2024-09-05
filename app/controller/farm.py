from datetime import datetime, timedelta

from app.services import player as PlayerService, farm as FarmService
from app.handler import exceptions
from app.config import constants

async def get_farm_info(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    farm = await FarmService.get_farm_by_telegram(telegram_code)
    if farm is None:
        raise exceptions.InvalidBodyException({"message": "Farm not found"})
    return { 
        "start": farm.start.isoformat(),
        "end": farm.end.isoformat(),
        "now": datetime.now().isoformat(),
        "reminder_code": player.reminder_code
    }


async def start_farm(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    farm = await FarmService.get_farm_by_telegram(telegram_code)
    if farm is not None:
        raise exceptions.InvalidBodyException({
            "message": "Farming is already started",
            "now": datetime.now().isoformat(),
            "start": farm.start.isoformat(),
            "end": farm.end.isoformat(),
        })
    new_farm = await FarmService.create_new_farm(telegram_code)
    return { 
        "start": new_farm.start.isoformat(),
        "end": new_farm.end.isoformat(),
        "now": datetime.now().isoformat(),
        "reminder_code": player.reminder_code
    }

async def claim_farm(telegram_code: str, reminder_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    farm = await FarmService.get_farm_by_telegram(telegram_code)
    if farm is None:
        raise exceptions.InvalidBodyException({"message": "Farm not found"})
    if datetime.now() < farm.end:
        timeleft = farm.end - datetime.now()
        raise exceptions.InvalidBodyException({
            "message": "Farming is not yet completed",
            "now": datetime.now().isoformat(),
            "start": farm.start.isoformat(),
            "end": farm.end.isoformat(),
            "timeleft": str(timeleft)
        })
    player = player.gain_ticket(constants.FARM_AWARD)
    player.reminder_code = reminder_code
    await farm.delete()
    await player.save()
    
    return {
        "now": datetime.now().isoformat(),
        "end": farm.end.isoformat(),
        "timeleft": str(timedelta(hours=0, minutes=0, seconds=0)),
        "ticket": player.ticket
    }