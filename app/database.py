from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.utils import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await database.connect()
        yield
    finally:
        exit()
