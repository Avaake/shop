from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import (
    ProductCreate,
    ProductCategoryRead,
    ProductUpdate,
    CategoryCrate,
)
from core.models import Product, Category
from sqlalchemy import select
from typing import Sequence
from fastapi import HTTPException, status
from sqlalchemy.orm import joinedload, selectinload


# CATEGORY
async def create_category(
    session: AsyncSession,
    category: CategoryCrate,
) -> Category:
    category = Category(**category.model_dump())
    session.add(category)
    await session.commit()
    return category


async def get_category_by_name(
    session: AsyncSession,
    category_name: str,
) -> int:
    stmt = select(Category.id).where(Category.category_name == category_name)
    result = await session.scalar(stmt)
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found",
        )
    return result


async def get_categories(session: AsyncSession) -> Sequence[Category]:
    stmt = select(Category).order_by(Category.id)
    result = await session.scalars(stmt)
    return result.all()


# PRODUCT
async def create_products(
    session: AsyncSession,
    product_create: ProductCreate,
) -> Product:
    category = await get_category_by_name(
        session=session,
        category_name=product_create.category,
    )
    product = Product(
        name=product_create.name,
        descriptions=product_create.descriptions,
        price=product_create.price,
        category_id=category,
    )
    session.add(product)
    await session.commit()
    return product


async def get_all_products(
    session: AsyncSession,
) -> Sequence[Product]:
    stmt = select(Product).order_by(Product.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_all_products_with_categories(
    session: AsyncSession,
) -> list[ProductCategoryRead]:
    stmt = (
        select(
            Product.name,
            Product.descriptions,
            Product.price,
            Product.id,
            Category.category_name,
        )
        .join(Category, Product.category_id == Category.id)
        .order_by(Product.id)
    )
    result = await session.execute(stmt)
    return [
        ProductCategoryRead(
            name=row[0],
            descriptions=row[1],
            price=row[2],
            id=row[3],
            category_name=row[4],
        )
        for row in result
    ]


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def update_product(
    session: AsyncSession,
    product: Product,
    product_update: ProductUpdate,
    partial: bool = False,
) -> Product:
    for name, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, name, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Product):
    await session.delete(product)
    await session.commit()
