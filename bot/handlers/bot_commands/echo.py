
from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from database.base import base, data_server
from bot.utils.states.echo_states import Register, Discuss
from bot.utils.inline_buttons import profile_buttons

from bot.utils.keyboard_buttons import start_buttons, echo_buttons
from bot.handlers.bot_commands.send_messages import sender


router = Router()


@router.message()
async def echo(message: Message, state: FSMContext) -> None:
     if message.text == '🚀 Пройти регистрацию':
          await state.set_state(Register.username)
          await message.answer('Введи свой nickname')
          
          
          
     elif message.text == '👤 Профиль':
          data = await base.take_username_avatar(id = message.from_user.id)
          
          await message.answer_photo(
               photo = data[1],
               caption = f'Nickname: {data[0]}',
               reply_markup = profile_buttons.profile_btn
          )
          
          
     
     elif message.text == '🌐 Найти собеседника':
          res = await data_server.check_len_add_users(
               id = message.from_user.id
          )
          
          if not res:
               await message.answer(
                    text = 'Вы добавлены в поиск 📝',
                    reply_markup=echo_buttons.echo_btn
               )
               return
          
          id_ = await data_server.get_id_from_users()
          await base.update_status(
               id_call = message.from_user.id,
               id_wait = id_
          )
          await sender.send_start_message(
               id_call = message.from_user.id,
               id_wait = id_
          )
          
          await state.set_state(Discuss.msg)
          
          
          
     elif message.text == '⬅️ Выйти из поиска':
          await data_server.out_from_users(
               id = message.from_user.id
          )
          
          await message.answer(
               text = 'Вы вышли из поиска ╰┈➤🚪',
               reply_markup=start_buttons.start_btn_profile
          )
          
          
          
          







