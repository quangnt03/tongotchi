import random
from datetime import datetime, timedelta

from app.config import constants
from app.config.level import LEVEL_REWARD
from app.handler import exceptions
from app.services import player as PlayerService, pet as PetService, item as ItemService


async def get_all_pets_with_telegram(telegram_code: str):
    await PlayerService.get_player_or_not_found(telegram_code)
    pets = await PetService.find_pet_with_player(telegram_code)
    return pets


async def get_single_pet_with_telegram(telegram_code: str, pet_id: int):
    await PlayerService.get_player_or_not_found(telegram_code)
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet == None:
        raise exceptions.InvalidBodyException({"message": "No such pet with that id"})
    return pet


async def get_new_pet(telegram_code: str):
    target_player = await PlayerService.get_player_or_not_found(telegram_code)

    if len(target_player.pets) == target_player.pet_slot:
        raise exceptions.InvalidBodyException(
            {"message": "You have reached the limit of your pets."}
        )

    possible_pet_id = []

    for pet_id in range(constants.MAX_PET_SLOT):
        if pet_id not in target_player.pets:
            possible_pet_id.append(pet_id)

    pet_id = random.choice(possible_pet_id)

    new_pet = await PetService.create_pet(pet_id, target_player)

    target_player.pets.append(pet_id)

    await new_pet.save()
    await target_player.save()

    return new_pet


async def hatch_pet(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException(
            {"message": "Player does not own pet with such id"}
        )
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase == 0:
        raise exceptions.InvalidBodyException({"message": "Pet is stil in egg form"})
    if pet.pet_phrase > 1:
        raise exceptions.InvalidBodyException({"message": "The selected pet is being hatched"})
    pet = pet.start_hatch()
    await pet.save()
    return pet


async def pet_sickness_status(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException(
            {"message": "Player does not own pet with such id"}
        )
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    return {
        "sickness": pet.sickness,
        "health": pet.health_value,
        "hunger": pet.hunger_value,
        "hygiene": pet.hygiene_value,
        "happiness": pet.happy_value,
    }
    

async def claim_hatched_pet(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException(
            {"message": "Player does not own pet with such id"}
        )
    if pet.pet_phrase == 0:
        raise exceptions.InvalidBodyException(
            {"message": f"Player has not started hatching pet{pet_id}"}
        )
    if pet.pet_phrase == 3:
        raise exceptions.InvalidBodyException(
            {"message": f"Pet{pet_id} has been hatched already"}
        )

    if datetime.now() < pet.target_hatching_time:
        remaining = pet.target_hatching_time - datetime.now()
        raise exceptions.InvalidBodyException(
            {
                "message": f"Hatching has not yet completed with pet#{pet_id}",
                "now": datetime.now().isoformat(),
                "target_time": pet.target_hatching_time.isoformat(),
                "time_left": str(remaining),
            }
        )
    pet = pet.claim_hatch()
    player = player.gain_ticket(constants.HATCH_COMPLETE_AWARD)
    await pet.save()
    await player.save()
    return {
        "pet": pet,
        "now": datetime.now().isoformat(),
        "target_time": pet.target_hatching_time,
        "time_left": str(timedelta(hours=0, minutes=0)),
    }


async def level_up_pet(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException(
            {"message": "Player does not own pet with such id"}
        )
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase < 3:
        raise exceptions.InvalidBodyException(
            {"message": "Pet is not yet being hatched"}
        )
    
    if pet.pet_level == constants.PET_MAX_LEVEL:
        raise exceptions.InvalidBodyException({
            "message": "Pet is already at maximum level",
            "pet_level": pet.level
        })
        
    next_level = LEVEL_REWARD[pet.pet_level + 1]
    if next_level['exp'] > pet.pet_exp:
        raise exceptions.InvalidBodyException({
            "message": "Pet does not have enough exp to level up",
            "pet_exp": pet.pet_exp,
            "next_level_exp": next_level['exp']
        })
    if next_level["evolution"] > pet.pet_evolve_level:
        raise exceptions.InvalidBodyException({
            "message": "Pet needs to evolve to level up",
            "pet_evolve_level": pet.pet_evolve_level,
            "next_level_evolution": next_level["evolution"]
        })
        
    pet.pet_level += 1
    player.diamond += next_level["diamonds"]
    player = player.gain_ticket(next_level["tickets"])
    
    await pet.save()
    await player.save()
    
    return {
        "ticket": player.ticket,
        "diamond": player.diamond,
        "pet_level": pet.pet_level,
        "pet_exp": pet.pet_exp,
        "pet_evolve_level": pet.pet_evolve_level,
    }


async def evolve_pet(telegram_code: str, pet_id: int):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if pet_id not in player.pets:
        raise exceptions.InvalidBodyException(
            {"message": "Player does not own pet with such id"}
        )
    pet = await PetService.get_pet_by_pet_id(telegram_code, pet_id)
    if pet.pet_phrase < 3:
        raise exceptions.InvalidBodyException(
            {"message": "Pet is not yet being hatched"}
        )
    
    if pet.pet_level == constants.PET_MAX_EVOLUTION:
        raise exceptions.InvalidBodyException({
            "message": "Pet is already at maximum evolution",
            "pet_evolution_level": pet.pet_evolve_level
        })
        
    next_level = LEVEL_REWARD[pet.pet_level + 1]
    if next_level["evolution"] == pet.pet_evolve_level:
        raise exceptions.InvalidBodyException({
            "message": "Pet pet needs to be at specified level",
            "pet_evolve_level": pet.pet_exp,
            "pet_level_evolution": next_level["evolution"]
        })
     
    evolve_potion = await ItemService.find_item(player, constants.EVOLVE_POTION_ID)
    
    if evolve_potion is None:
        raise exceptions.InvalidBodyException({
            "message": "Evolution requires evolve potion"
        })
       
    pet.pet_level = next_level["level"]
    pet.pet_evolve_level = next_level["evolution"]
    player.diamond += next_level["diamonds"]
    player = player.gain_ticket(next_level["tickets"])
    
    await evolve_potion.use_item().save()
    await player.save()
    await pet.save()
    
    return {
        "ticket": player.ticket,
        "diamond": player.diamond,
        "pet_level": pet.pet_level,
        "pet_exp": pet.pet_exp,
        "pet_evolve_level": pet.pet_evolve_level,
    }