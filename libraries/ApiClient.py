import requests
from datetime import datetime

address = f"http://localhost:8000"

class Database:

    async def GetBalance(id):
        return int(requests.get(address + f"/balance/{id}").text)
        
    async def SetBalance(id,balance):
        requests.patch(address + f"/balance/{id}",json={"Chips":balance})

    async def GetLastLogin(id):
        return datetime.fromisoformat(requests.get(address + f"/lastlogin/{id}").text)

    async def SetLastLogin(id):
        requests.patch(address + f"/lastlogin/{id}")

    async def IncGameWins(id,gameid):
        requests.patch(address + f"/gamewins/{id}/{gameid}/increment")

    async def GetGameWins(id,gameid):
        return int(requests.get(address + f"/gamewins/{id}/{gameid}").text)

    async def GetChipWLRatio(id):
        return int(requests.get(address + f"/chipwlr/{id}").text)