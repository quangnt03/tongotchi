from app.services import player as PlayerService

async def get_or_create_player(telegram_code: str):
    """
    This function checks if a player with the given telegram_code already exists in the database.
    If not, it creates a new Player document with default values.
    """
    player_in_db = await PlayerService.find_player_by_telegram_code(telegram_code)
    if not player_in_db:
        player_in_db = await PlayerService.create_player(telegram_code)
    return player_in_db