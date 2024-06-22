

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.states.echo_states import Discuss


router = Router()


@router.message(Discuss.msg, F.text)
async def discuss_text(message: Message, state: FSMContext) -> None:
     await state.update_data(msg = message.text)
     
     
     ...