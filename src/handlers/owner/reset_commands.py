from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from src import bot
from src.misc.commands import reset_commands

router = Router(name='Reset Commands Router')
router.message.filter(F.chat.type == 'private')


@router.message(Command(commands=['reset_commands']))
async def reset_cmd(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>🔁 Команды были успешно перезагружены!</b>'
    )
    await reset_commands(bot)
