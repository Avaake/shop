from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CreateUser
from sqlalchemy import select
from core.models import User
from fastapi import status, HTTPException
from .util import hash_password

# async def get_user_by_email(session: AsyncSession, email: str):
#     stmt = select(User)


async def create_user(
    session: AsyncSession,
    user_in: CreateUser,
) -> User:
    # Перевірка, чи існує користувач з такою ж електронною адресою
    existing_user = await session.scalar(
        select(User).where(User.email == user_in.email)
    )
    print(existing_user)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email address already exists.",
        )

    # Вивід даних користувача у консоль для дебагу
    print(user_in.model_dump())
    hash_pw = hash_password(user_in.password)
    # Створення нового користувача
    user = User(username=user_in.username, email=user_in.email, password=hash_pw)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
