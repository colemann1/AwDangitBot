import discord
from libraries.GameLogic import GameLogic, BlackjackGame



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
            view.winner = GameLogic.rockPaperScissors(view.user1_choice,view.user2_choice,view.user1,view.user2)
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


# BLACKJACK
class Blackjack(discord.ui.View):
    def __init__(self, user:discord.User, balance, wager):
        super().__init__()
        self.user = user
        self.balance = balance
        self.wager = wager
        self.game = BlackjackGame()
        self.doublebtn = self.children[-2]
        self.bust = None
        self.title = f"## Blackjack!\n{self.user.mention} bet {self.wager} chips!"

    @discord.ui.button(label="Stand", style=discord.ButtonStyle.primary,row=0)
    async def stand(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(f"You are not {self.user.display_name}!",ephemeral=True)
            return
        await interaction.response.defer()
        await interaction.delete_original_response()
        self.stop()


    @discord.ui.button(label="Hit", style=discord.ButtonStyle.primary,row=0)
    async def hit(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(f"You are not {self.user.display_name}!",ephemeral=True)
            return
        ##disable doubling now
        self.remove_item(self.doublebtn)
        self.game.player_hand.append(self.game.deck.deal_card())
        file = discord.File(fp=self.game.generate_board(self.user.display_name).image_bytes,filename="output.png")
        embed = discord.Embed().set_image(url="attachment://output.png")

        ##check bust
        if self.game.hand_value(self.game.player_hand) > 21:
            self.bust = True
            await interaction.response.defer()
            await interaction.delete_original_response()
            await interaction.channel.send(content=self.title,embed=embed, file=file)
            self.stop()
            return
        #continue
        await interaction.response.defer()
        await interaction.delete_original_response()
        await interaction.channel.send(content=self.title,embed=embed, file=file,view=self)


    @discord.ui.button(label="Double", style=discord.ButtonStyle.gray,row=0)
    async def double(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(f"You are not {self.user.display_name}!",ephemeral=True)
            return
        elif self.balance < self.wager:
            await interaction.response.send_message(content=f"You do not have enough chips left to double down!",ephemeral=True)
            return
        self.balance -= self.wager
        self.wager *= 2
        self.title += "\n**Doubled down!!**"
        
        ##HIT
        self.remove_item(self.doublebtn)
        self.game.player_hand.append(self.game.deck.deal_card())
        file = discord.File(fp=self.game.generate_board(self.user.display_name).image_bytes,filename="output.png")
        embed = discord.Embed().set_image(url="attachment://output.png")

        await interaction.response.defer()
        await interaction.delete_original_response()
        ##check bust
        if self.game.hand_value(self.game.player_hand) > 21:
            self.bust = True
            await interaction.channel.send(content=self.title,embed=embed, file=file)
        self.stop()


    @discord.ui.button(label="Surrender", style=discord.ButtonStyle.red,row=0)
    async def surrender(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(f"You are not {self.user.display_name}!",ephemeral=True)
            return

        self.bust = False
        await interaction.response.defer()
        await interaction.delete_original_response()
        file = discord.File(fp=self.game.generate_board(self.user.display_name).image_bytes,filename="output.png")
        embed = discord.Embed().set_image(url="attachment://output.png")
        await interaction.channel.send(content=self.title,embed=embed, file=file)
        self.stop()

class BlackjackInsurance(discord.ui.View):
    def __init__(self, user:discord.User,insuranceamt,can_afford=False):
        super().__init__()
        self.choice = None
        self.user = user
        self.can_afford = can_afford
        self.insuranceamt = insuranceamt

    @discord.ui.button(label="Take Insurance", style=discord.ButtonStyle.green,row=0)
    async def getInsurance(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(f"You are not {self.user.display_name}!",ephemeral=True)
            return

        await interaction.response.defer()
        await interaction.delete_original_response()
        if self.can_afford: 
            await interaction.channel.send(content=f"You took the insurance for **{self.insuranceamt}** chips.",delete_after=5)
            self.choice = True
        else:
            await interaction.channel.send(content=f"You do not have enough chips to take the insurance, sorry!",delete_after=5)
            self.choice = False
        self.stop()

    @discord.ui.button(label="No thanks", style=discord.ButtonStyle.red,row=0)
    async def noInsurance(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id != self.user.id:
            await interaction.response.send_message(f"You are not {self.user.display_name}!",ephemeral=True)
            return
        
        await interaction.response.defer()
        await interaction.delete_original_response()
        await interaction.channel.send(content=f"You ignored the insurance.",delete_after=5)
        self.choice = False
        self.stop()