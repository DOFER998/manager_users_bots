from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_buttons(owner: bool, admin: bool) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    if admin or owner:
        builder.row(
            KeyboardButton(text='📧 Рассылка')
        )
        builder.row(
            KeyboardButton(text='🤖➕ Добавить бота'),
            KeyboardButton(text='🤖➖ Удалить бота'),
        )
        builder.row(
            KeyboardButton(text='🤖👥 Список ботов'),
        )

    if owner:
        builder.row(
            KeyboardButton(text='👨‍💼✅ Добавить админа'),
            KeyboardButton(text='👨‍💼❌ Удалить админа'),
        )

    return builder.as_markup(
        resize_keyboard=True,
    )
