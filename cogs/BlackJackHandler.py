import discord
from discord import app_commands
from discord.ext import commands
from libraries.ApiClient import Database
from libraries.GameViews import Blackjack, BlackjackInsurance
from time import sleep

class BlackjackHandler(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    #Notify if cog is working
    @commands.Cog.listener()
    async def on_ready(self):
        print("BlackjackHandler is active")

    @app_commands.command(name="blackjack",description="play a game of blackjack!")
    @app_commands.describe(wager="How many chips you are betting")
    async def blackjack(self, interaction: discord.Interaction, wager:app_commands.Range[int, 2, 1000000]):
        oldbalance = await Database.GetBalance(interaction.user.id)
        insurance = 0
        insurancevalue = ""

        async def GameEnd(mult):
            if mult > 1:
                await Database.IncGameWins(interaction.user.id,"BJ")
            await Database.SetBalance(interaction.user.id,(blackjack.balance+round(blackjack.wager*mult)))

        ##Error checks
        if oldbalance < wager:
            await interaction.response.send_message(content=f"You do not have enough chips for that!\nBalance: {oldbalance}",ephemeral=True)
            return
        oldbalance -= wager

        ##First board generation/bj instance
        blackjack = Blackjack(interaction.user,oldbalance,wager)
        file = discord.File(fp=blackjack.game.generate_board(interaction.user.display_name).image_bytes,filename="output.png")
        embed = discord.Embed().set_image(url="attachment://output.png")
        #if dealer has blackjack revealed hand
        endfile = discord.File(fp=blackjack.game.generate_board(interaction.user.display_name,hide_dealer=False).image_bytes,filename="blackjack.png")
        endembed = discord.Embed().set_image(url="attachment://blackjack.png")

        ##Send first message without view
        await interaction.response.send_message(content=blackjack.title,embed=embed, file=file)

        if blackjack.game.check_for_blackjack(blackjack.game.player_hand): ##User blackjack checks
            if blackjack.game.check_for_blackjack(blackjack.game.dealer_hand):## User+Dealer have blackjack
                #displays the dealers hand
                await interaction.edit_original_response(content=blackjack.title,embed=endembed,attachments=[endfile])
                await interaction.followup.send(f"## You got a blackjack, but the dealer did too!\nYour wager has been returned to you.")
                await GameEnd(1) #return wager
                return ##END GAME
            await interaction.followup.send(f"## You got a blackjack!\nCongrats you have won 1.5x your wager!\n+{round(wager * 1.5)} chips")
            await GameEnd(2.5) #give winnings
            return ##END GAME

        if blackjack.game.dealer_hand[1].rank == 'Ace': ##Insurance checks
            insuranceView = BlackjackInsurance(interaction.user,round(wager/2),can_afford=(True if blackjack.balance >= round(wager/2) else False))
            await interaction.followup.send(view=insuranceView,content=f"# ⚠ WARNING!! ⚠\n The dealer *might* have a blackjack! Would you like insurance?\n-# Insurance takes an **additional 50%** of your bet ({round(wager/2)} chips).\n-# If the dealer has blackjack, you keep your initial bet.\n-# If not, then the game continues.")
            if await insuranceView.wait() == False:
                #If user took insurance change bal
                if insuranceView.choice == True: 
                    insurance = round(wager/2)
                    blackjack.balance -= insurance 
                    blackjack.title += f"\nTook insurance ({insurance} chips)"
                    insurancevalue = f"\n-{insurance} chips for insurance."
                #no blackjack
                if blackjack.game.check_for_blackjack(blackjack.game.dealer_hand) == False:
                    await interaction.channel.send(content="The dealer does **not** have a blackjack, the game will continue...",delete_after=5)
                else: #has blackjack
                    await interaction.edit_original_response(content=blackjack.title,embed=endembed,attachments=[endfile])
                    if insuranceView.choice == True: #took insurance
                        await interaction.channel.send(content=f"**The dealer has a blackjack**, but luckily you have insurance!\nYour wager has been returned\n-{insurance} chips for insurance.")
                        await GameEnd(1) ##return wager
                        return ##END GAME
                    else:
                        await interaction.channel.send(content=f"**The dealer has a blackjack!** Should have taken the insurance!\n-{wager} chips")
                        await GameEnd(0) ##Lost Game
                        return ##END GAME
            else: ##Timeout!!
                await interaction.channel.send(content=f"{interaction.user.mention}, you took too long to respond!\n-{wager} chips")
                await GameEnd(0) ##Lost Game
                return ##END GAME
            
        ##Main
        await interaction.edit_original_response(content=blackjack.title,view=blackjack)
        ##DEALERS TURN/LOSS
        if await blackjack.wait() == False:
            if blackjack.bust == True: ##Bust
                await interaction.channel.send(content=f"## Oops, you went over 21! That's a bust.\n-{blackjack.wager} chips{insurancevalue}")
                await GameEnd(0) ##Lost Game
                return ##END GAME
            elif blackjack.bust == False: ##Surrender
                await interaction.channel.send(content=f"## You surrendered!\nSometimes knowing when to quit is the real win.\n-{blackjack.wager} chips{insurancevalue}")
                await GameEnd(0) ##Lost Game
                return ##END GAME
            
            file = discord.File(fp=blackjack.game.generate_board(blackjack.user.display_name).image_bytes,filename="output.png")
            embed = discord.Embed(title="Dealer's Turn...").set_image(url="attachment://output.png")
            ##Dealers turn
            msg = await interaction.channel.send(content=blackjack.title,embed=embed, file=file)
            while True:
                dealfile = discord.File(fp=blackjack.game.generate_board(interaction.user.display_name,hide_dealer=False).image_bytes,filename="dealer.png")
                dealembed = discord.Embed(title="Dealer's Turn...").set_image(url="attachment://dealer.png")
                sleep(2)
                await msg.edit(content=blackjack.title,embed=dealembed,attachments=[dealfile])

                if blackjack.game.hand_value(blackjack.game.dealer_hand) > 21:
                    ##Dealer busts player wins
                    await interaction.channel.send(f"## The Dealer busted! You Win!!\n+{blackjack.wager} chips{insurancevalue}")
                    await GameEnd(2) ##Won Game!!
                    return ##END GAME
                elif blackjack.game.hand_value(blackjack.game.dealer_hand) < 17:
                    blackjack.game.dealer_hand.append(blackjack.game.deck.deal_card())
                else: #Dealer stands
                    #True = win, False = lose, None = tie
                    status = blackjack.game.determine_winner()
                    if status == True:
                        await interaction.channel.send(f"## You have a higher value! You Win!!\n+{blackjack.wager} chips{insurancevalue}")
                        await GameEnd(2) ##Won Game!!
                        return ##END GAME
                    elif status == False:
                        await interaction.channel.send(f"## The Dealer has a higher value, sorry!\n-{blackjack.wager} chips{insurancevalue}")
                        await GameEnd(0) ##Lost game
                        return ##END GAME
                    else: ##tie
                        await interaction.channel.send(f"## You Tied with The Dealer!\nYour wager has been returned{insurancevalue}")
                        await GameEnd(1) ##Tie
                        return ##END GAME
    


        else: ##Timeout!!
            await interaction.channel.send(content=f"{interaction.user.mention}, you took too long to respond!\n-{blackjack.wager} chips{insurancevalue}")
            await GameEnd(0) ##Lost Game
            return ##END GAME



    
async def setup(bot):
    await bot.add_cog(BlackjackHandler(bot))