from .base import Base
from mixins import IntIdPkMixins
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR


class Product(Base, IntIdPkMixins):
    name: Mapped[str] = mapped_column(VARCHAR(100))
    descriptions: Mapped[str] = mapped_column(VARCHAR(500))
    price: Mapped[int]
