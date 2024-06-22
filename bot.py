import os
import asyncio

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from loguru import logger

from bot.handlers.user_commands import start, profile
from bot.handlers.bot_commands import echo, echo_discuss, echo_register
from bot.callbacks import profile_callback, send_message_callback


load_dotenv()
tk = os.getenv('TOKEN')


async def main() -> None:
     bot = Bot(tk)
     dp = Dispatcher()
     
     logger.info('[+] Bot was started...')
     
     dp.include_routers(
          start.router,
          profile.router,
          profile_callback.router,
          send_message_callback.router,
          echo_register.router,
          echo_discuss.router,
          echo.router
     )
     
     await bot.delete_webhook(drop_pending_updates=True)
     await dp.start_polling(bot)
     
     
if __name__ == '__main__':
     asyncio.run(main())