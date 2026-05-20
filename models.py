from datetime import datetime

from sqlmodel import Field, SQLModel


class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    amount: float = Field(gt=0)
    description: str = Field(max_length=250)
    category: str
    date: datetime

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
