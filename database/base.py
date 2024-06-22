import asyncio
import json
import random

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import (
     select, 
     insert, 
     update
)
from loguru import logger

from database.models import ServerBot, User



class AsyncDataUser:
     
     def __init__(self) -> None:
          self.__path = r'data\alchemy.db'
          self.__engine = create_async_engine(f'sqlite+aiosqlite:///{self.__path}')
                    
     
     async def check_register(self, id: int ) -> bool:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(User.username).where(User.id == id)
               
               res = await session.execute(sttm)
               
               if not res.scalar():
                    return False
               return True
                    
                    
                    
     async def insert_data(self, id: int, data: dict) -> None:
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
               
               
     async def update_status(self, id_call: int, id_wait: int) -> None:
          async with AsyncSession(self.__engine) as session:
               sttm_call = (
                    update(User).
                    where(User.id == id_call).
                    values(status = id_wait)
               )
               sttm_wait = (
                    update(User).
                    where(User.id == id_wait).
                    values(status = id_call)
               )
               await session.execute(sttm_call)
               await session.execute(sttm_wait)
               
               await session.commit()
               
               
                    
     
     async def _check_database(self) -> None:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(User)
               
               result = await session.execute(sttm)
               print(result.scalars().all())
               
               
               
               

class AsyncDataServer:
     
     def __init__(self) -> None:
          self.__path = r'data\alchemy.db'
          self.__engine = create_async_engine(f'sqlite+aiosqlite:///{self.__path}')
          
          
     async def check_len_add_users(self, id: int) -> None | bool:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(ServerBot.users)

               res = await session.execute(sttm)
               res: list[int] = json.loads(res.scalar())
               
               if len(res) < 1:
                    res.append(id)
                    
                    sttm = (
                         update(ServerBot).
                         values(users = json.dumps(res))
                    )
                    await session.execute(sttm)
                    await session.commit()
                    
                    return None
               return True
          
          
     async def out_from_users(self, id: int) -> None:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(ServerBot.users)
               
               res = await session.execute(sttm)
               res: list[int] = json.loads(res.scalar())
               
               res.remove(id)
               
               sttm = (
                    update(ServerBot).
                    values(users = json.dumps(res))
               )
               await session.execute(sttm)
               await session.commit()
               
               
     async def get_id_from_users(self) -> int:
          async with AsyncSession(self.__engine) as session:
               sttm = select().add_columns(ServerBot.users)
               
               res = await session.execute(sttm)
               res: list[int] = json.loads(res.scalar())
               
               rnd = random.choice(res)
               res.remove(rnd)
               
               sttm = (
                    update(ServerBot).
                    values(users = json.dumps(res))
               )
               
               await session.execute(sttm)
               await session.commit()
               
          return rnd
               
               
base = AsyncDataUser()
data_server = AsyncDataServer()