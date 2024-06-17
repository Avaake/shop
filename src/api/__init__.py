from fastapi import APIRouter
from .product import products_router

router = APIRouter(
    prefix="/api",
)
router.include_router(
    products_router,
    prefix="/products",
)
