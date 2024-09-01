from fastapi import APIRouter

from app.controller import activity as ActivityController
from app.models.activity import Activity

activity_router = APIRouter(prefix="/activity", tags=["Pet activity"])

@activity_router.post("")
async def complete_activity(activity: Activity):
    return await ActivityController.complete_activity(
        activity.telegram_code,
        activity.pet_id,
        activity.activity_type,
        activity.item_id
    )