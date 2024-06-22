from fastapi import APIRouter, status, Depends
from . import crud as product_crud
from api.product.schemas import (
    CategoryCrate,
)
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

router = APIRouter(
    tags=["Category"],
)


@router.post("/", response_model=CategoryCrate, status_code=status.HTTP_201_CREATED)
async def create_category(
    session: Annotated[
        AsyncSession,
        Depends(
            db_helper.session_getter,
        ),
    ],
    category_create: CategoryCrate,
):
    category = await product_crud.create_category(session, category_create)
    return category
