from .base import Base
from .mixins import IntIdPkMixins
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR


class Category(Base, IntIdPkMixins):
    __tablename__ = "categories"
    category_name: Mapped[str] = mapped_column(VARCHAR(100))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, category_name={self.category_name!r})"

    def __repr__(self):
        return str(self)
