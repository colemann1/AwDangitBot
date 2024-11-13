import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio

#Imports bot token from .env
load_dotenv(".env")
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

#Creates bot with set intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".",intents=intents)

#Notify for bot status
@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

#Load cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

#Start cogs and bot
async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)
asyncio.run(main())
