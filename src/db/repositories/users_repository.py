from typing import List

from src.db.models import UserModel


class UsersRepository:
    def __init__(self):
        self.user = UserModel

    async def create(self, id: int, username: str) -> UserModel:
        user = self.user(id=id, username=username)
        return await user.create()

    async def get_by_id(self, id: int) -> UserModel:
        return await self.user.find_one(UserModel.id == id)

    async def get_all_role(self, role: str) -> List[UserModel]:
        return await self.user.find(UserModel.role == role).to_list()
