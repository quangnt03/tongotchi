from fastapi import FastAPI
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.config import env
from app.models.player import Player
from app.models.pet import Pet
from app.models.farm import Farm

@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(env.mongo_url)
    database = client[env.database]
    await init_beanie(database, document_models=[Player, Pet, Farm])
    print("INFO:", "Database Connection established", sep="\t")
    yield
