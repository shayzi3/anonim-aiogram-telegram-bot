

from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.enums.parse_mode import ParseMode

from database.base import base
from bot.utils.keyboard_buttons import start_buttons


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
     reply = start_buttons.start_btn_register
     register = await base.check_register(id = message.from_user.id)
     
     if register:
          reply = start_buttons.start_btn_profile
     
     
     await message.answer(
          f'Привет, <b>{message.from_user.full_name}</b>. Рад тебя видеть в анонимном боте, чтобы продолжить работу нужно пройти регистрацию.',
          reply_markup=reply,
          parse_mode=ParseMode.HTML
     )