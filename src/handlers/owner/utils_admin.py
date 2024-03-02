from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='Utils Admin Router')
router.message.filter(F.chat.type == 'private')


@router.message(F.text == '👨‍💼✅ Добавить админа')
@router.message(Command(commands=['add_admin']))
async def add_admin(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>👨‍💼✅  Админ добавлен!</b>'
    )


@router.message(F.text == '👨‍💼❌ Удалить админа')
@router.message(Command(commands=['del_admin']))
async def del_admin(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>‍👨‍💼❌ Админ удален!</b>'
    )
