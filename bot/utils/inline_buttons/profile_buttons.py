
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class ProfileCallbackData(CallbackData, prefix = 'profile'):
     action: str
     

profile_btn = InlineKeyboardMarkup(
     inline_keyboard=[
          [
               InlineKeyboardButton(text='Изменить имя', callback_data=ProfileCallbackData(action='name').pack())
          ],
          [
               InlineKeyboardButton(text='Изменить аватар', callback_data=ProfileCallbackData(action='ava').pack())
          ]
     ]
)

