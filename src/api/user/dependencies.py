from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud


async def get_user_by_id(
    session: AsyncSession = Depends(db_helper.session_getter),
    user_id: int = Annotated[int, Path],
) -> User:
    user = await crud.get_user(session, user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found",
    )
