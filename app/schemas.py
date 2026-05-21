from datetime import datetime

from sqlmodel import SQLModel


class ExpenseCreate(SQLModel):
    amount: float
    description: str
    category: str
    date: datetime


class ExpenseRead(SQLModel):
    id: int
    amount: float
    description: str
    category: str
    date: datetime
    created_at: datetime
    updated_at: datetime


class ExpenseUpdate(SQLModel):
    amount: float | None = None
    description: str | None = None
    category: str | None = None
    date: datetime | None = None
