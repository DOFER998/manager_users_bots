from enum import Enum
from typing import Annotated

from beanie import Document, Indexed
from pydantic import Field


class RolesEnum(str, Enum):
    user = 'user'
    admin = 'admin'
    owner = 'owner'


class UserModel(Document):
    id: int
    username: Annotated[str, Indexed(unique=True)]
    role: RolesEnum = Field(default=RolesEnum.user)

    class Settings:
        name = 'users'
