from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from dotenv import find_dotenv, load_dotenv
from app.database import lifespan
from app.routes.player import player_router
from app.middlewares.TelegramMiddleware import TelegramCodeMiddleware
load_dotenv(find_dotenv())

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(HTTPException)
async def custom_exception_handler(request: Request, exc: HTTPException):
    print("handling exception")
    if type(exc.detail) == dict:
        return JSONResponse(
            status_code=exc.status_code,
            content={
                **exc.detail,
                "status_code": exc.status_code
            },
        )
    else:
        return JSONResponse(
            status_code=404,
            content={
                "message": "Resource unavailable",
                "status_code": 404
            },
        )

# app.add_middleware(TelegramCodeMiddleware)
app.include_router(player_router)

@app.get('/')
def index():
    return {'message': 'Hello, World!'}