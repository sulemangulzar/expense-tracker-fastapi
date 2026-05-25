from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import bearer_scheme
from app.database.database import get_session
from app.models.models import User
from app.services.expenses import ExpenseService
from app.services.user import UserService
from app.utils import decode_token, is_token_logged_out

sessionDep = Annotated[AsyncSession, Depends(get_session)]


async def get_access_token(
    token: Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)],
) -> dict:
    data = decode_token(token.credentials)
    jti = data.get("jti") if data else None

    if data is None or jti is None or is_token_logged_out(jti):
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return data


async def get_current_user(
    token_data: Annotated[dict, Depends(get_access_token)], session: sessionDep
) -> User:
    user = await session.get(User, token_data["user_id"])

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user


def get_expense_service(session: sessionDep) -> ExpenseService:
    return ExpenseService(session)


def get_user_service(session: sessionDep) -> UserService:
    return UserService(session)


ServiceDep = Annotated[ExpenseService, Depends(get_expense_service)]
userServiceDep = Annotated[UserService, Depends(get_user_service)]
TokenDep = Annotated[dict, Depends(get_access_token)]
CurrentUserDep = Annotated[User, Depends(get_current_user)]
