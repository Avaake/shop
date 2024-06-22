from fastapi import APIRouter
from .product import products_router, products_category_router
from .user import users_router

router = APIRouter(
    prefix="/api",
)
router.include_router(
    products_router,
    prefix="/products",
)


router.include_router(
    products_category_router,
    prefix="/category",
)

router.include_router(
    users_router,
    prefix="/users",
)
