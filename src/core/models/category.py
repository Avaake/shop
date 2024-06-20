from .base import Base
from .mixins import IntIdPkMixins
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR


class Category(Base, IntIdPkMixins):
    __tablename__ = "categories"
    category_name: Mapped[str] = mapped_column(VARCHAR(100))
