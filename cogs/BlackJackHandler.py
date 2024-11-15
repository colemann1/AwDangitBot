import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database
from easy_pil import Editor, Canvas, Font


class InsuranceButtons(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Take Insurance", style=discord.ButtonStyle.green,row=0)
    async def getInsurance(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(ephemeral=True,content="took insurance")

    @discord.ui.button(label="No thanks", style=discord.ButtonStyle.red,row=0)
    async def noInsurance(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(ephemeral=True,content="did not take insurance")

class BlackJackButtons(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label="Stand", style=discord.ButtonStyle.primary,row=0)
    async def stand(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(ephemeral=True,content="stood")

    @discord.ui.button(label="Hit", style=discord.ButtonStyle.primary,row=0)
    async def hit(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(ephemeral=True,content="ow that hurt!")

    @discord.ui.button(label="Double", style=discord.ButtonStyle.gray,row=0)
    async def double(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(ephemeral=True,content="risky but ok")

    @discord.ui.button(label="Surrender", style=discord.ButtonStyle.red,row=0)
    async def surrender(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(ephemeral=True,content="oh well, my money now >:D")



class BlackJackHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("BlackJackHandler is active")

    @app_commands.command(name="blackjack",description="play a game of blackjack!")
    @app_commands.describe(wager="How many chips you are betting")
    async def blackjack(self, interaction: discord.Interaction, wager:app_commands.Range[int, 2, 1000000]):
        balance = Database.GetBalance(interaction.user.id)

        if balance < wager:
            await interaction.response.send_message(content=f"You do not have enough chips for that!\nBalance: {balance}",ephemeral=True)
            return


        #710x890
        pic = Editor("imgs/background.png")
        pic.paste(Editor("imgs/3-P.png"), (210,60))
        pic.paste(Editor("imgs/BACK.png"), (310,60))

        pic.paste(Editor("imgs/10-H.png"), (210,560))
        pic.paste(Editor("imgs/3-C.png"), (310,560))

        pic.text(position=(355,360),text="Dealer's Value: 3+",align="center",color="#ffffff",font=Font.poppins(size=50))
        pic.text(position=(355,480),text="Moore's Value: 13",align="center",color="#ffffff",font=Font.poppins(size=50))

        pic.resize((355,445))
        file = discord.File(fp=pic.image_bytes,filename="output.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://output.png")
        blackjackview = BlackJackButtons()
        insuranceView = InsuranceButtons()
        #embed.set_footer(text="Insurance takes an additional 50% of your bet. \nIf the dealer has blackjack, you keep your bet. \nIf not, then the game continues.")
        await interaction.response.send_message(view=blackjackview,content=f"## Blackjack!\n{interaction.user.mention} bet {wager} chips!",embed=embed, file=file)
        #await interaction.followup.send(view=insuranceView,content="# ⚠ WARNING!! ⚠\n The dealer *may* have a blackjack! Would you like insurance?\n-# Insurance takes an **additional 50%** of your bet.\n-# If the dealer has blackjack, you keep your bet.\n-# If not, then the game continues.")

    
async def setup(bot):
    await bot.add_cog(BlackJackHandler(bot))