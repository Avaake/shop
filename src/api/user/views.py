from fastapi import APIRouter, status, Depends, HTTPException
from .schemas import CreateUser, UserUpdate, UserRead
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, User
from . import crud as user_crud
from pydantic import EmailStr
from .dependencies import get_user_by_id

router = APIRouter(
    tags=["Users"],
)


@router.post("/create/", status_code=status.HTTP_201_CREATED)
async def register_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user: CreateUser,
):
    user = await user_crud.create_user(session=session, user_in=user)
    return {"user": f"{user.username, user.email} register"}


@router.get("/{email}/")
async def get_user_by_email(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    email: EmailStr,
):
    if user := await user_crud.get_user_by_email(session=session, email=email):
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with {email} not found",
    )


@router.delete("/{user_id}/delete/")
async def delete_user_by_id(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user: User = Depends(get_user_by_id),
):
    return await user_crud.delete_user(session=session, user=user)


@router.patch("/{user_id}/update/")
async def update_user_by_id(
    update_user: UserUpdate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user: User = Depends(get_user_by_id),
):
    return await user_crud.user_update(
        session=session, user=user, update_user=update_user
    )


@router.post("/{user_id}/")
async def get_user_by_id(
    user: User = Depends(get_user_by_id),
):
    return user
