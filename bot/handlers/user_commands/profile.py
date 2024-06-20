

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from database.base import base
from bot.utils.inline_buttons import profile_buttons


router = Router()


@router.message(Command('profile'))
async def profile(message: Message) -> None:
     data = await base.take_username_avatar(id = message.from_user.id)
     
     await message.answer_photo(
          photo = data[1],
          caption = f'Nickname: {data[0]}',
          reply_markup=profile_buttons.profile_btn
     )