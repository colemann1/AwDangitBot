import random

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
        
    def PNG(self):
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
    def ToString(self):
        """Returns a string representation of the card."""
        return f"{self.rank} of {self.suit} (Value: {self.value})"


class Deck:
    """Represents a deck of 52 playing cards."""
    
    def __init__(self):
        """Initializes the deck with 52 cards."""
        self.cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]
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
        return f"Deck of {len(self.cards)} cards: " + ", ".join(card.ToString() for card in self.cards)

class GameLogic():


    def RockPaperScissors(choice1, choice2,user1,user2):
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
        self.deck = Deck()
        self.player_hand = []
        self.split_hand = None  # For splitting
        self.dealer_hand = []
        self.insurance_taken = False

    def calculate_hand_value(self, hand):
        """Calculates the value of a hand, handling the Ace's dual value."""
        value = sum(card.value for card in hand)
        aces = sum(1 for card in hand if card.rank == 'Ace')
        while value > 21 and aces > 0:
            value -= 10  # Treat an Ace as 1 instead of 11
            aces -= 1
        return value

    def display_hand(self, hand, is_dealer=False, hide_first_card=False):
        """Displays the player's or dealer's hand."""
        if hide_first_card and is_dealer:
            print(f"Dealer's hand: [Hidden], {hand[1].ToString()}")
        else:
            hand_type = "Dealer's" if is_dealer else "Player's"
            print(f"{hand_type} hand: {', '.join(card.ToString() for card in hand)}")

    def check_for_blackjack(self, hand):
        """Checks if a hand has a Blackjack (value of 21 with 2 cards)."""
        return len(hand) == 2 and self.calculate_hand_value(hand) == 21

    def play_game(self):
        """Plays a single round of Blackjack."""
        print("Welcome to Blackjack with Splitting and Insurance!\n")

        # Initial deal
        self.player_hand = self.deck.deal_hand(2)
        self.dealer_hand = self.deck.deal_hand(2)

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
        while self.calculate_hand_value(self.dealer_hand) < 17:
            print("Dealer hits.")
            self.dealer_hand.append(self.deck.deal_card())
            self.display_hand(self.dealer_hand, is_dealer=True)

        dealer_value = self.calculate_hand_value(self.dealer_hand)
        print(f"\nDealer's final hand value: {dealer_value}")

        # Determine the outcome for each hand
        self.determine_winner(self.player_hand, "Your main hand")
        if self.split_hand:
            self.determine_winner(self.split_hand, "Your split hand")

    def play_hand(self, hand):
        """Handles the play for a single hand."""
        while True:
            value = self.calculate_hand_value(hand)
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

    def determine_winner(self, hand, hand_name):
        """Determines the winner for a specific hand."""
        player_value = self.calculate_hand_value(hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        print(f"\n{hand_name} value: {player_value}")
        if dealer_value > 21 or player_value > dealer_value:
            print(f"{hand_name} wins!")
        elif dealer_value > player_value:
            print(f"{hand_name} loses!")
        else:
            print(f"{hand_name} ties!")
