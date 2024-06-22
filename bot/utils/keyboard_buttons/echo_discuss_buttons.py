

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


echo_discuss_btn = ReplyKeyboardMarkup(
     keyboard = [
          [
               KeyboardButton(text = '🔚 Завершить диалог')
          ]
     ],
     one_time_keyboard=True,
     resize_keyboard=True
)

