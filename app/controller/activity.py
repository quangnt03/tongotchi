from app.services import player as PlayerService, \
    item as ItemService, \
    pet as PetService
from app.handler import exceptions
from app.config.enum import *

async def complete_activity(telegram_code: str, pet_id: int, action: ACTIVITY_CATEGORY, item_id: int | None = None):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException({"message": "No such pet with that id"})

    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase < 2:
        raise exceptions.InvalidBodyException({"message": "Pet is stil in egg form or being hatched"})
    if pet.sickness:
        raise exceptions.InvalidBodyException({"message": "Pet is suffering from a sickness"})
    if pet.is_sleeping:
        raise exceptions.InvalidBodyException({"message": "Pet is asleep"})
    
    item_detail = None
    item = None
    if action not in [ACTIVITY_CATEGORY.BATH, ACTIVITY_CATEGORY.CLEAN]:
        item = await ItemService.find_item(player, item_id)
        if item is None:
            raise exceptions.InvalidBodyException({"message": "No such item with that id"})
        item_detail = ItemService.get_local_item(item_id)
    if action not in [ACTIVITY_CATEGORY.BATH, ACTIVITY_CATEGORY.CLEAN]:
        value = item_detail["value"]
        specific_category = item_detail["specificCategory"]
    stat = 0
    if action == ACTIVITY_CATEGORY.BATH:
        stat = pet.hygiene_value
        pet.hygiene_value += ACTIVITY_STATS[ACTIVITY_CATEGORY.CLEAN]
        pet.pet_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.BATH]
        player.ticket += ACTIVITY_TICKET_MAP[ACTIVITY_CATEGORY.BATH]
    elif action == ACTIVITY_CATEGORY.PLAY:
        stat = pet.happy_value
        pet.happy_value += value
        pet.pet_exp += ITEM_EXP_MAP[specific_category]
    elif action == ACTIVITY_CATEGORY.FEED:
        stat = pet.hunger_value
        pet.hunger_value += value
        pet.pet_exp += ITEM_EXP_MAP[specific_category]
    elif action == ACTIVITY_CATEGORY.CLEAN:
        if pet.poop_count == 0:
            raise exceptions.InvalidBodyException({
                "message": "Unable to perform action because there is no poop",
            })
        stat = pet.poop_count
        player.ticket += ACTIVITY_TICKET_MAP[ACTIVITY_CATEGORY.CLEAN] * stat
        pet.poop_count = 0
        pet.pet_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.CLEAN] * stat
        
    
    if stat >= 90 or action == ACTIVITY_CATEGORY.CLEAN and stat == 0:
        raise exceptions.InvalidBodyException({
            "message": "Unable to perform action because stat is already over 90",
            "pet_stat": stat
        })
        
    if item is not None:
        try:
            await item.use_item()
        except exceptions.BrokenItemException:
            raise exceptions.InvalidBodyException({"message": "The item for action is already in use"})
        
    pet.health_value = pet.get_health()
    await pet.save()
    await player.save()
        
    return {
        "player_ticket": player.ticket,
        "pet_exp": pet.pet_exp,
        "pet_level": pet.pet_level,
        "hunger_value": pet.hunger_value,
        "hygiene_value": pet.hygiene_value,
        "happy_value": pet.happy_value,
        "poop_count": pet.poop_count,
        "sickness": pet.sickness,
    }
    
    
    
