import os

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv

from database.base import base
from bot.utils.inline_buttons import send_message_buttons as send_bt



class SenderMessages(Bot):

     def __init__(self) -> None:
          load_dotenv()
          super().__init__(token = os.getenv('TOKEN'))
          
          
          
     async def send_start_message(self, id_call: int, id_wait: int) -> None:
          data_call = await base.take_username_avatar(id = id_call)
          data_wait = await base.take_username_avatar(id = id_wait)
          
          text_call = f'Собеседник найден! \n<b>Name: {data_wait[0]}</b>'
          text_wait = f'Собеседник найден! \n<b>Name: {data_call[0]}</b>'
          
          
          # Send to data_call
          await self.send_message(
               chat_id = id_call,
               text = text_call,
               reply_markup = send_bt.send_button(id_user = id_wait),
               parse_mode = ParseMode.HTML
          )
          # Send to data_wait
          await self.send_message(
               chat_id = id_wait,
               text = text_wait,
               reply_markup = send_bt.send_button(id_user = id_call),
               parse_mode = ParseMode.HTML
          )
          
          await self.session.close()
          
sender = SenderMessages()