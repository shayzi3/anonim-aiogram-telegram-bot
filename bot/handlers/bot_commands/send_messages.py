import os

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv

from database.base import base
from bot.utils.inline_buttons import send_message_buttons as send_bt
from bot.utils.keyboard_buttons import start_buttons, echo_discuss_buttons



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
          await self.send_message(
               chat_id = id_call,
               text = 'Диалог начался.',
               reply_markup = echo_discuss_buttons.echo_discuss_btn
          )
          # Send to data_wait
          await self.send_message(
               chat_id = id_wait,
               text = 'Диалог начался.',
               reply_markup = echo_discuss_buttons.echo_discuss_btn
          )
          await self.session.close()
          
          
     async def sender_message(self, id: int, message_: str) -> None:
          await self.send_message(chat_id = id, text = message_)
          
          
     async def sender_photo(self, id: int, id_to_file: str) -> None:
          await self.send_photo(chat_id = id, photo = id_to_file)
          
          
     async def sender_audio(self, id: int, id_to_file: str) -> None:
          await self.send_audio(chat_id = id, audio = id_to_file)
          
          
     async def sender_voice(self, id: int, id_to_file: str) -> None:
          await self.send_voice(chat_id = id, voice = id_to_file)
          
          
     async def sender_video(self, id: int, id_to_file: str) -> None:
          await self.send_video(chat_id = id, video = id_to_file)
          
     
     async def sender_sticker(self, id: int, id_to_file: str) -> None:
          await self.send_sticker(chat_id = id, sticker = id_to_file)
          
          
     async def sender_document(self, id: int, id_to_file: str) -> None:
          await self.send_document(chat_id = id, document = id_to_file)
          
          
     async def stop_dioalog(self, id: int) -> None:
          await self.send_message(chat_id = id, text = 'Диалог завершён.', reply_markup = start_buttons.start_btn_profile)
          
sender = SenderMessages()