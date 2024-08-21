from fastapi import APIRouter
from app.models.player import PlayerTelegramCode
from app.controller import player as PlayerController
from app.models.player import PlayerTelegramCode, PlayerSocialQuest

player_router = APIRouter(prefix="/player", tags=["Player"])

@player_router.post("")
async def get_player_from_telegram(player: PlayerTelegramCode):
    return await PlayerController.get_or_create_player(player.telegram_code)

@player_router.post("/quest")
async def get_player_quest(player: PlayerTelegramCode):
    # Add logic to handle player's quests, e.g., generating a random quest for the player
    return await PlayerController.get_player_quest(player.telegram_code)

@player_router.post("/quest/complete")
async def get_player_quest(player: PlayerSocialQuest):
    # Add logic to handle player's quests,
    return await PlayerController.complete_quest(player.telegram_code, player.quest)