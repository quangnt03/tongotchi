from app.services import player as PlayerService
from app.handler import exceptions



async def start_minigame(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if player.game_ticket == 0:
        raise exceptions.InvalidBodyException({
            "message": "No game ticket to start"
        })

    player.game_ticket -= 1
    player.in_game = True
    await player.save()

    return {
        "in_game": player.in_game,
        "game_ticket": player.game_ticket,
        "score": player.game_point,
    }


async def complete_minigame(telegram_code: str, score: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    # if not player.in_game:
    #     raise exceptions.InvalidBodyException({"message": "Player has not in game"})
    
    player.game_point += score
    player.gain_ticket(score)
    player.in_game = False
    
    await player.save()
    
    return {    
        "in_game": player.in_game,
        "game_ticket": player.game_ticket,
        "score": player.game_point,
        "ticket": player.ticket
    }



async def get_leaderboard(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)

    leaderboard, player_position = await PlayerService.get_game_leaderboard(player)

    formatted_leaderboard = []

    for position, top_player in enumerate(leaderboard):
        formatted_leaderboard.append({
            "telegram_code": top_player.telegram_code,
            "game_point": top_player.game_point,
            "position": position + 1
        })

    return {
        "leaderboard": formatted_leaderboard,
        "player_position": player_position + 1
    }