from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    name: str
    descriptions: str
    price: int


class ProductCreate(ProductBase):
    category: str


# class ProductUpdate(BaseModel):
#     category_id: int | None = None


class ProductUpdate(BaseModel):
    name: str | None = None
    descriptions: str | None = None
    price: int | None = None
    category_id: int | None = None


class ProductRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    category_id: int


class ProductCategoryRead(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    category_name: str


class CategoryCrate(BaseModel):
    category_name: str


class CategoryRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
