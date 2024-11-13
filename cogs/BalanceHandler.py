import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database


class BalanceHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("BalanceHandler is active")

    @app_commands.command(name="balance",description="Checks your balance")
    async def balance(self, interaction: discord.Interaction):
        balance = Database.GetBalance(interaction.user.id)
        if balance == 1:
            await interaction.response.send_message(f"You have a balance of **{balance} chip**",ephemeral=True)
            return

        await interaction.response.send_message(f"You have a balance of **{balance} chips**",ephemeral=True)


    
async def setup(bot):
    await bot.add_cog(BalanceHandler(bot))