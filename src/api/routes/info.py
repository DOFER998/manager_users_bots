from fastapi import APIRouter
from pydantic import BaseModel, Field

from src import info_controller

info_router = APIRouter(prefix='/api')


class Info(BaseModel):
    info: str


class Version(BaseModel):
    version: str


@info_router.get('/info', name='info', description='Get info app')
async def get_info():
    return {'success': await info_controller.get_by_id()}


@info_router.post('/info', name='info', description='Modify info app')
async def modify_info(info: Info):
    await info_controller.update_info(info=info.info)
    return {'success': await info_controller.get_by_id()}


@info_router.patch('/version', name='version', description='Modify version app')
async def modify_version(version: Version):
    await info_controller.update_version(version=version.version)
    return {'success': await info_controller.get_by_id()}
