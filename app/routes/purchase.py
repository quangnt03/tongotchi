from fastapi import APIRouter
from app.models.player import PlayerPurchase
from app.models.item import QueryItem
from app.controller import purchase as PurchaseController

purchase_router = APIRouter(prefix="/purchase", tags=["Buy items"])

@purchase_router.post("/ticket")
async def purchase_ticket(player: PlayerPurchase):
    return await PurchaseController.purchase_ticket(player.telegram_code, player.quantity)


@purchase_router.post("/diamond")
async def purchase_diamond(player: PlayerPurchase):
    return await PurchaseController.purchase_diamond(player.telegram_code, player.quantity)


@purchase_router.post("/petslot")
async def purchase_petslot(player: PlayerPurchase):
    return await PurchaseController.purchase_pet_slot(player.telegram_code, player.quantity)

@purchase_router.post("/item")
async def purchase_item(query: QueryItem):
    return await PurchaseController.purchase_item(query.telegram_code, query.pet_id, query.item_id)
