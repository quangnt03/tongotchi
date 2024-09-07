from fastapi import APIRouter

from app.models.player import PlayerTelegramCode, PlayerGame
from app.controller import minigame as MinigameController

# Create an API router
game_router = APIRouter(prefix="/game", tags=['Minigame'])

@game_router.post("/start")
async def start_minigame(player: PlayerTelegramCode):
    return await MinigameController.start_minigame(player.telegram_code)


@game_router.post("/leaderboard")
async def complete_game(player: PlayerTelegramCode):
    return await MinigameController.get_leaderboard(player.telegram_code)


@game_router.post("/complete")
async def complete_game(player: PlayerGame):
    return await MinigameController.complete_minigame(player.telegram_code, player.score)