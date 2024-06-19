

from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
     await message.answer(f'Hello, {message.from_user.id}')