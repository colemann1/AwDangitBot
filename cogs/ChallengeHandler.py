import discord
from discord import app_commands
from discord.ext import commands
from api_client import Database

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

class ChallengeHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("ChallengeHandler is active")

    @app_commands.command(name="challenge",description="Challenge a user to a game!")
    @app_commands.describe(user="The user being challenged",wager="How many chips you are betting")
    async def challenge(self, interaction: discord.Interaction, user: discord.User, wager:app_commands.Range[int, -1, 1000000]=-1):
        player1 = interaction.user
        player2 = user
        wagermsg = ""
        gameChoice = None
        player1_bal = Database.GetBalance(player1.id)
        player2_bal = Database.GetBalance(player2.id)
        if wager == 1:
            wagermsg = " for **1 chip**"
        elif wager >= 2:
            wagermsg = f" for **{wager} chips**"
        elif wager < 0:
            wagermsg = " no, you are dumb, bad, badababdsabdsbabdbdsabdbsbsabasbsa chips"

        ##Error checks
        if interaction.user.id == user.id:
            await interaction.response.send_message(content="You cannot challenge yourself!",ephemeral=True)
            return
        elif player1_bal < wager:
            await interaction.response.send_message(content=f"You do not have enough chips for that!\nBalance: {player1_bal}",ephemeral=True)
            return
        elif player2_bal < wager:
            await interaction.response.send_message(content=f"{player2.display_name} does not have enough chips for that!",ephemeral=True)
            return

        ##First menu
        gameChoiceView = ChallengeGamesList()
        await interaction.response.send_message(content=f"Challenging {player2.display_name}{wagermsg}, what game will you play?", view=gameChoiceView, ephemeral=True)
        ##First menu success
        if await gameChoiceView.wait() == False:
            gameChoice = gameChoiceView.gameChoice
            ##Second menu
            challengeAcceptView = ChallengeAccept(player2)
            await interaction.channel.send(content=f"{player2.mention}, {player1.display_name} is challenging you to a game of {gameChoice}{wagermsg}, do you accept?", view=challengeAcceptView)
        ##Second menu success
        if await challengeAcceptView.wait() == False:
            ##GAME SELECTION LOGIC
            await interaction.channel.send(f"game start, test complete.\nChallenger: {player1.name}\nTarget: {player2.name}\nGame type: {gameChoice}\nWager: {wager}")


        # match game.value:
        #     case 1: #Rock Paper Scissors
        #         mainmsg:discord.Message
        #         player_choices = {}
        #         rpsselect = Select(options=[
        #             discord.SelectOption(label="Rock",value=1),
        #             discord.SelectOption(label="Paper",value=2),
        #             discord.SelectOption(label="Scissors",value=3)
        #         ],placeholder="What is your choice?")

        #         async def player2_choice(interaction: discord.Interaction):
        #             if (interaction.user.id != player2.id):
        #                 await interaction.response.send_message(f"You are not {player2.display_name}!",ephemeral=True)
        #                 return
        #             await interaction.response.send_message(f"Pick your move:", view=rpsview, ephemeral=True)
        #             await mainmsg.edit(content=f"{player2.display_name} is picking their option...")
        #         async def choice_selected(interaction: discord.Interaction):
        #             player_choices[interaction.user] = rpsselect.values[0]
        #             print(player_choices)
        #             if len(player_choices) == 1:
        #                 rpsbutton = Button(label="Challenge Accepted!", style=discord.ButtonStyle.primary)
        #                 rpsbutton.callback = player2_choice
        #                 rpschallenge = View()
        #                 rpschallenge.add_item(rpsbutton)
        #                 await interaction.response.defer()
        #                 mainmsg = await interaction.followup.send(content=f"{player2.mention}, {interaction.user.display_name} is challenging you to a game of Rock Paper Scissors! do you accept?", view=rpschallenge,wait=True)
        #             elif len(player_choices) >= 2:
        #                 await interaction.response.send_message(f"{player1.mention}'s choice was {player_choices[player1]}, and {player2.mention} was {player_choices[player2]}!")
        #                 await interaction.followup.delete_message(mainmsg.id)

                
        #         rpsselect.callback = choice_selected
        #         rpsview = View()
        #         rpsview.add_item(rpsselect)
        #         await interaction.response.send_message(f"Challenging {user.display_name}!", view=rpsview, ephemeral=True)

            


        #await interaction.response.send_message(f"{interaction.user.mention} challenges {user.mention} to a game of {game.name}")


    
async def setup(bot):
    await bot.add_cog(ChallengeHandler(bot))