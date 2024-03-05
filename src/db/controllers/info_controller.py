from src.db.models import InfoModel
from src.db.repositories import info_repository


class InfoController:
    def __init__(self):
        self.repository = info_repository

    async def create(self, id: int = 1, info: str = 'Connecting...', version: str = '0.0.1') -> InfoModel:
        try:
            return await self.repository.create(id, info, version)
        except:
            pass

    async def get_by_id(self, id: int = 1) -> InfoModel:
        return await self.repository.get_by_id(id)

    async def update_info(self, id: int = 1, info: str = 'Connecting...') -> InfoModel:
        return await self.repository.update_info(id, info)

    async def update_version(self, id: int = 1, version: str = '0.0.1') -> InfoModel:
        return await self.repository.update_version(id, version)
