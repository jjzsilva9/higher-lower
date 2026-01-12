"""
Deck module - Manages a deck of playing cards.
"""

import random
from card import Card


class Deck:
    """Represents a deck of playing cards."""
    
    def __init__(self, include_jokers=False):
        """
        Initialize a deck of cards.
        
        Args:
            include_jokers (bool): Whether to include 2 jokers in the deck
        """
        self.cards = []
        self.include_jokers = include_jokers
        self.reset()
    
    def reset(self):
        """Reset the deck to a full standard 52-card deck (plus jokers if enabled)."""
        self.cards = []
        
        # Create all standard cards
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(suit, rank))
        
        # Add jokers if requested
        if self.include_jokers:
            self.cards.append(Card('Red', 'Joker'))
            self.cards.append(Card('Black', 'Joker'))
    
    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)
    
    def draw_card(self):
        """
        Draw a card from the top of the deck.
        
        Returns:
            Card: The drawn card, or None if deck is empty
        """
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
    
    def cards_remaining(self):
        """
        Get the number of cards remaining in the deck.
        
        Returns:
            int: Number of cards left in the deck
        """
        return len(self.cards)
    
    def is_empty(self):
        """
        Check if the deck is empty.
        
        Returns:
            bool: True if deck is empty, False otherwise
        """
        return len(self.cards) == 0
    
    def __str__(self):
        """String representation of the deck."""
        joker_str = " (with Jokers)" if self.include_jokers else ""
        return f"Deck with {len(self.cards)} cards{joker_str}"
    
    def __len__(self):
        """Get the number of cards in the deck."""
        return len(self.cards)
