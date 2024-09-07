from fastapi import APIRouter

from app.models.player import PlayerTelegramCode, PlayerMilestone
from app.controller import player as PlayerController

milestone_router = APIRouter(prefix="/milestone", tags=['Milestone'])

@milestone_router.post("")
async def get_milestones(player: PlayerTelegramCode):
    return await PlayerController.get_player_milestone(player.telegram_code)


@milestone_router.post("/complete")
async def complete_milestone(player: PlayerMilestone):
    return await PlayerController.complete_milestone(player.telegram_code, player.accumulated_point)