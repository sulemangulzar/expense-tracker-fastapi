from fastapi import APIRouter

from ..routers import expenses, user

master_router = APIRouter()

master_router.include_router(expenses.router)
master_router.include_router(user.router)
