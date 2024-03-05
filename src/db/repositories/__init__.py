from .users_repository import UsersRepository
from .info_repository import InfoRepository

users_repository = UsersRepository()

info_repository = InfoRepository()

__all__ = [
    'users_repository',
    'info_repository',
]
