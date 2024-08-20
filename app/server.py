from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from dotenv import find_dotenv, load_dotenv
from app.database import lifespan
from app.routes.player import player_router
from app.middlewares.TelegramMiddleware import TelegramCodeMiddleware
from app.handler.handler import custom_exception_handler
load_dotenv(find_dotenv())

app = FastAPI(lifespan=lifespan)
app.add_exception_handler(HTTPException, custom_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(TelegramCodeMiddleware)
app.include_router(player_router)

@app.get('/')
def index():
    return {'message': 'Hello, World!'}