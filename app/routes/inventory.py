from fastapi import APIRouter

from app.models.player import PlayerTelegramCode
from app.models.item import QueryItem
from app.controller import inventory as  InventoryController

inventory_router = APIRouter(prefix="/inventory", tags=['Inventory'])


@inventory_router.post("/get")
async def get_inventory(player: PlayerTelegramCode):
    return await InventoryController.get_player_inventory(player.telegram_code)


@inventory_router.post("/find")
async def find_item_in_inventory(query_item: QueryItem):
    return await InventoryController.find_inventory_item(query_item.telegram_code, query_item.item_id)
