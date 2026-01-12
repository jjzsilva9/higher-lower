# **Higher/Lower** and **Blackjack**

## Quick Start

```bash
python main.py
```

## Games

**Higher/Lower** - Guess if next card is higher or lower  
**Blackjack** - Beat the dealer, get closest to 21 without busting


## Project Structure

```
├── main.py                  # CLI interface
├── card.py                  # Card class
├── deck.py                  # Deck class
├── higher_lower_game.py     # Higher/Lower game logic
└── blackjack_game.py        # Blackjack game logic
```

## Implementation Decisions

I chose to implement separate classes for both the cards and decks.

On the card level, each object has several tasks it needs to perform, such as tracking its own value, comparing to other cards, and displaying itself, which forms a reasonable amount of functionality that justifies its own class.
On the deck level, we need to manage 52 (or 54 with Jokers) cards, including initialisation, shuffling, and drawing. Implementing this in its own class enables the simple reuse of the functionality across the 2 games.

## Further Work

Ideas for improvement here definitely include using a GUI to display the cards; this would make the user experience much cleaner (could use buttons instead of the clunky CLI).
It would also be nice to have the best scores persist across sessions by storing a save game.
