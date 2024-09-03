from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.utils import database, schedule_job


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        job = await schedule_job.init_schedule()
        job.start()
        await database.connect()
        yield
    except (SystemExit, KeyboardInterrupt):
        job.shutdown()
        exit()
    finally:
        job.shutdown()
        exit()
