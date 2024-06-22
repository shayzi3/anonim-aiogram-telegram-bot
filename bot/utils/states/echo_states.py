
from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
     username = State()
     avatar = State()
     
     
class Discuss(StatesGroup):
     msg = State()