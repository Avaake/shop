from pydantic import BaseModel, EmailStr
from annotated_types import MaxLen, MinLen
from typing import Annotated


class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(30)]
    email: EmailStr
    password: str
