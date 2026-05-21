from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers import router
from app.database import create_all_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router)
