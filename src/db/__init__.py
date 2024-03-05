from motor.motor_asyncio import AsyncIOMotorClient

from src.data import settings
from .models import UserModel, SelfBotModal, InfoModel
from .controllers import UsersController, InfoController


class MongoClient(AsyncIOMotorClient):
    def __init__(self):
        super().__init__(settings.database_url)


db_client = MongoClient()

users_controller = UsersController()
info_controller = InfoController()

__all__ = [
    'users_controller',
    'info_controller',
    'SelfBotModal',
    'InfoModel',
    'db_client',
    'UserModel',
]
