from fastapi import APIRouter

router = APIRouter(
    tags=["Products"],
)


@router.get("")
async def get_products():
    return {"products": ["Product 1", "Product 2"]}
