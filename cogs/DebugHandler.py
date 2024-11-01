import discord
from discord import app_commands
from discord.ext import commands

class DebugHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("DebugHandler is active")

    ## Sync command for only owner
    async def is_owner(ctx: commands.Context):
        return ctx.author.id == 560123152349528066
    @commands.command()
    @commands.check(is_owner)
    async def sync(self, ctx: commands.Context):
        message = await ctx.reply("Syncing commands...")
        try:
            synced_commands = await self.bot.tree.sync()
            await message.edit(content=f"Synced {len(synced_commands)} commands.")
        except Exception as e:
            await message.edit(content=("An error has occurred with syncing: ", e))

    @app_commands.command(name="ping",description="Gets the bot's latency")
    async def ping(self, interaction: discord.Interaction):
        ping_embed = discord.Embed(title="Pong!", color=discord.Color.random())
        ping_embed.set_footer(text=f"Requested by {interaction.user.name}",icon_url=interaction.user.avatar)
        ping_embed.add_field(name=f"Bot's Latency: {round(self.bot.latency * 1000)}ms",value="")
        await interaction.response.send_message(embed=ping_embed)

    


async def setup(bot):
    await bot.add_cog(DebugHandler(bot))