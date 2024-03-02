from motor.motor_asyncio import AsyncIOMotorClient

from src.data import settings
from .models import UserModel, SelfBotModal
from .controllers import UsersController


class MongoClient(AsyncIOMotorClient):
    def __init__(self):
        super().__init__(settings.database_url)


db_client = MongoClient()

users_controller = UsersController()

__all__ = [
    'users_controller',
    'SelfBotModal',
    'db_client',
    'UserModel',
]
