

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


echo_btn = ReplyKeyboardMarkup(
     keyboard=[
          [
               KeyboardButton(text = '⬅️ Выйти из поиска')
          ]
     ],
     one_time_keyboard=True,
     resize_keyboard=True
)