"""
Blackjack game implementation.
"""

from deck import Deck


class BlackjackGame:
    """Implements a simplified Blackjack game (player vs dealer)."""
    
    def __init__(self):
        """Initialize a new Blackjack game."""
        self.deck = Deck(include_jokers=False)
        self.player_hand = []
        self.dealer_hand = []
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def start_new_game(self):
        """Start a new game by resetting and dealing cards."""
        self.deck.reset()
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []
        
        # Deal initial cards
        self.player_hand.append(self.deck.draw_card())
        self.dealer_hand.append(self.deck.draw_card())
        self.player_hand.append(self.deck.draw_card())
        self.dealer_hand.append(self.deck.draw_card())
        
        self.games_played += 1
    
    def calculate_hand_value(self, hand):
        """
        Calculate the value of a hand in Blackjack.
        
        Args:
            hand (list): List of Card objects
            
        Returns:
            int: The value of the hand (Aces count as 11 or 1)
        """
        value = 0
        aces = 0
        
        for card in hand:
            rank = card.rank
            if rank == 'Ace':
                aces += 1
                value += 11
            elif rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                value += int(rank)
        
        # Adjust for aces if value is over 21
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    def hit(self):
        """
        Player draws a card.
        
        Returns:
            dict: Result containing 'card', 'hand_value', 'busted'
        """
        card = self.deck.draw_card()
        self.player_hand.append(card)
        hand_value = self.calculate_hand_value(self.player_hand)
        
        return {
            'card': card,
            'hand_value': hand_value,
            'busted': hand_value > 21
        }
    
    def dealer_play(self):
        """
        Dealer plays according to standard rules (hit until 17 or higher).
        
        Returns:
            dict: Dealer's final hand value and whether they busted
        """
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw_card())
        
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        return {
            'hand_value': dealer_value,
            'busted': dealer_value > 21
        }
    
    def determine_winner(self):
        """
        Determine the winner of the game.
        
        Returns:
            str: 'player', 'dealer', or 'tie'
        """
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        
        # Player busted
        if player_value > 21:
            self.losses += 1
            return 'dealer'
        
        # Dealer busted
        if dealer_value > 21:
            self.wins += 1
            return 'player'
        
        # Compare values
        if player_value > dealer_value:
            self.wins += 1
            return 'player'
        elif dealer_value > player_value:
            self.losses += 1
            return 'dealer'
        else:
            self.ties += 1
            return 'tie'
    
    def get_player_hand(self):
        """Get the player's hand."""
        return self.player_hand
    
    def get_dealer_hand(self):
        """Get the dealer's hand."""
        return self.dealer_hand
    
    def get_dealer_visible_card(self):
        """Get the dealer's visible card (first card)."""
        return self.dealer_hand[0] if self.dealer_hand else None
    
    def get_stats(self):
        """
        Get game statistics.
        
        Returns:
            dict: Statistics including wins, losses, and ties
        """
        return {
            'games_played': self.games_played,
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties
        }
