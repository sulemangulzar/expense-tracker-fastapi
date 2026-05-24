from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.database import get_session
from app.services.expenses import ExpenseService
from app.services.user import UserService

sessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_expense_service(session: sessionDep):
    return ExpenseService(session)


def get_user_service(session: sessionDep) -> UserService:
    return UserService(session)


ServiceDep = Annotated[ExpenseService, Depends(get_expense_service)]
userServiceDep = Annotated[UserService, Depends(get_user_service)]
