import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database
from libraries.GameViews import Roulette

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
        firstwager = wager
        async def GameEnd(mult,balance,wager):
            if mult > 1:
                await Database.IncGameWins(interaction.user.id,"ROU")
            wager *= mult
            balance += wager
            await Database.SetBalance(interaction.user.id,balance)

        ##Error checks
        if balance < wager:
            await interaction.delete_original_response()
            await interaction.followup.send(content=f"You do not have enough chips for that!\nBalance: {balance}",ephemeral=True)
            return
        balance -= wager

        firstembed = discord.Embed(title="Place your bet",color=0x2a4d3e,description="choose wisely...")
        roulette = Roulette(interaction.user)
        await interaction.delete_original_response()
        await interaction.channel.send(f"## Roulette!\n{interaction.user.mention} bet {wager} chips!",view=roulette,embed=firstembed)
        if await roulette.wait() == False:
            ##Ending message
            if roulette.mult > 1: #win
                lastembed = discord.Embed(title="The Wheel has been spun...",color=0x2a4d3e,description=f"## {roulette.game.result[2]} {roulette.game.result[0]}\n### You bet on {roulette.bet}\n**You Win!**")
                lastembed.add_field(name="",value=f"x{roulette.mult} Win Multiplier\n+{wager} chips")
            else: #lose
                lastembed = discord.Embed(title="The Wheel has been spun...",color=0x2a4d3e,description=f"## {roulette.game.result[2]} {roulette.game.result[0]}\n### You bet on {roulette.bet}\n**You Lose...**")
                lastembed.add_field(name="",value=f"-{firstwager} chips")
            await interaction.channel.send(content=f"## Roulette!\n{interaction.user.mention} bet {wager} chips!",embed=lastembed)
        else: ##TIMEOUT!!
            await interaction.channel.send(content=f"{interaction.user.mention}, you took too long to respond!\n-{firstwager} chips")
        await GameEnd(roulette.mult,balance,wager)

    
async def setup(bot):
    await bot.add_cog(RouletteHandler(bot))