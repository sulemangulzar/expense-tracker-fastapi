from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.database.database import create_all_tables
from app.routers.routers import master_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )


app.include_router(master_router)
