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
    if not pet.sickness and action == ACTIVITY_CATEGORY.CURE:
        raise exceptions.InvalidBodyException({"message": "Pet is not sick"})
    if pet.is_sleeping:
        raise exceptions.InvalidBodyException({"message": "Pet is asleep"})
    
    item_detail = None
    item = None
    if action not in [ACTIVITY_CATEGORY.BATH, ACTIVITY_CATEGORY.CLEAN]:
        item = await ItemService.find_item(player, item_id)
        if item is None:
            raise exceptions.InvalidBodyException({"message": "No such item with that id"})
        item_detail = ItemService.get_local_item(item_id)
        item = item.use_item()
                
    statistic = 0
    daily_exp = 0
    reward_exp = 0
    if action == ACTIVITY_CATEGORY.BATH:
        statistic = pet.hygiene_value
        daily_exp = pet.today_clean_exp
        reward_exp = ITEM_EXP_MAP[ACTIVITY_CATEGORY.BATH]
    elif action == ACTIVITY_CATEGORY.CLEAN:
        if pet.poop_count == 0:
            raise exceptions.InvalidBodyException({"message": "No poop to clean"})
        statistic = pet.poop_count
        daily_exp = pet.today_clean_exp
        reward_exp = ITEM_EXP_MAP[ACTIVITY_CATEGORY.CLEAN] * pet.poop_count 
    elif action == ACTIVITY_CATEGORY.PLAY:
        statistic = pet.happy_value
        daily_exp = pet.today_play_exp
        reward_exp = ITEM_EXP_MAP[item_detail["specificCategory"]]
    elif action == ACTIVITY_CATEGORY.FEED:
        statistic = pet.hunger_value
        daily_exp = pet.today_feed_exp
        reward_exp = ITEM_EXP_MAP[item_detail["specificCategory"]]
        
    if statistic >= 90:
        raise exceptions.InvalidBodyException({
            "message": "Pet statistic is already over 90",
            "pet_stat": statistic
        })
    if daily_exp + reward_exp > constants.DAILY_XP_LIMIT:
        raise exceptions.InvalidBodyException({
            "message": "Pet received more than daily exp limit",
            "pet_exp": daily_exp 
        })
             
    player, pet = activity_reducer(player, pet, action, item_detail)

    await pet.save()
    await player.save()
    if item is not None:
        if item.quantity == 0 and item.usage == item.usage_limit:
            await item.delete()
        else:
            await item.save()
        
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
    if action == ACTIVITY_CATEGORY.CURE:
        pet.sickness = False
        pet.happy_value += item_detail["value"]
        pet.hygiene_value += item_detail["value"]
        pet.hunger_value += item_detail["value"]

    if action == ACTIVITY_CATEGORY.BATH:
        player = player.gain_ticket(ACTIVITY_TICKET_MAP[ACTIVITY_CATEGORY.BATH])
        pet.pet_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.BATH]
        pet.today_clean_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.BATH]
        pet.hygiene_value += ACTIVITY_STATS[ACTIVITY_CATEGORY.CLEAN]
    
    elif action == ACTIVITY_CATEGORY.CLEAN:
        player = player.gain_ticket(ACTIVITY_TICKET_MAP[ACTIVITY_CATEGORY.CLEAN] * pet.poop_count)
        pet.pet_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.CLEAN] * pet.poop_count
        pet.today_clean_exp += ITEM_EXP_MAP[ACTIVITY_CATEGORY.CLEAN] * pet.poop_count
        pet.poop_count = 0
        
    else:
        specific_category = item_detail["specificCategory"]
        pet.pet_exp += ITEM_EXP_MAP[specific_category]
        value = item_detail["value"]
        if action == ACTIVITY_CATEGORY.PLAY:
            pet.happy_value += value        
            pet.today_play_exp += ITEM_EXP_MAP[specific_category]
        else:
            pet.hunger_value += value
            pet.today_feed_exp += ITEM_EXP_MAP[specific_category]
    
    if pet.sickness:
        pet.happy_value = 30 if pet.happy_value > 30 else pet.happy_value
        pet.hygiene_value = 30 if pet.hygiene_value > 30 else pet.hygiene_value
        pet.hunger_value = 30 if pet.hunger_value > 30 else pet.hunger_value
        
    pet.health_value = pet.get_health()
    
    return [player, pet]