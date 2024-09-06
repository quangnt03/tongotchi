from app.services import player as PlayerService, item as ItemService, pet as PetService
from app.config import constants
from app.config.enum import *
from app.handler import exceptions

async def purchase_ticket(telegram_code: str, quantity: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if quantity <= 0:
        raise exceptions.InternalServerException({"message": "Invalid quantity"})
    
    if player.diamond < quantity:
        raise exceptions.InvalidBodyException({"message": "Not enough diamond"})
    
    player.diamond -= quantity
    player.ticket += constants.TICKET_PER_DIAMOND * quantity
    
    await player.save()
    return {
        "ticket": player.ticket,
        "diamond": player.diamond,
    }


async def purchase_diamond(telegram_code: str, quantity: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if quantity <= 0:
        raise exceptions.InternalServerException({"message": "Invalid quantity"})
    
    player.diamond += quantity
    
    await player.save()
    return {
        "diamond": player.diamond,
    }



async def purchase_pet_slot(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if player.diamond < constants.DIAMOND_PER_PETSLOT:
        raise exceptions.InternalServerException({"message": "Insufficient diamond "})
    
    if player.pet_slot == constants.MAX_PET_SLOT:
        raise exceptions.InvalidBodyException({"message": "Pet slot limit reached"})
    
    player.pet_slot += 1
    player.diamond -= constants.DIAMOND_PER_PETSLOT
    
    await player.save()
    return {
        "diamond": player.diamond,
        "pet_slot": player.pet_slot,
    }


async def purchase_item(telegram_code: str, pet_id: int | None, item_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    item = ItemService.get_local_item(item_id)
    if item is None:
        raise exceptions.InvalidBodyException({"message": "Item not found"})
    currency = 0
    if item["currencyType"] == 2:
        currency = player.ticket
    else:
        currency = player.diamond
    if currency < item["price"]:
        raise exceptions.InvalidBodyException({"message": "Insufficient currency to purchase"})
    
    currency -= item["price"]
    pet = None
    current_item = None
    if item["category"] < 3 or item_id == constants.EVOLVE_POTION_ID:
        current_item = await ItemService.buy_item(player, item_id)
    elif item["Id"] == constants.TICKET_BOOST_ITEM_ID:
        player = PlayerService.get_boost(player)
    elif item["Id"] == constants.XP_BOOST_ITEM_ID:
        pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
        pet.pet_exp += constants.XP_BOOST
        
    currencyType = "ticket"
    
    if item["currencyType"] == 2:
        player.ticket = currency
    else:
        player.diamond = currency
        currencyType = "diamond"
        
    await player.save()
    if pet is not None:
        await pet.save()
        
    if current_item is not None:
        return {"item": current_item, currencyType: currency}
    elif item_id == constants.TICKET_BOOST_ITEM_ID:
        return {
            currencyType: currency, 
            "boost_until": player.boost.isoformat()
        }
    elif item["Id"] == constants.XP_BOOST_ITEM_ID:
        return {
            currencyType: currency,
            "pet_id": pet_id, 
            "pet_exp": pet.pet_exp,
        }