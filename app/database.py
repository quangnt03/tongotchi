from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.utils import database, schedule_job


@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler = None
    try:
        await database.connect()
        # Start the scheduler
        scheduler = await schedule_job.init_schedule()
        scheduler.start()
        yield
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        exit()
    finally:
        scheduler.shutdown()
        exit()
