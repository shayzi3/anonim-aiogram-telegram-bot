import asyncio
import json

from typing import Annotated, Text, Optional
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import BigInteger, insert, select, update


typeID = Annotated[int, mapped_column(BigInteger, primary_key = True)]
typeSTATUS = Annotated[int, mapped_column(BigInteger)]



class Base(AsyncAttrs, DeclarativeBase):
     pass



class ServerBot(Base):
     __tablename__ = 'server'
     
     id: Mapped[typeID | None]    # admin_id
     users: Mapped[Text | None]
     
     

class User(Base):
     __tablename__ = 'user'
     
     id: Mapped[typeID | None]
     username: Mapped[str | None]
     avatar: Mapped[str | None]
     status: Mapped[typeSTATUS | None]
     
     
     

class Main:
     '''
          Class for check data in db
          
          create_table(  ) - create table User and ServerBot
          
          data_in_server_bot( admin_id: int ) - add data in table ServerBot
          
          update_data_in_server_bot(  ) - clear data in column ServerBot users
          
          get_id(  ) - get all id from table User
          
          get_users(  ) - get id user from list users from ServerBot
          
     '''
     
     def __init__(self) -> None:
          self.__path = r'data\alchemy.db'
          self.__engine = create_async_engine(f'sqlite+aiosqlite:///{self.__path}', echo=True)
          
     
     async def create_table(self) -> None:
          async with self.__engine.begin() as begin:
               await begin.run_sync(Base.metadata.create_all)
               
          await self.__engine.dispose()
          
          
     async def data_in_server_bot(self, admin_id: int) -> None:
          async with self.__engine.begin() as begin:
               sttm = (
                    insert(ServerBot).
                    values(id = admin_id, users = json.dumps([]))
               )
               await begin.execute(sttm)
          await self.__engine.dispose()
          
     
     async def update_data_in_server_bot(self) -> None:
          async with self.__engine.begin() as begin:
               sttm = (
                    update(ServerBot).
                    values(users = json.dumps([]))
               )
               await begin.execute(sttm)
          
          
     async def get_id(self) -> None:
          async with self.__engine.connect() as connect:
               sttm = select().add_columns(User.id)
               res = await connect.execute(sttm)
               
               return res.fetchall()
          
          
     async def get_users(self) -> None:
          async with self.__engine.connect() as connect:
               sttm = select().add_columns(ServerBot.users)
               
               res = await connect.execute(sttm)
               return res.fetchall()
          

# main = Main()
# asyncio.run(main.create_table())
# asyncio.run(main.data_in_server_bot(admin_id = 2054556183))


     
     