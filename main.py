"""
CLI interface for the card games.
"""

import os
import sys
from higher_lower_game import HigherLowerGame
from blackjack_game import BlackjackGame


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Print the game header."""
    print("=" * 60)
    print()


def print_card_art(card):
    """
    Print ASCII art representation of a card.
    
    Args:
        card: The Card object to display
    """
    if not card:
        return
    
    # Get card display info
    rank = card.rank
    suit = card.suit
    
    # Suit symbols
    suit_symbols = {
        'Hearts': '♥',
        'Diamonds': '♦',
        'Clubs': '♣',
        'Spades': '♠',
        'Red': 'J',
        'Black': 'J'
    }
    
    symbol = suit_symbols.get(suit, suit[0])
    
    # Create card art
    print("┌─────────┐")
    print(f"│ {rank:<7} │")
    print(f"│    {symbol}    │")
    print(f"│ {rank:>7} │")
    print("└─────────┘")


def play_higher_lower():
    """Play the Higher/Lower game."""
    clear_screen()
    print_header()
    print("HIGHER OR LOWER")
    print("=" * 60)
    print()
    
    # Ask about jokers
    use_jokers = input("Include Jokers? (y/n): ").lower() == 'y'
    game = HigherLowerGame(include_jokers=use_jokers)
    
    while True:
        clear_screen()
        print_header()
        print("HIGHER OR LOWER")
        print("=" * 60)
        print()
        
        game.start_new_game()
        print("Game started! Guess if the next card will be HIGHER or LOWER.")
        print()
        
        # Game loop
        while not game.deck.is_empty():
            stats = game.get_stats()
            print(f"Score: {stats['score']} | Streak: {stats['streak']} | Best: {stats['best_streak']} | Cards left: {stats['cards_remaining']}")
            print()
            
            print("Current card:")
            print_card_art(game.get_current_card())
            print()
            
            # Get user guess
            guess = input("Your guess (higher/lower/quit): ").lower().strip()
            
            if guess == 'quit':
                print("\nThanks for playing!")
                return
            
            if guess not in ['higher', 'lower']:
                print("Invalid input! Please enter 'higher' or 'lower'.")
                input("Press Enter to continue...")
                continue
            
            # Make the guess
            result = game.make_guess(guess)
            
            print()
            print(result['message'])
            print()
            print("Next card was:")
            print_card_art(result['next_card'])
            print()
            
            if not result['correct']:
                print("Game Over!")
                final_stats = game.get_stats()
                print(f"Final Score: {final_stats['score']}")
                print(f"Best Streak: {final_stats['best_streak']}")
                break
            
            input("Press Enter to continue...")
            clear_screen()
            print_header()
            print("HIGHER OR LOWER")
            print("=" * 60)
            print()
        
        if game.deck.is_empty():
            print("Congratulations! You've gone through the entire deck!")
            final_stats = game.get_stats()
            print(f"Final Score: {final_stats['score']}")
            print(f"Best Streak: {final_stats['best_streak']}")
        
        print()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("\nThanks for playing Higher or Lower!")


def play_blackjack():
    """Play the Blackjack game."""
    clear_screen()
    print_header()
    print("BLACKJACK")
    print("=" * 60)
    print()
    
    game = BlackjackGame()
    
    while True:
        clear_screen()
        print_header()
        print("BLACKJACK")
        print("=" * 60)
        print()
        
        game.start_new_game()
        
        print("Dealer's visible card:")
        print_card_art(game.get_dealer_visible_card())
        print()
        
        print("Your hand:")
        for card in game.get_player_hand():
            print(f"  - {card}")
        print(f"Hand value: {game.calculate_hand_value(game.get_player_hand())}")
        print()
        
        # Player's turn
        while True:
            player_value = game.calculate_hand_value(game.get_player_hand())
            
            if player_value > 21:
                print("BUST! You went over 21!")
                break
            
            if player_value == 21:
                print("BLACKJACK!")
                break
            
            action = input("Hit or Stand? (h/s/quit): ").lower().strip()
            
            if action == 'quit':
                print("\nThanks for playing!")
                return
            
            if action == 'h':
                result = game.hit()
                print(f"\nYou drew: {result['card']}")
                print(f"Hand value: {result['hand_value']}")
                print()
                
                if result['busted']:
                    print("BUST! You went over 21!")
                    break
            elif action == 's':
                break
            else:
                print("Invalid input! Please enter 'h' for Hit or 's' for Stand.")
                continue
        
        # Dealer's turn
        print("\nDealer's turn...")
        input("Press Enter to continue...")
        
        dealer_result = game.dealer_play()
        print("\nDealer's hand:")
        for card in game.get_dealer_hand():
            print(f"  - {card}")
        print(f"Hand value: {dealer_result['hand_value']}")
        print()
        
        if dealer_result['busted']:
            print("Dealer BUST!")
        
        # Determine winner
        winner = game.determine_winner()
        print()
        if winner == 'player':
            print("You WIN!")
        elif winner == 'dealer':
            print("Dealer wins!")
        else:
            print("It's a TIE!")
        
        # Show stats
        stats = game.get_stats()
        print()
        print(f"Games: {stats['games_played']} | Wins: {stats['wins']} | Losses: {stats['losses']} | Ties: {stats['ties']}")
        
        print()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("\nThanks for playing Blackjack!")


def main():
    """Main menu for the card games."""
    while True:
        clear_screen()
        print_header()
        print("Select a game to play:")
        print()
        print("  1. Higher or Lower")
        print("  2. Blackjack")
        print("  3. Exit")
        print()
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            play_higher_lower()
        elif choice == '2':
            play_blackjack()
        elif choice == '3':
            print("\nThanks for playing! Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
