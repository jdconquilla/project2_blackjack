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

- Card - rank, suit, value attributes of each card

- Deck - creates a 52-card deck, automatically shuffles and deal cards

- Hand - which handles card storage per player. value calculation, bust and win detection, and cards display

- Player - checks the place bet and player turn

- Dealer - inherits from Player and has the blackjack logic rules

- BlackjackGame - control game glow and logic

### Recommendations

- Add the Blackjack payout of 3:2

- Add the other player options of split and double-down

- Improve UI with colors or GUI

- Add automated testing

#### Author

Developed by: 

Jossh Walter Conquilla

BS Computer Engineering - 1st Year



