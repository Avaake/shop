from fastapi import APIRouter, status, Depends
from . import crud as product_crud
from api.product.schemas import (
    ProductRead,
    ProductCreate,
    ProductCategoryRead,
    ProductUpdate,
    CategoryCrate,
)
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Product
from .dependencies import product_by_id

router = APIRouter(
    tags=["Products, Category"],
)


@router.post(
    "/category", response_model=CategoryCrate, status_code=status.HTTP_201_CREATED
)
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


@router.get("/all", response_model=list[ProductRead])
async def get_products(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    product = await product_crud.get_all_products(session=session)
    return product


@router.get("/all-with-category", response_model=list[ProductCategoryRead])
async def get_products_with_categories(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    product = await product_crud.get_all_products_with_categories(session=session)
    return product


@router.patch("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await product_crud.update_product(
        session=session, product=product, product_update=product_update, partial=True
    )
