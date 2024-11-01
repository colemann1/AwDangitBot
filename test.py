import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".",intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

@bot.command()
async def hello(ctx):
    await ctx.reply(f'Hello!')

@bot.command()
async def ping(ctx):
    ping_embed = discord.Embed(title="Pong!", color=discord.Color.random())
    ping_embed.set_footer(text=f"Requested by {ctx.author.name}",icon_url=ctx.author.avatar)
    ping_embed.add_field(name=f"Bot's Latency: {round(bot.latency * 1000)}ms",value="")
    await ctx.send(embed=ping_embed)


bot.run(DISCORD_BOT_TOKEN)