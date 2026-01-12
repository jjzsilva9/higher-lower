"""
Card module - Defines a playing card with suit and rank.
"""

class Card:
    """Represents a single playing card."""
    
    # Define suits and ranks
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    # Map ranks to values (for comparison)
    RANK_VALUES = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
    }
    
    def __init__(self, suit, rank):
        """
        Initialize a card with a suit and rank.
        
        Args:
            suit (str): The suit of the card (Hearts, Diamonds, Clubs, Spades, or Red/Black for Jokers)
            rank (str): The rank of the card (2-10, Jack, Queen, King, Ace, or Joker)
        """
        # Allow special suits for Jokers
        if rank == 'Joker':
            if suit not in ['Red', 'Black']:
                raise ValueError(f"Joker must have suit 'Red' or 'Black', not '{suit}'")
        elif suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Must be one of {self.SUITS}")
        
        if rank not in self.RANKS and rank != 'Joker':
            raise ValueError(f"Invalid rank: {rank}. Must be one of {self.RANKS} or 'Joker'")
        
        self.suit = suit
        self.rank = rank
    
    def get_value(self):
        """
        Get the numeric value of the card for comparison.
        
        Returns:
            int: The numeric value of the card
        """
        if self.rank == 'Joker':
            return 15  # Joker is highest
        return self.RANK_VALUES[self.rank]
    
    def __str__(self):
        """String representation of the card."""
        if self.rank == 'Joker':
            return f"Joker ({self.suit})"
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        """Developer-friendly representation of the card."""
        return f"Card('{self.suit}', '{self.rank}')"
    
    def __eq__(self, other):
        """Check if two cards are equal."""
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.rank == other.rank
    
    def __lt__(self, other):
        """Check if this card is less than another card."""
        if not isinstance(other, Card):
            return NotImplemented
        return self.get_value() < other.get_value()
    
    def __gt__(self, other):
        """Check if this card is greater than another card."""
        if not isinstance(other, Card):
            return NotImplemented
        return self.get_value() > other.get_value()
