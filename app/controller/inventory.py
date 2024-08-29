from app.services import \
    player as PlayerService, \
    item as ItemService 
from app.handler import exceptions


async def get_player_inventory(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    items = await ItemService.find_player_items(player)
    return items


async def find_inventory_item(telegram_code: str, item_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    item = await ItemService.find_item(player, item_id)
    if item is None:
        raise exceptions.InvalidBodyException({"message": "No such item with that id"})
    return item