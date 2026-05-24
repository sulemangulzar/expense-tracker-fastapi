from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from app.models.models import Expense
from app.schemas.schemas import ExpenseCreate, ExpenseUpdate


class ExpenseService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> list[Expense]:
        result = await self.session.execute(select(Expense))
        return list(result.scalars().all())

    async def get(self, id: int) -> Expense:
        expense = await self.session.get(Expense, id)
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        return expense

    async def add(self, expense: ExpenseCreate) -> Expense:
        new_expense = Expense(**expense.model_dump())
        self.session.add(new_expense)
        await self.session.commit()
        await self.session.refresh(new_expense)
        return new_expense

    async def update(self, id: int, update_schema: ExpenseUpdate) -> Expense:
        expense = await self.session.get(Expense, id)
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        update_data = update_schema.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(expense, key, value)
        self.session.add(expense)
        await self.session.commit()
        await self.session.refresh(expense)
        return expense

    async def delete(self, id: int) -> dict:
        expense = await self.session.get(Expense, id)
        if not expense:
            raise HTTPException(status_code=404, detail="Expense not found")
        await self.session.delete(expense)
        await self.session.commit()
        return {"message": "Expense deleted successfully"}
