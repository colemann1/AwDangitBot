import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database
from libraries.GameViews import Roulette
from time import sleep

class RouletteHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("RouletteHandler is active")

    @app_commands.command(name="roulette",description="play a game of roulette!")
    @app_commands.describe(wager="How many chips you are betting")
    async def roulette(self, interaction: discord.Interaction, wager:app_commands.Range[int, 1, 1000000]):
        await interaction.response.send_message("Thinking...")
        balance = await Database.GetBalance(interaction.user.id)
        async def GameEnd(mult,balance,wager):
            if mult > 1:
                await Database.IncGameWins(interaction.user.id,"ROU")
            wager *= mult
            print(wager)
            balance += wager
            print(balance)
            await Database.SetBalance(interaction.user.id,balance)

        ##Error checks
        if balance < wager:
            await interaction.delete_original_response()
            await interaction.followup.send(content=f"You do not have enough chips for that!\nBalance: {balance}",ephemeral=True)
            return
        balance -= wager

        roulette = Roulette(interaction.user)
        await interaction.delete_original_response()
        await interaction.followup.send("This is a test",view=roulette)
        if await roulette.wait() == False:
            await interaction.channel.send(f"GAME COMPLETE, WAGER: {wager}, GAME VALUE: {roulette.game.result}, BET: {roulette.bet}, WIN? {roulette.mult}")
        else: ##TIMEOUT!!
            await interaction.channel.send("TIMEOUT!!")
        await GameEnd(roulette.mult,balance,wager)

    
async def setup(bot):
    await bot.add_cog(RouletteHandler(bot))