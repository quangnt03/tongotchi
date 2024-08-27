from app.config import constants
from app.services import player as PlayerService
from app.handler import exceptions

async def get_tutorial(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    return {
        "tutorial_phrase": player.tutorial_phrase,
        "is_tutorial_done": player.is_tutorial_done,
        "max_phrase": constants.MAX_TUTORIAL_PHRASES
    }

async def complete_tutorial(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if player.is_tutorial_done:
        raise exceptions.InvalidBodyException({"message": "Tutorial already completed"})
    player.tutorial_phrase += 1
    if player.tutorial_phrase == constants.MAX_TUTORIAL_PHRASES:
        player.is_tutorial_done = True
    await player.save()
    return {
        "tutorial_phrase": player.tutorial_phrase,
        "is_tutorial_done": player.is_tutorial_done,
        "max_phrase": constants.MAX_TUTORIAL_PHRASES
    }
