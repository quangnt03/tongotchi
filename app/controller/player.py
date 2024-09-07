from datetime import datetime
from fastapi.responses import JSONResponse
from app.services import player as PlayerService, pet as PetService
from app.handler import exceptions
from app.config import constants
# from app.dependencies.auth import PlayerAuthenticationDep

async def get_or_create_player(telegram_code: str):
    """
    This function checks if a player with the given telegram_code already exists in the database.
    If not, it creates a new Player document with default values.
    """
    player_in_db = await PlayerService.find_player_by_telegram_code(telegram_code)
    if not player_in_db:
        player_in_db = await PlayerService.create_player(telegram_code)
    else:
        player = await PlayerService.daily_login(player_in_db)
        pets = await PetService.find_pet_with_player(telegram_code)
        player_in_db = {**player.__dict__, "pets": pets}

    return player_in_db

async def get_player_quest(telegram_code: str):
    player = await PlayerService.get_player_or_not_found(telegram_code)
    
    quest = []
    for (index, status) in enumerate(player.social_quest_completed):
        if status:
            quest.append({
                "quest": index,
                "is_completed": status
            })
    return quest

async def complete_quest(telegram_code: str, quest: int):
    if quest not in range(5):
        raise exceptions.InvalidBodyException({
            "message": "Unknown social quest"
        })
        
    player = await PlayerService.get_player_or_not_found(telegram_code)
    if player.social_quest_completed[quest]:
        raise exceptions.InvalidBodyException({
            "message": "Quest already completed"
        })
        
    player.social_quest_completed[quest] = True
    player = player.gain_ticket(constants.SOCIAL_QUEST_TICKET_REWARD)
 
    no_completed_quest = 0 
    for status in player.social_quest_completed:
        if status:
            no_completed_quest += 1
            
    if no_completed_quest == len(player.social_quest_completed):
        pet_list = await PetService.find_pet_with_player(telegram_code)
        for pet in pet_list:
            if pet.pet_phrase == 2 and pet.target_hatching_time > datetime.now():
                pet.target_hatching_time = datetime.now()
                await pet.save()
                break
            
    await player.save()
    return JSONResponse({
        "status_code": 200,
        "quest": quest,
        "is_completed": True,
        "completed_quests": no_completed_quest
    })