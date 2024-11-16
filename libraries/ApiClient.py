from datetime import datetime


class Database:

    async def GetBalance(id):
        if id == 560123152349528066:
            #main acc
            return 1000
        elif id == 1099399216054423793:
            #alt acc
            return 20
        elif id == 178655110891569153:
            #nolan
            return 1000
        elif id == 527500730698039296:
            #jo
            return 269
        else:
            return 100
        
    async def SetBalance(id,balance):
        pass

    async def GetLastLogin(id):
        date = datetime(2024,11,15,20,0)
        return date

    async def SetLastLogin(id):
        pass

    async def IncGameWins(id,gameid):
        pass

    async def GetGameWins(id):
        pass

    async def GetChipWLRatio(id):
        pass


