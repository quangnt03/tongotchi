from datetime import date
from typing import Union, List

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
    player = player.gain_ticket(award_ticket)
    if player.game_ticket < 5:
        player.game_ticket = 5
    player.last_claimed_reward = date.today()
    await player.save()
    return player


def get_boost(player: Player):
    if player.boost is None or player.boost < date.today():
        player.boost = date.today() 
    player.boost += constants.BOOST_DURATION
    return player


async def get_game_leaderboard(player: Player) -> Union[List[Player], int]:
    player_list = Player.find_all().sort(-Player.game_point)
    leaderboard = await player_list.limit(10).to_list()
    compare_leaderboard = await player_list.to_list()
    player_position = compare_leaderboard.index(player)
    return [leaderboard, player_position]