from datetime import datetime, timezone

from pydantic import EmailStr
from sqlalchemy import Column, DateTime
from sqlmodel import Field, SQLModel


class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    amount: float = Field(gt=0)
    description: str = Field(max_length=250)
    category: str
    date: datetime = Field(sa_column=Column(DateTime(timezone=True)))

    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True)),
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True)),
    )


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field()
    email: EmailStr = Field()
    password_hash: str = Field()
