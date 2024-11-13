import discord
from libraries.GameLogic import GameLogic



# ROCK PAPER SCISSORS
class RPSButton(discord.ui.Button):
    def __init__(self, label, emoji, value):
        super().__init__(style=discord.ButtonStyle.primary,label=label,emoji=emoji,row=0)
        self.value = value
        self.choices = {
            1:"🪨Rock",
            2:"📄Paper",
            3:"✂️Scissors"
        }

    async def callback(self, interaction:discord.Interaction):
        view:RockPaperScissors = self.view
        if interaction.user.id != view.user1.id and interaction.user.id != view.user2.id:
            await interaction.response.send_message("You are not playing this game!",ephemeral=True)
            return
        await interaction.response.defer()
        #If user is either player1 or player2, set values
        if interaction.user.id == view.user1.id:
            view.embed.set_field_at(0,name=f"{view.user1.display_name}: ✅",value="",inline=False) 
            view.user1_choice = self.value
        elif interaction.user.id == view.user2.id:
            view.embed.set_field_at(1,name=f"{view.user2.display_name}: ✅",value="",inline=False) 
            view.user2_choice = self.value
        #If both values are set, delete msg and send values
        if view.user1_choice != None and view.user2_choice != None:
            await interaction.delete_original_response()
            ##MAIN LOGIC CHECK
            view.winner = GameLogic.RockPaperScissors(view.user1_choice,view.user2_choice,view.user1,view.user2)
            view.user1_choice = self.choices[view.user1_choice] # Sets choices to fancified wording
            view.user2_choice = self.choices[view.user2_choice]
            view.stop()
        else: #Edits msg to show player has selected
            await interaction.edit_original_response(embed=view.embed)

class RockPaperScissors(discord.ui.View):
    def __init__(self, user1:discord.User, user2:discord.User, embed:discord.Embed):
        super().__init__()
        self.user1 = user1
        self.user2 = user2
        self.user1_choice = None
        self.user2_choice = None
        self.embed = embed
        self.winner:discord.User = None
        self.add_item(RPSButton(label="Rock",emoji="🪨",value=1))
        self.add_item(RPSButton(label="Paper",emoji="📄",value=2))
        self.add_item(RPSButton(label="Scissors",emoji="✂️",value=3))

