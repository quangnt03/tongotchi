from fastapi import APIRouter
from app.models.player import PlayerTelegramCode
from app.controller import player as PlayerController

player_router = APIRouter(prefix="/player", tags=["Player"])

@player_router.post("")
async def get_player_from_telegram(player: PlayerTelegramCode):
    return await PlayerController.get_or_create_player(player.telegram_code)
