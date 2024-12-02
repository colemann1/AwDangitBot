from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


# Define database models
class Base(DeclarativeBase):
    pass

class UserInfo(Base):
    __tablename__ = 'UserInfo'
    UserID = Column(Integer, primary_key=True)
    Chips = Column(Integer, default=100, nullable=False)
    TotalChipsGained = Column(Integer, default=0)
    TotalChipsLost = Column(Integer, default=0)
    LastLogin = Column(String)  
    GamesWon = Column(Integer, default=0, nullable=False)

# Pydantic models

class BalanceModel(BaseModel):
    Chips: int

    class Config:
        from_attributes = True
