from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.services.expenses import ExpenseService

sessionDep = Annotated[AsyncSession, Depends(get_session)]


def get_expense_service(session: sessionDep):
    return ExpenseService(session)


ServiceDep = Annotated[ExpenseService, Depends(get_expense_service)]
