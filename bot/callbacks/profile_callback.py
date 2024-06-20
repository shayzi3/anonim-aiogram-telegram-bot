

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from bot.utils.inline_buttons.profile_buttons import ProfileCallbackData
from bot.utils.states.echo_states import Register
from database.base import base


router = Router()


@router.callback_query(ProfileCallbackData.filter(F.action == 'name'))
async def change_username(query: CallbackQuery, state: FSMContext) -> None:
     await state.set_state(Register.username)
     await query.message.answer('Введи новое имя')
     
     await query.answer()
     
     
@router.message(Register.username, F.text)
async def update_username(message: Message, state: FSMContext) -> None:
     await state.update_data(username = message.text)
     
     await base.update_username_or_avatar(
          id = message.from_user.id,
          name = message.text
     )
     
     await message.answer(f'Установлен новый никнейм: {message.text}')
     await state.clear()
     
     
     
     
     
@router.callback_query(ProfileCallbackData.filter(F.action == 'ava'))
async def change_avatar(query: CallbackQuery, state: FSMContext) -> None:
     await state.set_state(Register.avatar)
     await query.message.answer('Отправь мне новый аватар')
     
     await query.answer()
     

@router.message(Register.avatar, F.photo)
async def update_avatar(message: Message, state: FSMContext) -> None:
     await state.update_data(avatar = message.photo[-1].file_id)
     
     await base.update_username_or_avatar(
          id = message.from_user.id,
          avatar = message.photo[-1].file_id
     )
     
     await message.answer('Аватар успешно обновлён.')
     await state.clear()