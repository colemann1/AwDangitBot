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
