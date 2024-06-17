from fastapi import APIRouter, status

from api.product.schemas import Product, ProductCreate

router = APIRouter(
    tags=["Products"],
)


# @router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
# async def create_product(
#     product_in: ProductCreate,
# ) -> Product:
#     return


@router.get("")
async def get_product():
    return {"products": ["Product 1", "Product 2"]}
