from app.models.player import Player
from app.config import constants

async def find_player_by_telegram_code(telegram_code: str) -> Player | None:
    player = await Player.find_one(Player.telegram_code == telegram_code)
    return player if player else None

async def create_player(telegram_code: str) -> Player:
    player = Player(
        telegram_code=telegram_code,
        **constants.NEW_PLAYER
    )
    await player.save()
    return player