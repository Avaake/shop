from fastapi import APIRouter, status, Depends
from . import crud as product_crud
from api.product.schemas import ProductRead, ProductCreate, ProductCategoryRead
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper

router = APIRouter(
    tags=["Products"],
)


@router.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def create_product(
    session: Annotated[
        AsyncSession,
        Depends(
            db_helper.session_getter,
        ),
    ],
    product_create: ProductCreate,
):
    product = await product_crud.create_products(session, product_create)
    return product


@router.get("", response_model=list[ProductRead])
async def get_products(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    product = await product_crud.get_all_products(session=session)
    return product
