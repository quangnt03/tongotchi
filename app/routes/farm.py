from fastapi import APIRouter

from app.models.player import PlayerTelegramCode
from app.models.farm import FarmRequest
from app.controller import farm as FarmController

farm_router = APIRouter(prefix="/farm", tags=["Farming"])

@farm_router.post("", response_model_exclude={"id", "revision_id"})
async def get_farming_info(player: PlayerTelegramCode):
    return await FarmController.get_farm_info(player.telegram_code)


@farm_router.post("/start")
async def start_farming(player: PlayerTelegramCode):
    return await FarmController.start_farm(player.telegram_code)


@farm_router.post("/claim")
async def claim_farming(player: FarmRequest):
    return await FarmController.claim_farm(player.telegram_code, player.reminder_code)