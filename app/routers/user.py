from fastapi import APIRouter

from app.api.dependencies import TokenDep, userServiceDep
from app.schemas.schemas import UserCreate, UserLogin, UserRead
from app.utils import logout_token

router = APIRouter()


@router.post("/signup", response_model=UserRead)
async def signup(user_create: UserCreate, service: userServiceDep):
    return await service.signup(user_create)


@router.post("/login")
async def login(user: UserLogin, service: userServiceDep):
    return await service.login(user)


@router.post("/logout")
async def logout(token_data: TokenDep):
    logout_token(token_data["jti"])
    return {"message": "Logged out successfully"}
