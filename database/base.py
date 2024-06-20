import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import (
     select, 
     insert, 
     update
)
from loguru import logger

from database.models import ServerBot, User



class AsyncDataBase:
     
     def __init__(self) -> None:
          self.__path = r'C:\Users\dyadh\OneDrive\Рабочий стол\Telegram Shop\data\alchemy.db'
          self.__engine = create_async_engine(f'sqlite+aiosqlite:///{self.__path}')
                    
     
     async def check_register(self, id: int ) -> bool:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(User.username).where(User.id == id)
               
               res = await session.execute(sttm)
               
               if not res.scalar():
                    return False
               return True
                    
                    
                    
     async def update_name_avatar(self, id: int, data: dict) -> None:
          async with AsyncSession(self.__engine) as session:  
               sttm = (
                    insert(User).
                    values(
                         username = data['username'], 
                         avatar = data['avatar'], 
                         id = id, 
                         status = False
                    )
               )  
               await session.execute(sttm)
               await session.commit()   
                              
               logger.info(f'New (username, avatar) for {id}. Name in bot: {data["username"]}')
               
               
     async def take_username_avatar(self, id: int) -> tuple[str]:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(User.username, User.avatar).where(User.id == id)
               
               res = await session.execute(sttm)
               return res.fetchone()
          
          
     async def update_username_or_avatar(self, id: int, name: str = None, avatar: str = None) -> None:
          async with AsyncSession(self.__engine) as session:
               if name:
                    sttm = (
                         update(User).
                         where(User.id == id).
                         values(username = name)
                    )
               elif avatar:
                    sttm = (
                         update(User).
                         where(User.id == id).
                         values(avatar = avatar)
                    )
                    
               await session.execute(sttm)
               await session.commit()     
                    
     
     async def _check_database(self) -> None:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(User)
               
               result = await session.execute(sttm)
               print(result.scalars().all())
               
               
base = AsyncDataBase()
# asyncio.run(base._check_database())