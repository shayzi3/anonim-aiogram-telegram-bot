
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_btn_register = ReplyKeyboardMarkup(
     keyboard=[
          [
               KeyboardButton(text='🚀 Пройти регистрацию')
          ]
     ],
     one_time_keyboard=True,
     resize_keyboard=True
)



start_btn_profile = ReplyKeyboardMarkup(
     keyboard=[
          [
               KeyboardButton(text=f'👤 Profile')
          ]
     ],
     one_time_keyboard=True,
     resize_keyboard=True
)