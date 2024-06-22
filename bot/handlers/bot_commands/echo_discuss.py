
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.states.echo_states import Discuss
from bot.handlers.bot_commands.send_messages import sender
from bot.utils.keyboard_buttons import start_buttons
from database.base import base


router = Router()


@router.message(Discuss.msg, F.text)
async def discuss_text(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.text)

     id_ = await base.get_status(id = message.from_user.id)
     
     if message.text == '🔚 Завершить диалог':
          await sender.stop_dioalog(id = id_)
          await message.answer('Диалог завершён.', reply_markup = start_buttons.start_btn_profile)
          
          await base.clear_status(
               id_call = message.from_user.id,
               id_wait = id_
          )
         
          await state.clear()
          return 
          
     await sender.sender_message(id = id_, message_ = message.text)
     
     
     
@router.message(Discuss.msg, F.photo)
async def discuss_photo(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.photo[-1].file_id)
     
     id_ = await base.get_status(id = message.from_user.id)
     await sender.sender_photo(id = id_, id_to_file = message.photo[-1].file_id)
     



@router.message(Discuss.msg, F.audio)
async def discuss_audio(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.audio.file_id)
     
     id_ = await base.get_status(id = message.from_user.id)
     await sender.sender_audio(id = id_, id_to_file = message.audio.file_id)
     
     

     
@router.message(Discuss.msg, F.voice)
async def discuss_voice(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.voice.file_id)
     
     id_ = await base.get_status(id = message.from_user.id)
     await sender.sender_voice(id = id_, id_to_file = message.voice.file_id)
     
     

     
     
@router.message(Discuss.msg, F.video)
async def discuss_video(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.video.file_id)
     
     id_ = await base.get_status(id = message.from_user.id)
     await sender.sender_video(id = id_, id_to_file = message.video.file_id)
     
     

     
@router.message(Discuss.msg, F.sticker)
async def discuss_sticker(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.sticker.file_id)
     
     id_ = await base.get_status(id = message.from_user.id)
     await sender.sender_sticker(id = id_, id_to_file = message.sticker.file_id)
     

     

@router.message(Discuss.msg, F.document)
async def discuss_document(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.document.file_id)
     
     id_ = await base.get_status(id = message.from_user.id)
     await sender.sender_document(id = id_, id_to_file = message.document.file_id)