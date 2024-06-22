

from aiogram.fsm.state import StatesGroup, State


class UpUsername(StatesGroup):
     name = State()
     
     
class UpAvatar(StatesGroup):
     ava = State()