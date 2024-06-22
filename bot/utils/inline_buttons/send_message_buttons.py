

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class IDToPhotoButton(CallbackData, prefix = 'photo'):
     id: int | None
     action: bool | None
               
     
def send_button(id_user: int | None = None, action: bool | None = None) -> InlineKeyboardBuilder:
     build = InlineKeyboardBuilder()
     
     if not action:
          build.button(text = 'Показать аватар', callback_data = IDToPhotoButton(id = id_user, action = None).pack())
          
     else:
          build.button(text = 'Убрать картинку', callback_data = IDToPhotoButton(action = True, id = None).pack())

     return build.as_markup()




