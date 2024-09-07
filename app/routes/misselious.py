from fastapi import APIRouter

from app.controller import misselious as MisseliousController
from app.models.pet import QuerySinglePet

misselious_router = APIRouter(prefix="/misselious", tags=["Use misselious (XP Potion and Robot maid)"])


@misselious_router.post("/xp-potion")
async def use_xp_potion(query: QuerySinglePet):
    return await MisseliousController.use_xp_potion(query.telegram_code, query.pet_id)

@misselious_router.post("/robot-maid")
async def use_xp_potion(query: QuerySinglePet):
    return await MisseliousController.use_robot_maid(query.telegram_code, query.pet_id)