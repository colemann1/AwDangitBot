from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from data_models import Base, UserInfo, BalanceModel
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)

# This binds our ORM class models
Base.metadata.create_all(bind=engine)

# Create a session to interact with the databsae
Session = sessionmaker(bind=engine)
session = Session()

app = FastAPI()


def get_or_create_user(UserID: int):
    user = session.get(UserInfo, UserID)
    if not user:
        user = UserInfo(UserID=UserID)
        session.add(user)
        session.commit()
    return user

@app.get("/balance/{UserID}")
async def GetBalance(UserID: int):
    user = get_or_create_user(UserID)
    return user.Chips

@app.patch("/balance/{UserID}")
async def SetBalance(UserID: int, sent: BalanceModel):
    user = get_or_create_user(UserID)
    diff = sent.Chips - user.Chips
    if diff < 0: ##Chips were lost
        user.TotalChipsLost += abs(diff)
    else: ##Chips gained
        user.TotalChipsGained += diff
    user.Chips = sent.Chips
    session.commit()

@app.get("/lastlogin/{UserID}")
async def GetLastLogin(UserID: str):
        user = get_or_create_user(UserID)
        if user.LastLogin is None: ##Update last login to more than 1 day ago for registration
            user.LastLogin = "2000-01-01"
            session.commit()
        return PlainTextResponse(user.LastLogin)

@app.patch("/lastlogin/{UserID}")
async def SetLastLogin(UserID: str):
        user = get_or_create_user(UserID)
        user.LastLogin = datetime.now().isoformat()
        user.Chips += 10
        session.commit()
    
@app.patch("/gamewins/{UserID}/increment")
async def IncGameWins(UserID: str):
        user = get_or_create_user(UserID)
        user.GamesWon += 1
        await session.commit()

@app.get("/gamewins/{UserID}")
async def GetGameWins(UserID: str):
        user = get_or_create_user(UserID)
        return user.GamesWon

@app.get("/chipwlr/{UserID}")
async def GetChipWLRatio(UserID: str):
        user = get_or_create_user(UserID)
        chips_lost = user.TotalChipsLost or 1  # Avoid division by zero
        return user.TotalChipsGained / chips_lost
