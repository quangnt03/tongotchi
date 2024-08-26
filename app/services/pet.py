from app.models.pet import Pet
from app.models.player import Player


async def create_pet(pet_id: int, player: Player) -> Pet:
    pet = Pet(telegram_code=player.telegram_code, pet_id=pet_id)
    await pet.save()
    return pet


async def find_pet_with_player(telegram_code: str) -> list[Pet]:
    pets = await Pet.find({"telegram_code": telegram_code}).to_list()
    return pets


async def get_pet_by_pet_id(telegram_code: str, pet_id: int):
    pet = await Pet.find_one({"telegram_code": telegram_code, "pet_id": pet_id})
    return pet


async def claim_hatch(pet: Pet):
    return pet.claim_hatch()