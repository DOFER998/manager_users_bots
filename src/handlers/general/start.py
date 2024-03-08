from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from src.db import users_controller
from src.db.models import RolesEnum
from src.keyboards.general import main_buttons

router = Router(name='Start Router')
router.message.filter(F.chat.type == 'private')


@router.message(Command(commands=['start']))
async def cmd_start(msg: Message):
    await users_controller.create(msg.from_user.id, msg.from_user.username)
    verification = await users_controller.get_by_id(msg.from_user.id)
    await msg.delete()
    if verification.role in [RolesEnum.admin, RolesEnum.owner]:
        await msg.answer(
            text=f'<b>Hello</b> {msg.from_user.first_name}👋',
            reply_markup=main_buttons(
                verification.role == RolesEnum.owner,
                verification.role == RolesEnum.admin
            ),
        )
    else:
        pass
