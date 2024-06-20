from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    descriptions: str
    price: int


class ProductCreate(ProductBase):
    category: str


class ProductUpdate(ProductCreate):
    pass


class ProductUpdatePartial(ProductCreate):
    name: str | None = None
    description: str | None = None
    price: int | None = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    category_id: int


class ProductCategoryRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    category_name: str


class CategoryRead(BaseModel):
    id: int
    name: str
