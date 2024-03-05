from fastapi import APIRouter

from src.db import users_controller
from src.db.models import RolesEnum

is_admin_router = APIRouter()


@is_admin_router.get('/is_admin', name='is Admin', description='Check if user is admin')
async def is_admin(id: int):
    verification = await users_controller.get_by_id(id)
    if not verification:
        return {'success': False}
    elif verification.role in (RolesEnum.admin, RolesEnum.owner):
        return {'success': True}
    else:
        return {'success': False}
