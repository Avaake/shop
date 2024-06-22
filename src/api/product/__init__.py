__all__ = [
    "products_router",
    "products_category_router",
]

from .views_product import router as products_router
from .views_category import router as products_category_router
