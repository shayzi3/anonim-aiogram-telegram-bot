
from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.utils.inline_buttons import send_message_buttons as send_
from database.base import base


router = Router()


@router.callback_query(send_.IDToPhotoButton.filter(F.id))
async def photo_callback(query: CallbackQuery, callback_data: send_.IDToPhotoButton) -> None:
     photo = await base.take_username_avatar(id = callback_data.id)
     
     await query.message.answer_photo(photo = photo[1], reply_markup = send_.send_button(action = True))
     await query.answer()
     
     
@router.callback_query(send_.IDToPhotoButton.filter(F.action))
async def photo_del(query: CallbackQuery) -> None:
     await query.message.delete()
     
     
