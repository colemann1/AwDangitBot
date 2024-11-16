import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database
from datetime import datetime, timedelta


class AccountHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("AccountHandler is active")

    @app_commands.command(name="balance",description="Checks your balance")
    async def balance(self, interaction: discord.Interaction):
        balance = await Database.GetBalance(interaction.user.id)
        if balance == 1:
            await interaction.response.send_message(f"You have a balance of **{balance} chip**",ephemeral=True)
            return

        await interaction.response.send_message(f"You have a balance of **{balance} chips**",ephemeral=True)

    @app_commands.command(name="daily",description="Get your daily bonus of chips")
    async def daily(self, interaction: discord.Interaction):
        lastlogin: datetime = await Database.GetLastLogin(interaction.user.id)
        today = datetime.now()

        diff = today - lastlogin
        if diff >= timedelta(days=1):
            balance = await Database.GetBalance(interaction.user.id)
            newbal = balance + 10
            await Database.SetBalance(interaction.user.id, newbal)
            await Database.SetLastLogin(interaction.user.id)
            await interaction.response.send_message(f"You have gained 10 chips! Please wait 1 day for another daily bonus.",ephemeral=True)
        else:
            timeleft = (timedelta(days=1) - diff).total_seconds()

            if timeleft > 3600:
                hours_left = timeleft // 3600
                unit = "hour" if hours_left == 1 else "hours"
                await interaction.response.send_message(f"You have **{int(hours_left)} {unit}** remaining...",ephemeral=True)
            else:
                minutes_left = timeleft // 60
                unit = "minute" if minutes_left == 1 else "minutes"
                await interaction.response.send_message(f"You have **{int(minutes_left)} {unit}** remaining...",ephemeral=True)

            

async def setup(bot):
    await bot.add_cog(AccountHandler(bot))