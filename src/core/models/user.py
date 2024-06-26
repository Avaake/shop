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
    active: Mapped[bool] = mapped_column(default=True, server_default="1")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, pw={self.password!r}, "
            f"email={self.email!r}, reg_time={self.reg_time!r}, role={self.role!r},)"
        )

    def __repr__(self):
        return str(self)
