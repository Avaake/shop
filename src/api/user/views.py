from fastapi import APIRouter, status, Depends
from .schemas import CreateUser
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from . import crud as user_crud

router = APIRouter(
    tags=["Users"],
)


@router.post("", status_code=status.HTTP_201_CREATED)
async def register_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user: CreateUser,
):
    user = await user_crud.create_user(session=session, user_in=user)
    return {"user": f"{user.username, user.email} register"}
