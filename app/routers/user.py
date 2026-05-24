from fastapi import APIRouter

from app.api.dependencies import userServiceDep
from app.schemas.schemas import UserCreate, UserLogin, UserRead

router = APIRouter()


@router.post("/signup", response_model=UserRead)
async def signup(user_create: UserCreate, service: userServiceDep):
    return await service.signup(user_create)


@router.post("/login")
async def login(user: UserLogin, service: userServiceDep):
    return await service.login(user)
