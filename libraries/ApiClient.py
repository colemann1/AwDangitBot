from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from datetime import datetime

# Define database models
Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'UserInfo'
    UserID = Column(String, primary_key=True)
    Chips = Column(Integer, default=100, nullable=False)
    TotalChipsGained = Column(Integer, default=0)
    TotalChipsLost = Column(Integer, default=0)
    LastLogin = Column(String)  
    GamesWon = Column(Integer, default=0, nullable=False)

# Database setup
DATABASE_URL = "sqlite+aiosqlite:///api/database.db"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Database:
    UserInfo = UserInfo

    @staticmethod
    async def get_session():
        async with async_session() as session:
            yield session

    @staticmethod
    async def get_or_create_user(session, user_id: str):
        user = await session.get(UserInfo, user_id)
        if not user:
            user = UserInfo(UserID=user_id)
            session.add(user)
            await session.commit()
        return user

    @staticmethod
    async def GetBalance(user_id: str):
        async for session in Database.get_session():
            user = await Database.get_or_create_user(session, user_id)
            return user.Chips

    @staticmethod
    async def SetBalance(user_id: str, balance: int):
        async for session in Database.get_session():
            user = await Database.get_or_create_user(session, user_id)
            user.Chips = balance
            await session.commit()

    @staticmethod
    async def GetLastLogin(user_id: str):
        async for session in Database.get_session():
            user = await Database.get_or_create_user(session, user_id)
            if user.LastLogin:
                return datetime.fromisoformat(user.LastLogin)
            return None

    @staticmethod
    async def SetLastLogin(user_id: str):
        async with async_session() as session:
            user = await session.get(UserInfo, user_id)
            if user:
                user.LastLogin = datetime.utcnow()
                await session.commit()
                
    @staticmethod
    async def IncGameWins(user_id: str):
        async for session in Database.get_session():
            user = await Database.get_or_create_user(session, user_id)
            user.GamesWon += 1
            await session.commit()

    @staticmethod
    async def GetGameWins(user_id: str):
        async for session in Database.get_session():
            user = await Database.get_or_create_user(session, user_id)
            return user.GamesWon

    @staticmethod
    async def GetChipWLRatio(user_id: str):
        async for session in Database.get_session():
            user = await Database.get_or_create_user(session, user_id)
            chips_lost = user.TotalChipsLost or 1  # Avoid division by zero
            return user.TotalChipsGained / chips_lost
