from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from src.middlewares import RoleAdminMsg

router = Router(name='Self Bot Router')
router.message.filter(F.chat.type == 'private')
router.message.middleware(RoleAdminMsg())


@router.message(F.text == '🤖➕ Добавить бота')
@router.message(Command(commands=['add_self_bot']))
async def add_self_bot(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>🤖➕ Бот добавлен!</b>'
    )


@router.message(F.text == '🤖➖ Удалить бота')
@router.message(Command(commands=['del_self_bot']))
async def del_self_bot(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>‍🤖➖ Бот удален!</b>'
    )


@router.message(F.text == '🤖👥 Список ботов')
@router.message(Command(commands=['list_self_bots']))
async def list_self_bots(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>‍🤖👥 Список ботов!</b>'
    )
