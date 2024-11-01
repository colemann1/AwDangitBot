import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".",intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} is online!')



@bot.tree.command(name="hello",description="Says hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello!')




async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())
