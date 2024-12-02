import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database
from libraries.GameViews import RockPaperScissors

##Views
class ChallengeGamesList(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.gameChoice = None

    @discord.ui.select(
        placeholder="Options...",
        options=[
            discord.SelectOption(label="Rock Paper Scissors")
        ]
    )
    async def game_chosen(self, interaction:discord.Interaction, select_option:discord.ui.Select):
        self.gameChoice = select_option.values[0]
        await interaction.response.defer()
        await interaction.delete_original_response()
        self.stop()

class ChallengeAccept(discord.ui.View):
    def __init__(self, target:discord.User):
        super().__init__()
        self.target = target
    
    @discord.ui.button(label="Accept!", style=discord.ButtonStyle.primary)
    async def accept_challenge(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id == self.target.id:
            await interaction.response.defer()
            await interaction.delete_original_response()
            self.stop()
        else:
            await interaction.response.send_message(content=f"You are not {self.target.display_name}!",ephemeral=True)



##Main class
class ChallengeHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("ChallengeHandler is active")

    @app_commands.command(name="challenge",description="Challenge a user to a game!")
    @app_commands.describe(user="The user being challenged",wager="How many chips you are betting")
    async def challenge(self, interaction: discord.Interaction, user: discord.User, wager:app_commands.Range[int, 0, 1000000]=0):
        await interaction.response.send_message("Checking balances...",ephemeral=True)
        player1 = interaction.user
        player2 = user
        winner:discord.User = None
        wagermsg = ""
        wagervalue = ""
        gameChoice = None
        gameid = None
        player1_bal = 0
        player2_bal = 0
        if wager == 1:
            player1_bal = await Database.GetBalance(player1.id)
            player2_bal = await Database.GetBalance(player2.id)
            wagermsg = " for **1 chip**"
            wagervalue = "1 chip"
        elif wager >= 2:
            player1_bal = await Database.GetBalance(player1.id)
            player2_bal = await Database.GetBalance(player2.id)
            wagermsg = f" for **{wager} chips**"
            wagervalue = f"{wager} chips"

        ##Error checks
        if interaction.user.id == user.id:
            await interaction.edit_original_response(content="You cannot challenge yourself!")
            return
        elif user.bot:
            await interaction.edit_original_response(content="You cannot challenge a bot!")
            return
        elif player1_bal < wager:
            await interaction.edit_original_response(content=f"You do not have enough chips for that!\nBalance: {player1_bal}")
            return
        elif player2_bal < wager:
            await interaction.edit_original_response(content=f"{player2.display_name} does not have enough chips for that!")
            return

        ##First menu
        gameChoiceView = ChallengeGamesList()
        await interaction.edit_original_response(content=f"Challenging {player2.display_name}{wagermsg}, what game will you play?", view=gameChoiceView)
        ##First menu success
        if await gameChoiceView.wait() == False:
            gameChoice = gameChoiceView.gameChoice
            ##Second menu
            challengeAcceptView = ChallengeAccept(player2)
            await interaction.channel.send(content=f"{player2.mention}, {player1.display_name} is challenging you to a game of {gameChoice}{wagermsg}, do you accept?", view=challengeAcceptView)
        ##Second menu success
        if await challengeAcceptView.wait() == False:
            ##GAME SELECTION LOGIC
            if gameChoice == "Rock Paper Scissors":
                gameid = "RPS"
                rpsEmbed = discord.Embed(title="Rock Paper Scissors!",color=0xaf7ffb,description=wagermsg)
                rpsEmbed.add_field(name=f"{player1.display_name}: thinking...",value="",inline=False)
                rpsEmbed.add_field(name=f"{player2.display_name}: thinking...",value="",inline=False)
                rpsView = RockPaperScissors(player1,player2,rpsEmbed)
                await interaction.channel.send(embed=rpsEmbed,view=rpsView)
                await rpsView.wait()
                winner = rpsView.winner
                #construct winning message
                if rpsView.winner is not None:
                    gameResults = discord.Embed(title="Game Results:",color=0x334bde,description=f"{player1.display_name}: {rpsView.user1_choice}\n{player2.display_name}: {rpsView.user2_choice}\n**{winner.display_name} Wins!**")
                    gameResults.set_thumbnail(url=winner.avatar.url)
                else:
                    gameResults = discord.Embed(title="Game Results:",color=0x334bde,description=f"{player1.display_name}: {rpsView.user1_choice}\n{player2.display_name}: {rpsView.user2_choice}\n**It's a Tie!**")
            
            ##Display balance changes
            if wager != 0 and winner is not None:
                if winner.id == player1.id:
                    player1_bal += wager
                    player2_bal -= wager
                    gameResults.add_field(name="",value=f"{winner.display_name}: +{wagervalue}\n{player2.display_name}: -{wagervalue}")
                    await interaction.channel.send(content=f"## {gameChoice}!\n**{player1.mention}** vs **{player2.mention}**",embed=gameResults)
                    await Database.SetBalance(player1.id, player1_bal)
                    await Database.SetBalance(player2.id, player2_bal)
                    await Database.IncGameWins(player1.id,gameid)
                else:
                    player1_bal -= wager
                    player2_bal += wager
                    gameResults.add_field(name="",value=f"{winner.display_name}: +{wagervalue}\n{player1.display_name}: -{wagervalue}")
                    await interaction.channel.send(content=f"## {gameChoice}!\n**{player1.mention}** vs **{player2.mention}**",embed=gameResults)
                    await Database.SetBalance(player1.id, player1_bal)
                    await Database.SetBalance(player2.id, player2_bal)
                    await Database.IncGameWins(player2.id,gameid)
            else:
            ##Send final game announcement msg    
                await interaction.channel.send(content=f"## {gameChoice}!\n**{player1.mention}** vs **{player2.mention}**",embed=gameResults)




async def setup(bot):
    await bot.add_cog(ChallengeHandler(bot))