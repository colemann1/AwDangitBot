import random
from easy_pil import Editor,Font

class Card:
    """Represents a single playing card."""
    
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    # Card values mapping: 2-10 are face value, Jack, Queen, King are 10, Ace is 11
    RANK_VALUES = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }

    def __init__(self, rank, suit):
        """Initializes a card with a specific rank and suit."""
        if rank not in Card.RANKS or suit not in Card.SUITS:
            raise ValueError(f"Invalid rank {rank} or suit {suit}")
        self.rank = rank
        self.suit = suit
        self.value = Card.RANK_VALUES[rank]  # Assign the value based on the rank
        
    def png(self):
        match self.suit:
            case 'Hearts':
                match self.rank:
                    case '10':
                        return "10-H.png"
                    case '9':
                        return "9-H.png"
                    case '8':
                        return "8-H.png"
                    case '7':
                        return "7-H.png"
                    case '6':
                        return "6-H.png"
                    case '5':
                        return "5-H.png"
                    case '4':
                        return "4-H.png"
                    case '3':
                        return "3-H.png"
                    case '2':
                        return "2-H.png"
                    case 'Jack':
                        return "J-H.png"
                    case 'Queen':
                        return "Q-H.png"
                    case 'King':
                        return "K-H.png"
                    case 'Ace':
                        return "A-H.png"
            case 'Diamonds':
                 match self.rank:
                    case '10':
                        return "10-D.png"
                    case '9':
                        return "9-D.png"
                    case '8':
                        return "8-D.png"
                    case '7':
                        return "7-D.png"
                    case '6':
                        return "6-D.png"
                    case '5':
                        return "5-D.png"
                    case '4':
                        return "4-D.png"
                    case '3':
                        return "3-D.png"
                    case '2':
                        return "2-D.png"
                    case 'Jack':
                        return "J-D.png"
                    case 'Queen':
                        return "Q-D.png"
                    case 'King':
                        return "K-D.png"
                    case 'Ace':
                        return "A-D.png"
            case 'Clubs':
                 match self.rank:
                    case '10':
                        return "10-C.png"
                    case '9':
                        return "9-C.png"
                    case '8':
                        return "8-C.png"
                    case '7':
                        return "7-C.png"
                    case '6':
                        return "6-C.png"
                    case '5':
                        return "5-C.png"
                    case '4':
                        return "4-C.png"
                    case '3':
                        return "3-C.png"
                    case '2':
                        return "2-C.png"
                    case 'Jack':
                        return "J-C.png"
                    case 'Queen':
                        return "Q-C.png"
                    case 'King':
                        return "K-C.png"
                    case 'Ace':
                        return "A-C.png"
            case 'Spades':
                 match self.rank:
                    case '10':
                        return "10-P.png"
                    case '9':
                        return "9-P.png"
                    case '8':
                        return "8-P.png"
                    case '7':
                        return "7-P.png"
                    case '6':
                        return "6-P.png"
                    case '5':
                        return "5-P.png"
                    case '4':
                        return "4-P.png"
                    case '3':
                        return "3-P.png"
                    case '2':
                        return "2-P.png"
                    case 'Jack':
                        return "J-P.png"
                    case 'Queen':
                        return "Q-P.png"
                    case 'King':
                        return "K-P.png"
                    case 'Ace':
                        return "A-P.png"  
     
    def toString(self):
        """Returns a string representation of the card."""
        return f"{self.rank} of {self.suit} (Value: {self.value})"


