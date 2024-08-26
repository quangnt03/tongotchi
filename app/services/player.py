from app.models.player import Player
from app.config import constants
from app.handler import exceptions

async def find_player_by_telegram_code(id) -> Player | None:
    try:
        player = await Player.find_one({ "telegram_code": id })
        return player if player else None
    except Exception as e:
        print(e)

async def get_player_or_not_found(telegram_code: str) -> Player:
    player = await find_player_by_telegram_code(telegram_code)
    if player is None:
        raise exceptions.InvalidBodyException({
            "message": "Player not found",
        })
    return player

async def create_player(telegram_code: str) -> Player:
    player = Player(
        telegram_code=telegram_code,
        **constants.NEW_PLAYER
    )
    await player.save()
    return player

async def get_player_social_quest(player: Player) -> list[dict]:
    # Add logic to generate a social quest for the player
    quest = []
    for (index, status) in enumerate(player.social_quest_completed):
        if status:
            quest.append({
                "quest": index,
                "is_completed": status
            })
    return quest