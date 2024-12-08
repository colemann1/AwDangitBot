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

class RouletteGame:
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
        self.result = self.spin_roulette()

    def spin_roulette(self):
        """Simulates spinning the roulette wheel and returns the result."""
        selected_number = random.choice(self.roulette_wheel)
        selected_color = self.colors[selected_number]
        print(f"The roulette wheel spun: {selected_number} ({selected_color})")
        return selected_number, selected_color

    def evaluate_bet(self, bet):
        """Evaluates the result of the bet against the spin result."""
        number, color = self.result

        match bet:
            case bet if bet == "Red" or bet == "Black": ## Color, returns 2x win, 0x lose
                if color == bet:
                    return 2
                else:
                    return 0
            case bet if bet == "Odd" or bet == "Even": ## Odd/Even, returns 2x win, 0x lose
                if number in ["00", 0]:
                    return 0
                elif (number % 2 == 0 and bet == "Even") or (number % 2 == 1 and bet == "Odd"):
                    return 2
                else:
                    return 0
            case bet if bet == "High" or bet == "Low": ## High/Low, returns 2x win, 0x lose
                if number in ["00", 0]:
                    return 0
                elif (1 <= number <= 18 and bet == "Low") or (19 <= number <= 36 and bet == "High"):
                    return 2
                else:
                    return 0
            case bet if str(bet).startswith("Col"): ## Columns, returns 3x win, 0x lose
                if number in ["00", 0]:
                    return 0
                elif (number - 1) % 3 == 0 and bet == "Col1":
                    return 3
                elif (number - 2) % 3 == 0 and bet == "Col2":
                    return 3
                elif (number - 3) % 3 == 0 and bet == "Col3":
                    return 3
                else:
                    return 0
            case bet if int(bet) in list(range(0, 37)) or bet == "00": ## Number, returns 36x win, 0x lose
                if str(number) == str(bet):
                    return 36
                else:
                    return 0    