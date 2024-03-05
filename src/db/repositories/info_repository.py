from beanie.odm.operators.update.general import Set

from src.db.models import InfoModel


class InfoRepository:
    def __init__(self):
        self.info = InfoModel

    async def create(self, id: int = 1, info: str = 'Connecting...', version: str = '0.0.1') -> InfoModel:
        i = self.info(id=id, info=info, version=version)
        return await i.create()

    async def update_info(self, id: int = 1, info: str = 'Connecting...') -> InfoModel:
        return await self.info.find_one(InfoModel.id == id).update(Set({InfoModel.info: info}))

    async def update_version(self, id: int = 1, version: str = '0.0.1') -> InfoModel:
        return await self.info.find_one(InfoModel.id == id).update(Set({InfoModel.version: version}))

    async def get_by_id(self, id: int = 1) -> InfoModel:
        return await self.info.find_one(InfoModel.id == id)
