from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from app.database import lifespan
from app.routes.farm import farm_router
from app.routes.pet import pet_router
from app.routes.player import player_router
from app.routes.tutorial import tutorial_router
from app.routes.inventory import inventory_router
from app.routes.purchase import purchase_router
from app.routes.activity import activity_router


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def custom_exception_handler(request: Request, exc: HTTPException):
    if type(exc.detail) == dict:
        return JSONResponse(
            status_code=exc.status_code,
            content={**exc.detail, "status_code": exc.status_code},
        )
    else:
        return JSONResponse(
            status_code=404,
            content={"message": "Resource unavailable", "status_code": 404},
        )


# app.add_middleware(TelegramCodeMiddleware)
app.include_router(player_router)
app.include_router(pet_router)
app.include_router(farm_router)
app.include_router(tutorial_router)
app.include_router(inventory_router)
app.include_router(purchase_router)
app.include_router(activity_router)


@app.get("/")
def index():
    return {"message": "Hello, World!"}
