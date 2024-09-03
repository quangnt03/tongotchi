from app.services import player as PlayerService, \
    item as ItemService, \
    pet as PetService
from app.handler import exceptions
from app.config import constants
from app.config.enum import *

async def complete_activity(
    telegram_code: str, 
    pet_id: int, 
    action: ACTIVITY_CATEGORY, 
    item_id: int | None = None
):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException({"message": "No such pet with that id"})

    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase < 2:
        raise exceptions.InvalidBodyException({"message": "Pet is stil in egg form or being hatched"})
    if pet.sickness and action != ACTIVITY_CATEGORY.CURE:
        raise exceptions.InvalidBodyException({"message": "Pet is suffering from a sickness"})
    if not pet.sickness and action == ACTIVITY_CATEGORY.CURE:
        raise exceptions.InvalidBodyException({"message": "Pet is not sick"})
    if pet.is_sleeping:
        raise exceptions.InvalidBodyException({"message": "Pet is asleep"})
    
    item, item_detail = None
    item = None
    if action not in [ACTIVITY_CATEGORY.BATH, ACTIVITY_CATEGORY.CLEAN]:
        item = await ItemService.find_item(player, item_id)
        if item is None:
            raise exceptions.InvalidBodyException({"message": "No such item with that id"})
        item_detail = ItemService.get_local_item(item_id)
        try:
            await item.use_item()
        except exceptions.BrokenItemException:
            await item.delete()
            raise exceptions.InvalidBodyException({"message": "The item for action is already broken"})
                
    stat, daily_stat = 0
    if action == ACTIVITY_CATEGORY.BATH:
        stat = pet.hygiene_value
        daily_stat = pet.today_clean_exp
    elif action == ACTIVITY_CATEGORY.CLEAN:
        if pet.poop_count == 0:
            raise exceptions.InvalidBodyException({"message": "No poop to clean"})
        stat = pet.poop_count
        daily_stat = pet.today_clean_exp
    elif action == ACTIVITY_CATEGORY.PLAY:
        stat = pet.happy_value
        daily_stat = pet.today_play_exp
    elif action == ACTIVITY_CATEGORY.FEED:
        stat = pet.hunger_value
        daily_stat = pet.today_feed_exp
        
    if stat >= 90:
        raise exceptions.InvalidBodyException({
            "message": "Pet statistic is already over 90",
            "pet_stat": stat
        })
    if daily_stat > constants.DAILY_XP_LIMIT:
        raise exceptions.InvalidBodyException({
            "message": "Pet received more than daily stats limit",
            "pet_stat": stat
        })
             
    player, pet = activity_reducer(player, pet, action, item_detail)

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
    
    
def activity_reducer(
    player: PlayerService.Player,
    pet: PetService.Pet,
    action: ACTIVITY_CATEGORY,
    item_detail: ItemService.LocalItem
) ->  [PlayerService.Player, PetService.Pet]: # type: ignore

    if action == ACTIVITY_CATEGORY.BATH:
        pet.hygiene_value += ACTIVITY_STATS[ACTIVITY_CATEGORY.CLEAN]
        pet.pet_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.BATH]
        player.ticket += ACTIVITY_TICKET_MAP[ACTIVITY_CATEGORY.BATH]
    
    elif action == ACTIVITY_CATEGORY.CLEAN:
        player.ticket += ACTIVITY_TICKET_MAP[ACTIVITY_CATEGORY.CLEAN] * pet.poop_count
        pet.pet_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.CLEAN] * pet.poop_count
        pet.poop_count = 0
        
    else:
        value = item_detail["value"]
        specific_category = item_detail["specificCategory"]
        pet.pet_exp += ITEM_EXP_MAP[specific_category]
        if action == ACTIVITY_CATEGORY.PLAY:
            pet.happy_value += value        
        else:
            pet.hunger_value += value
        
    pet.health_value = pet.get_health()
    
    return [player, pet]