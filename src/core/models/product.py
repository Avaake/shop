from .base import Base
from .mixins import IntIdPkMixins
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, ForeignKey


class Product(Base, IntIdPkMixins):
    name: Mapped[str] = mapped_column(VARCHAR(100))
    descriptions: Mapped[str] = mapped_column(VARCHAR(500))
    price: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, name={self.name!r}, descriptions={self.descriptions!r}, "
            f"price={self.price!r}, category_id={self.category_id!r},)"
        )

    def __repr__(self):
        return str(self)
