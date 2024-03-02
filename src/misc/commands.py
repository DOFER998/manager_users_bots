from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat

from src.data import owner_commands, admin_commands
from src.db.models import RolesEnum
from src.db.repositories import users_repository


async def set_commands(bot: Bot):
    owners = await users_repository.get_all_role(RolesEnum.owner)
    for owner in owners:
        try:
            await bot.set_my_commands(
                [
                    BotCommand(command=command, description=description)
                    for command, description in owner_commands.commands.items()
                ],
                scope=BotCommandScopeChat(chat_id=owner.id)
            )
        except:
            pass
    admins = await users_repository.get_all_role(RolesEnum.admin)
    for admin in admins:
        try:
            await bot.set_my_commands(
                [
                    BotCommand(command=command, description=description)
                    for command, description in admin_commands.commands.items()
                ],
                scope=BotCommandScopeChat(chat_id=admin.id)
            )
        except:
            pass


async def remove_commands(bot: Bot):
    owners = await users_repository.get_all_role(RolesEnum.owner)
    for owner in owners:
        try:
            await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=owner.id))
        except:
            pass
    admins = await users_repository.get_all_role(RolesEnum.admin)
    for admin in admins:
        try:
            await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id=admin.id))
        except:
            pass


async def reset_commands(bot: Bot):
    await remove_commands(bot)
    await set_commands(bot)
