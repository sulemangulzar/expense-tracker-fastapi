from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlmodel import col, select

from app.models.models import User
from app.schemas.schemas import UserCreate, UserLogin
from app.utils import create_access_token

password_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def signup(self, creds: UserCreate):
        existing_user = await self.session.execute(
            select(User).where(col(User.email) == str(creds.email))
        )

        if existing_user.scalar_one_or_none():
            raise HTTPException(status_code=409, detail="Email already registered")

        user = User(
            **creds.model_dump(exclude={"name", "email", "password"}),
            name=creds.name,
            email=str(creds.email),
            password_hash=password_context.hash(creds.password),
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def login(self, creds: UserLogin):
        result = await self.session.execute(
            select(User).where(col(User.email) == str(creds.email))
        )
        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(status_code=401, detail="Invalid email or password")

        if not password_context.verify(creds.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_access_token({"user_id": user.id, "email": user.email})
        return {"access_token": token, "token_type": "bearer"}
