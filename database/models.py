import asyncio

from typing import Annotated, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import BigInteger


typeID = Annotated[int, mapped_column(BigInteger, primary_key = True, nullable = True)]
typeSTR = Annotated[str, mapped_column(nullable = True)]
typeUSERS = Annotated[Text, mapped_column(nullable = True)]
typeSTATUS = Annotated[bool, mapped_column(nullable=True)]



class Base(AsyncAttrs, DeclarativeBase):
     pass



class ServerBot(Base):
     __tablename__ = 'server'
     
     id: Mapped[typeID]    # admin_id
     users: Mapped[typeUSERS]
     
     

class User(Base):
     __tablename__ = 'user'
     
     id: Mapped[typeID]
     username: Mapped[typeSTR]
     avatar: Mapped[typeSTR]
     status: Mapped[typeSTATUS]
     
     
     

class Main:
     def __init__(self) -> None:
          self.__path = r'C:\Users\dyadh\OneDrive\Рабочий стол\Telegram Shop\data\alchemy.db'
          
     
     async def create_table(self) -> None:
          async_engine = create_async_engine(f'sqlite+aiosqlite:///{self.__path}', echo=True)
          
          async with async_engine.begin() as begin:
               await begin.run_sync(Base.metadata.create_all)
               
          await async_engine.dispose()
          

# main = Main()
# asyncio.run(main.create_table())


     
     