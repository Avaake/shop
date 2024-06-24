from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import CreateUser, UserRead
from sqlalchemy import select
from core.models import User
from fastapi import status, HTTPException
from .util import hash_password
from pydantic import EmailStr


async def get_user_by_email(
    session: AsyncSession,
    email: EmailStr,
) -> UserRead | None:
    stmt = select(User).where(User.email == email)
    user = await session.scalar(stmt)
    if user is not None:
        return UserRead(
            username=user.username,
            email=user.email,
            role=user.role,
        )
    return None


async def create_user(
    session: AsyncSession,
    user_in: CreateUser,
) -> User:
    # Перевірка, чи існує користувач з такою ж електронною адресою
    existing_user = await get_user_by_email(session, user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email address already exists.",
        )

    # Вивід даних користувача у консоль для дебагу
    hash_pw = hash_password(user_in.password)
    # Створення нового користувача
    user = User(username=user_in.username, email=user_in.email, password=hash_pw)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def get_user(session: AsyncSession, user_id: int):
    return await session.get(User, user_id)


async def delete_user(
    session: AsyncSession,
    user: User,
):
    await session.delete(user)
    await session.commit()
