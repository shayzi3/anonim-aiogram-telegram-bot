
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.utils.states.echo_states import Register
from database.base import base


router = Router()


@router.message(Register.username, F.text)
async def save_usernaame(message: Message, state: FSMContext) -> None:
     await state.update_data(username = message.text)
     
     await state.set_state(Register.avatar)
     await message.answer('Теперь отправь свой аватар')
     
     
     
@router.message(Register.avatar, F.photo)
async def save_avatar(message: Message, state: FSMContext) -> None:
     await state.update_data(avatar = message.photo[-1].file_id)
     
     data = await state.get_data()
     
     # ? Save data in database
     await base.update_name_avatar(
          id = message.from_user.id,
          data = data
     )   
     
     await message.answer('Регистрация завершена успешно ✨. Чтобы увидеть профиль /profile')
     await state.clear()



@router.message()
async def echo(message: Message, state: FSMContext) -> None:
     if message.text == '🚀 Пройти регистрацию':
          await state.set_state(Register.username)
          await message.answer('Введи свой nickname')
          
          
          







