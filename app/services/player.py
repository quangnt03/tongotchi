from datetime import date

from app.models.player import Player
from app.config import constants
from app.handler import exceptions

async def find_player_by_telegram_code(id) -> Player | None:
    player = await Player.find_one({ "telegram_code": id })
    return player if player else None


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


async def daily_login(player: Player) -> Player:
    if player.last_claimed_reward == date.today():
        return player
    login_day_diff = date.today() - player.last_claimed_reward
    if login_day_diff.days >= 1 or player.day_collected == constants.MAX_DAILY_STREAK:
        player.day_collected = 1
    else:
        player.day_collected += 1
    award_ticket = 0
    if player.day_collected == 1:
        award_ticket += 20
    elif player.day_collected == 2:
        award_ticket += 25
    else:
        award_ticket = (player.day_collected + 2) * constants.BASE_TICKET_FACTOR
    player.ticket += award_ticket
    player.last_claimed_reward = date.today()
    await player.save()
    return player