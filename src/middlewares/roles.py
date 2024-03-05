from typing import Callable, Dict, Any, Awaitable, Optional

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject, User

from src.db import users_controller
from src.db.models import RolesEnum


class RoleOwnerMsg(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Optional[Any]:
        user: Optional[User] = data.get("event_from_user", None)

        if user is not None:
            verification = await users_controller.get_by_id(user.id)
            if verification.role == RolesEnum.owner:
                return await handler(event, data)
            else:
                return await event.delete()


class RoleOwnerCall(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any],
    ) -> Optional[Any]:
        user: Optional[User] = data.get("event_from_user", None)

        if user is not None:
            verification = await users_controller.get_by_id(user.id)
            if verification.role == RolesEnum.owner:
                return await handler(event, data)
            else:
                return await event.answer(text='❌ Not owner!', show_alert=True)


class RoleAdminMsg(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Optional[Any]:
        user: Optional[User] = data.get("event_from_user", None)

        if user is not None:
            verification = await users_controller.get_by_id(user.id)
            if verification.role in (RolesEnum.admin, RolesEnum.owner):
                return await handler(event, data)
            else:
                return await event.delete()


class RoleAdminCall(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            data: Dict[str, Any],
    ) -> Optional[Any]:
        user: Optional[User] = data.get("event_from_user", None)

        if user is not None:
            verification = await users_controller.get_by_id(user.id)
            if verification.role in (RolesEnum.admin, RolesEnum.owner):
                return await handler(event, data)
            else:
                return await event.answer(text='❌ Not admin!', show_alert=True)
