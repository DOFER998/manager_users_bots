from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='Mailing Router')
router.message.filter(F.chat.type == 'private')


@router.message(F.text == '📧 Рассылка')
@router.message(Command(commands=['mailing']))
async def start_mailing(msg: Message):
    await msg.delete()
    await msg.answer(
        text='<b>📧 Рассылка!</b>'
    )
