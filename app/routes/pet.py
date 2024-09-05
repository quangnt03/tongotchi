from fastapi import APIRouter

from app.controller import pet as PetController
from app.models.pet import QuerySinglePet
from app.models.player import PlayerTelegramCode

pet_router = APIRouter(prefix="/pet", tags=["Pet and Egg"])


@pet_router.post("/all")
async def get_all_pet(player: PlayerTelegramCode):
    return await PetController.get_all_pets_with_telegram(player.telegram_code)


@pet_router.post("/one")
async def get_pet(query: QuerySinglePet):
    return await PetController.get_single_pet_with_telegram(
        query.telegram_code, query.pet_id
    )
    
        
@pet_router.post("/sick")
async def get_pet_sickness(query: QuerySinglePet):
    return await PetController.pet_sickness_status(
        query.telegram_code, query.pet_id
    )


@pet_router.post("/new")
async def get_new_egg(player: PlayerTelegramCode):
    return await PetController.get_new_pet(player.telegram_code)


@pet_router.post("/hatch")
async def get_hatch(player: QuerySinglePet):
    return await PetController.hatch_pet(player.telegram_code, player.pet_id)


@pet_router.post("/claim")
async def claim_hatched_pet(query: QuerySinglePet):
    return await PetController.claim_hatched_pet(query.telegram_code, query.pet_id)
