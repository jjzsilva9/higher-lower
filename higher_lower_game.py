"""
Higher/Lower game implementation.
"""

from deck import Deck


class HigherLowerGame:
    """Implements the Higher/Lower card game."""
    
    def __init__(self, include_jokers=False):
        """
        Initialize a new game.
        
        Args:
            include_jokers (bool): Whether to include jokers in the deck
        """
        self.deck = Deck(include_jokers=include_jokers)
        self.current_card = None
        self.next_card = None
        self.score = 0
        self.streak = 0
        self.best_streak = 0
        self.games_played = 0
    
    def start_new_game(self):
        """Start a new game by resetting and shuffling the deck."""
        self.deck.reset()
        self.deck.shuffle()
        self.current_card = self.deck.draw_card()
        self.next_card = None
        self.score = 0
        self.streak = 0
        self.games_played += 1
    
    def make_guess(self, guess):
        """
        Make a guess (higher or lower) and check if it's correct.
        
        Args:
            guess (str): 'higher' or 'lower'
            
        Returns:
            dict: Result containing 'correct', 'next_card', 'message'
        """
        if self.deck.is_empty():
            return {
                'correct': None,
                'next_card': None,
                'message': 'No more cards in the deck!',
                'game_over': True
            }
        
        self.next_card = self.deck.draw_card()
        
        # Determine if guess was correct
        if guess.lower() == 'higher':
            correct = self.next_card.get_value() >= self.current_card.get_value()
        elif guess.lower() == 'lower':
            correct = self.next_card.get_value() <= self.current_card.get_value()
        else:
            return {
                'correct': False,
                'next_card': self.next_card,
                'message': 'Invalid guess! Use "higher" or "lower".',
                'game_over': False
            }
        
        # Update score and streak
        if correct:
            self.score += 1
            self.streak += 1
            if self.streak > self.best_streak:
                self.best_streak = self.streak
            message = "Correct!"
        else:
            self.streak = 0
            message = "Wrong!"
        
        # Move to next card
        self.current_card = self.next_card
        
        return {
            'correct': correct,
            'next_card': self.next_card,
            'message': message,
            'game_over': False
        }
    
    def get_current_card(self):
        """Get the current card."""
        return self.current_card
    
    def get_score(self):
        """Get the current score."""
        return self.score
    
    def get_streak(self):
        """Get the current streak."""
        return self.streak
    
    def get_best_streak(self):
        """Get the best streak."""
        return self.best_streak
    
    def get_cards_remaining(self):
        """Get the number of cards remaining."""
        return self.deck.cards_remaining()
    
    def get_stats(self):
        """
        Get game statistics.
        
        Returns:
            dict: Statistics including score, streak, and cards remaining
        """
        return {
            'score': self.score,
            'streak': self.streak,
            'best_streak': self.best_streak,
            'cards_remaining': self.deck.cards_remaining(),
            'games_played': self.games_played
        }
