import os
import asyncio

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv
from loguru import logger

from bot.handlers.user_commands import start


load_dotenv()
tk = os.getenv('TOKEN')


async def main() -> None:
     bot = Bot(tk)
     dp = Dispatcher()
     
     logger.info('[+] Bot was started...')
     
     dp.include_routers(
          start.router
     )
     
     await bot.delete_webhook(drop_pending_updates=True)
     await dp.start_polling(bot)
     
     
     
     
if __name__ == '__main__':
     asyncio.run(main())