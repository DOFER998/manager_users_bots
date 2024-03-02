from typing import List

from src.db.models import UserModel
from src.db.repositories import users_repository


class UsersController:
    def __init__(self):
        self.repository = users_repository

    async def create(self, id: int, username: str) -> UserModel:
        try:
            return await self.repository.create(id, username)
        except:
            pass

    async def get_by_id(self, id: int) -> UserModel:
        return await self.repository.get_by_id(id)

    async def get_all_role(self, role: str) -> List[UserModel]:
        users = await self.repository.get_all_role(role)
        return users
