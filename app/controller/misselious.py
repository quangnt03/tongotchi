from datetime import date

from app.services import player as PlayerService, \
    item as ItemService, \
    pet as PetService
from app.handler import exceptions
from app.config import constants
from app.config.enum import *

async def use_xp_potion(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException({"message": "No such pet with that id"})
    
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase < 2:
        raise exceptions.InvalidBodyException({"message": "Pet is stil in egg form or being hatched"})
    
    item = await ItemService.find_item(player, constants.XP_BOOST_ITEM_ID)
    if item is None:
        raise exceptions.InvalidBodyException({"message": "No XP Boost item found"})
    
    pet.pet_exp += constants.XP_BOOST
    item = item.use_item()
    if item.quantity > 0:
        await item.save()
    else:
        await item.delete()
    await pet.save()
    
    return {
        "pet_exp": pet.pet_exp,
        "pet_level": pet.pet_level
    }


async def use_robot_maid(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException({"message": "No such pet with that id"})

    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase < 2:
        raise exceptions.InvalidBodyException({"message": "Pet is stil in egg form or being hatched"})

    item = await ItemService.find_item(player, constants.ROBOT_MAID_ID)
    if item is None:
        raise exceptions.InvalidBodyException({"message": "No Robot-maid item found"})
    
    if pet.robot_maid is None or pet.robot_maid < date.today():
        pet.robot_maid = date.today()
    
    pet.robot_maid += constants.ROBOT_DURATION
    
    item = item.use_item()
    if item.quantity > 0:
        await item.save()
    else:
        await item.delete()
    await pet.save()
    
    return {
        "robot_maid_expiration": pet.robot_maid
    }