class Deck:
    """Represents a deck of 52 playing cards."""
    
    def __init__(self,num_of_decks=1):
        self.cards = []
        """Initializes the deck with 52 cards."""
        for _ in range(num_of_decks):
            self.cards += [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
            self.shuffle()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deals one card from the deck."""
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt!")
        return self.cards.pop()

    def deal_hand(self, hand_size):
        """Deals a hand of a specified number of cards."""
        if hand_size > len(self.cards):
            raise ValueError("Not enough cards left to deal the hand.")
        hand = [self.deal_card() for _ in range(hand_size)]
        return hand

    def reset_deck(self):
        """Resets the deck to 52 cards and shuffles it."""
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
        self.shuffle()

    def remaining_cards(self):
        """Returns the number of remaining cards in the deck."""
        return len(self.cards)

    def __repr__(self):
        """Returns a string representation of the deck using the cards' ToString method."""
        return f"Deck of {len(self.cards)} cards: " + ", ".join(card.toString() for card in self.cards)

class GameLogic:

    def rockPaperScissors(choice1, choice2,user1,user2):
        outcome = choice1 - choice2
        if outcome == 0:
            return None
        elif outcome == 1 or outcome == -2:
            return user1
        else:
            return user2
            
class BlackjackGame:
    """A Blackjack game with splitting and insurance options."""

    def __init__(self):
        self.deck = Deck(8)
        self.split_hand = None  # For splitting
        self.player_hand = self.deck.deal_hand(2)
        self.dealer_hand = self.deck.deal_hand(2)
        # [Card('King',"Hearts"),Card("Ace","Spades")]

    def hand_value(self, hand):
        """Calculates the value of a hand, handling the Ace's dual value."""
        value = sum(card.value for card in hand)
        aces = sum(1 for card in hand if card.rank == 'Ace')
        while value > 21 and aces > 0:
            value -= 10  # Treat an Ace as 1 instead of 11
            aces -= 1
        return value

    def display_hand(self, hand:list[Card], hide_first_card=False):
        """Displays the player's or dealer's hand."""
        cardpos = [200]
        disp = Editor("imgs/handtemp.png")
        for _ in range(len(hand)-1):
            cardpos = [x - 50 for x in cardpos]
            cardpos.append(cardpos[-1]+100)
        if hide_first_card:
            disp.paste(Editor("imgs/BACK.png"), (cardpos[0],0))
            disp.paste(Editor("imgs/" + hand[1].png()), (cardpos[1],0))
        else:
            for i in range(len(hand)):
                disp.paste(Editor("imgs/" + hand[i].png()), (cardpos[i],0))
        return disp

    def generate_board(self, username, hide_dealer=True):
        pic = Editor("imgs/background.png")
        pic.paste(self.display_hand(self.dealer_hand,hide_first_card=hide_dealer), (60,60))
        pic.paste(self.display_hand(self.player_hand), (60,560))
        if hide_dealer==True:
            pic.text(position=(355,360),text=f"Dealer's Hand: {self.dealer_hand[1].value}+",align="center",color="#ffffff",font=Font.poppins(size=50))
        else:
            pic.text(position=(355,360),text=f"Dealer's Hand: {self.hand_value(self.dealer_hand)}",align="center",color="#ffffff",font=Font.poppins(size=50))
        pic.text(position=(355,480),text=f"{username}'s Hand: {self.hand_value(self.player_hand)}",align="center",color="#ffffff",font=Font.poppins(size=50))
        pic.resize((355,445))
        return pic

    def check_for_blackjack(self, hand):
        """Checks if a hand has a Blackjack (value of 21 with 2 cards)."""
        return len(hand) == 2 and self.hand_value(hand) == 21

    def play_game(self):
        """Plays a single round of Blackjack."""
        print("Welcome to Blackjack with Splitting and Insurance!\n")

        # Display hands
        self.display_hand(self.player_hand)
        self.display_hand(self.dealer_hand, is_dealer=True, hide_first_card=True)

        # Insurance Option
        if self.dealer_hand[0].rank == 'Ace':
            print("\nDealer shows an Ace. Would you like to take insurance? (Half your bet)")
            choice = input("Enter 'Y' for Yes or 'N' for No: ").lower()
            if choice == 'y':
                self.insurance_taken = True

        # Check for Blackjack
        if self.check_for_blackjack(self.dealer_hand):
            self.display_hand(self.dealer_hand, is_dealer=True)
            print("\nDealer has Blackjack!")
            if self.insurance_taken:
                print("You took insurance. It's a push on your main bet!")
            else:
                print("You lose!")
            return

        if self.check_for_blackjack(self.player_hand):
            print("\nBlackjack! You win!")
            return

        # Splitting Option
        if self.player_hand[0].rank == self.player_hand[1].rank:
            print("\nYou have two cards of the same rank. Would you like to split? (Requires doubling your bet)")
            choice = input("Enter 'Y' for Yes or 'N' for No: ").lower()
            if choice == 'y':
                self.split_hand = [self.player_hand.pop()]
                self.player_hand.append(self.deck.deal_card())
                self.split_hand.append(self.deck.deal_card())
                print("\nFirst hand:")
                self.display_hand(self.player_hand)
                print("\nSecond hand:")
                self.display_hand(self.split_hand)

        # Play both hands if split
        if self.split_hand:
            print("\nPlaying first hand:")
            if not self.play_hand(self.player_hand):
                return

            print("\nPlaying second hand:")
            if not self.play_hand(self.split_hand):
                return
        else:
            if not self.play_hand(self.player_hand):
                return

        # Dealer's turn
        print("\nDealer's turn...")
        self.display_hand(self.dealer_hand, is_dealer=True)
        while self.hand_value(self.dealer_hand) < 17:
            print("Dealer hits.")
            self.dealer_hand.append(self.deck.deal_card())
            self.display_hand(self.dealer_hand, is_dealer=True)

        dealer_value = self.hand_value(self.dealer_hand)
        print(f"\nDealer's final hand value: {dealer_value}")

        # Determine the outcome for each hand
        self.determine_winner(self.player_hand, "Your main hand")
        if self.split_hand:
            self.determine_winner(self.split_hand, "Your split hand")

    def play_hand(self, hand):
        """Handles the play for a single hand."""
        while True:
            value = self.hand_value(hand)
            print(f"\nCurrent hand value: {value}")
            if value > 21:
                print("Bust! You lose this hand.")
                return False
            move = input("Would you like to [H]it or [S]tand? ").lower()
            if move == 'h':
                hand.append(self.deck.deal_card())
                self.display_hand(hand)
            elif move == 's':
                break
            else:
                print("Invalid input. Please enter 'H' to Hit or 'S' to Stand.")
        return True

    def determine_winner(self):
        """Determines the winner of the game"""
        player_value = self.hand_value(self.player_hand)
        dealer_value = self.hand_value(self.dealer_hand)
        if player_value > dealer_value:
            return True ##player wins
        elif dealer_value > player_value:
            return False ##dealer wins
        else:
            return None ##tie

class Roulette:
    def __init__(self):
        # Initialize the Roulette wheel and colors
        self.roulette_wheel = [0, "00"] + list(range(1, 37))
        self.colors = {
            0: "Green", "00": "Green",
            1: "Red", 2: "Black", 3: "Red", 4: "Black", 5: "Red", 6: "Black",
            7: "Red", 8: "Black", 9: "Red", 10: "Black", 11: "Black", 12: "Red",
            13: "Black", 14: "Red", 15: "Black", 16: "Red", 17: "Black", 18: "Red",
            19: "Red", 20: "Black", 21: "Red", 22: "Black", 23: "Red", 24: "Black",
            25: "Red", 26: "Black", 27: "Red", 28: "Black", 29: "Black", 30: "Red",
            31: "Black", 32: "Red", 33: "Black", 34: "Red", 35: "Black", 36: "Red"
        }

    def spin_roulette(self):
        """Simulates spinning the roulette wheel and returns the result."""
        selected_number = random.choice(self.roulette_wheel)
        selected_color = self.colors[selected_number]
        print(f"The roulette wheel spun: {selected_number} ({selected_color})")
        return selected_number, selected_color

    def place_bet(self):
        """Prompts the user to place a bet and returns the bet type and value."""
        print("Betting options:")
        print("1. Bet on a specific number (0, 00, or 1-36)")
        print("2. Bet on a color (Red or Black)")
        print("3. Bet on Odd or Even")
        print("4. Bet on High or Low (1-18 or 19-36)")
        print("5. Bet on a Column (1st, 2nd, 3rd)")
        choice = int(input("Enter the type of bet you'd like to place (1-5): "))

        if choice == 1:
            bet = input("Enter the number you want to bet on (0, 00, or 1-36): ")
            return "number", bet
        elif choice == 2:
            bet = input("Enter the color you want to bet on (Red or Black): ").capitalize()
            return "color", bet
        elif choice == 3:
            bet = input("Enter 'Odd' or 'Even': ").capitalize()
            return "odd/even", bet
        elif choice == 4:
            bet = input("Enter 'Low' (1-18) or 'High' (19-36): ").capitalize()
            return "high/low", bet
        elif choice == 5:
            bet = input("Enter the column ('1st', '2nd', or '3rd'): ").lower()
            return "column", bet
        else:
            print("Invalid bet choice!")
            return None, None

    def evaluate_bet(self, bet_type, bet, spin_result):
        """Evaluates the result of the bet against the spin result."""
        number, color = spin_result

        if bet_type == "number":
            if str(number) == bet:
                print("You win! Your number was correct.")
            else:
                print("You lose. The number didn't match.")
        elif bet_type == "color":
            if color == bet:
                print("You win! Your color was correct.")
            else:
                print("You lose. The color didn't match.")
        elif bet_type == "odd/even":
            if number in ["00", 0]:
                print("You lose. It's neither odd nor even.")
            elif (number % 2 == 0 and bet == "Even") or (number % 2 == 1 and bet == "Odd"):
                print("You win! Your choice was correct.")
            else:
                print("You lose. The choice didn't match.")
        elif bet_type == "high/low":
            if number in ["00", 0]:
                print("You lose. It's not high or low.")
            elif (1 <= number <= 18 and bet == "Low") or (19 <= number <= 36 and bet == "High"):
                print("You win! Your choice was correct.")
            else:
                print("You lose. The choice didn't match.")
        elif bet_type == "column":
            if number in ["00", 0]:
                print("You lose. It's not in any column.")
            elif (number - 1) % 3 == 0 and bet == "1st":
                print("You win! Your column was correct.")
            elif (number - 2) % 3 == 0 and bet == "2nd":
                print("You win! Your column was correct.")
            elif (number - 3) % 3 == 0 and bet == "3rd":
                print("You win! Your column was correct.")
            else:
                print("You lose. The column didn't match.")

    def play(self):
        """Main game loop for testing the class independently."""
        while True:
            bet_type, bet = self.place_bet()
            if bet_type is None:
                continue

            spin_result = self.spin_roulette()
            self.evaluate_bet(bet_type, bet, spin_result)

            play_again = input("Do you want to play again? (yes or no): ").lower()
            if play_again != "yes":
                print("Thanks for playing!")
                break
