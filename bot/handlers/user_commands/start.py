

from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from aiogram.enums.parse_mode import ParseMode

from database.base import base, data_server
from bot.utils.keyboard_buttons import start_buttons


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
     reply = start_buttons.start_btn_register
     text = f'Привет, <b>{message.from_user.full_name}</b>. Рад тебя видеть в анонимном боте, чтобы продолжить работу нужно пройти регистрацию.'
     
     register = await base.check_register(id = message.from_user.id)
     if register:
          reply = start_buttons.start_btn_profile
          text = f'Привет, <b>{message.from_user.full_name}</b>.'
          
          
     status = await base.get_status(id = message.from_user.id)
     if status:
          await message.answer(text, parse_mode=ParseMode.HTML)
          return
     
     users = await data_server.get_users()
     if message.from_user.id in users:
          await message.answer(text, parse_mode=ParseMode.HTML)
          return
     
     
     await message.answer(
          text,
          reply_markup=reply,
          parse_mode=ParseMode.HTML
     )