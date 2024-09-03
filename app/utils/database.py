import os
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.player import Player
from app.models.pet import Pet
from app.models.farm import Farm
from app.models.item import Item


async def connect():
    client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
    database = client[os.getenv("DATABASE")]
    await init_beanie(database, document_models=[Player, Pet, Farm, Item])
    print("INFO:", "    Database Connection established", sep="\t")