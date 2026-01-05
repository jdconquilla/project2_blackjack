# project2_blackjack

## Blackjack Game ♠

### Project Overview

This project is a console-based Blackjack game written in Python using object-oriented programming principles. It is written to demonstrate the use of classes, inheritance, and game logic. 

The game allows 1-4 players to play Blackjack against a computerized dealer, place bets, draw cards, and win or lose based on standard Blackjack rule with the exception of the split and double down rules.

### Features

- Object-oriented design using Python classes

- Supports multiple players (1-4) by setting up their profile

- Functional betting system without limits

- Automatic dealer behavior

- Detection of busts, wins, losses, and ties

- Eliminates players who gets bankrupt

- A clean game loop that applies Blackjack logic

### Project Structure

- main.py - handles the main game loop and the control logic

- card.py - has the Card class 

- deck.py - has the Deck class 

- hand.py - has the Hand class 

- player.py - has the Player class 

- dealer.py - has the Dealer class 

- README.md - has the project documentation

### Game Rules

1. The goal is to have a hand value as close to 21 as possible without exceeding it.

2. Number cards are worth their face value, face cards are worth 10, and Aces can be worth 1 or 11.

3. Players can choose to 'Hit' to receive another card or 'Stand' to end their turn.

4. If a player's hand exceeds 21, they bust and lose the round.

5. The dealer must hit until their hand value is at least 17.

6. If the dealer busts, all remaining players win.

7. If neither busts, the higher hand value wins. Ties result in a push.

### Object-Oriented Design 

#### Class Responsibilities Summary

#### Main Classes

##### Card class

represents a single playing card with a rank and suit

###### Parameters:

- name (str): Card rank (2-10, J, Q, K, A)

- suit (str): Card suit (S, D, H, C)

###### Methods:

- display(self)

    Displays the card in a readable format using suit symbols.

- value(self)

    Returns the Blackjack value of the card as an integer:

> Face cards = 10;
> Ace = 1 or 11;
> Number cards = face value

##### Deck class 

Creates a 52-card deck, automatically shuffles and deal cards.
###### Methods:
- shuffle(self)

    Shuffle the deck randomly

- deal(self)

    Removes and returns the top card from the deck.
  
##### Hand 

Handles card storage per player. value calculation, bust and win detection, and cards display

###### Parameters:

- card (Card): Card to add to the hand
  
###### Methods:

- display_hand(self)

    Displays all cards currently in the hand.

- hand_value(self)
  
    Calculates and returns the total Blackjack value of the hand, adjusting Aces as needed.

- detect_blackjack(self)
  
    Returns True if the hand is a Blackjack (total of 21).

- detect_bust(self)

    Returns True if the hand value exceeds 21.
  
##### Player class 

Represents a Blackjack player: checks the place bet and player turn
  
###### Paramaters: 

- name (str): Player's name

- balance (int): Starting balance

- bet (int): Current bet amount

###### Methods:

- place_bet(self, amount)

    Attempts to a place a bet. Returns True if valid, False if not.

- hit(self, deck)
  
    Deals one card to the player's hand

- stand(self)

    Ends the player's turn.

- bal(self)
    Displays the player's current balance.
  
##### Dealer class 

Represents the Blackjack dealer: inherits from Player and has the blackjack logic rules

###### Methods:

- play_turn(self, deck)
  
    Automatically plays the dealer's turn by hitting until hand value is at least 17.

- reveal_initial_card(self)
  
    Displays only the dealer's first card.

- reveal_hand(self)

    Displays all cards in the dealer's hand

##### BlackjackGame class

Controls game glow and logic

###### Methods:

- start(self)

    Starts the game loop and manages rounds.

- setup_players(self)

    Prompts the user to create player profiles.

- place_bets(self)

    Prompts each player to place a valid bet.
  
- initial_deal(self)

    Deals two cards to each player and the dealer.

- reset_hands(self)

    Clears all hands and resets player bets.

- resolve_round(self)

    Compares hands and updates player balances based on outcomes.

- eliminate_broke_players(self)

    Removes players who have run out of balance.

- ask_continue(self)

    Asks remaining players if they want to continue playing.

- leader_board(self)

    Displays current balances of all players.

- reveal_rules(self)

    Prints the Blackjack rules to the console.
  
### Recommendations

- Add the Blackjack payout of 3:2

- Add the other player options of split and double-down

- Improve UI with colors or GUI

- Add automated testing

#### Author

Developed by: 

Jossh Walter Conquilla

BS Computer Engineering - 1st Year



