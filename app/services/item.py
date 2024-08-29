from app.models.item import Item 
from app.models.player import Player
from app.config.item import items, Item as LocalItem


async def find_item(player: Player, item_id: int) -> Item:
    item = await Item.find(
        Item.telegram_code == player.telegram_code and Item.item_id == item_id
    ).first_or_none()
    return item


async def find_player_items(player: Player) -> list[Item]:
    items = await Item.find(
        Item.telegram_code == player.telegram_code
    ).to_list()
    return items

    
async def buy_item(player: Player, item_id: int) -> Item:
    item = await Item.find(
        Item.telegram_code == player.telegram_code and Item.item_id == item_id
    ).first_or_none()

    if item is None:
        item = await Item(item_id=item_id, telegram_code=player.telegram_code).insert()
    else:
        item.quantity += 1
        await item.save()

    return item   


def get_local_item(item_id: int) -> LocalItem:
    found_item = None
    for item in items:
        if item["Id"] == item_id and item["Active"] == 1:
            found_item = item
            break
    return found_item