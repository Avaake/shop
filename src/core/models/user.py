from datetime import datetime

from .base import Base
from .mixins import IntIdPkMixins
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import VARCHAR, func


class User(Base, IntIdPkMixins):
    username: Mapped[str] = mapped_column(VARCHAR(32))
    email: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    password: Mapped[bytes]
    reg_time: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.utcnow,
    )
    role: Mapped[str] = mapped_column(
        VARCHAR(5),
        default="user",
        server_default="user",
    )
