from typing import Dict, List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    token: str = ''
    database_url: str = ''


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8'
)


class OwnerCommands(BaseSettings):
    commands: Dict[str, str] = {
        'start': '💼 Главное меню',
        'add_admin': '👨‍💼✅ Добавить админа',
        'del_admin': '👨‍💼❌ Удалить админа',
        'add_self_bot': '🤖➕ Добавить бота',
        'del_self_bot': '🤖➖ Удалить бота',
        'list_self_bots': '🤖👥 Список ботов',
        'mailing': '📧 Рассылка',
        'reset_commands': '🔁 Перезагрузить команды',
    }


owner_commands = OwnerCommands()


class AdminCommands(BaseSettings):
    commands: Dict[str, str] = {
        'start': '💼 Главное меню',
        'add_self_bot': '🤖➕ Добавить бота',
        'del_self_bot': '🤖➖ Удалить бота',
        'list_self_bots': '🤖👥 Список ботов',
        'mailing': '📧 Рассылка',
    }


admin_commands = AdminCommands()
