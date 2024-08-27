from fastapi import APIRouter

from app.controller import tutorial as TutorialController
from app.models.player import PlayerTelegramCode

tutorial_router = APIRouter(prefix="/tutorial", tags=["Tutorial"])


@tutorial_router.post("")
async def get_tutorial(player: PlayerTelegramCode):
    return await TutorialController.get_tutorial(player.telegram_code)
@tutorial_router.post("/complete")
async def complete_tutorial(player: PlayerTelegramCode):
    return await TutorialController.complete_tutorial(player.telegram_code)
