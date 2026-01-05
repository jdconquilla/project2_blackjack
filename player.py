from hand import Hand
class Player():
    def __init__(self, name, balance, bet=0):
        self.name = name
        self.balance = balance
        self.hand = Hand()
        self.bet = bet
        
    def bal(self):
        print(f"Remaining balance: ${self.balance}")

    def place_bet(self, amount):
        if amount <= 0:
            print("Bet amount must be greater than zero.")  
            return False
        if amount > self.balance:
            print("Insufficient balance to place that bet.")
            return False
        else:
            self.balance -= amount
            print(f"Bet of ${amount} placed.")
            self.bet = amount
            return True
        

    def hit(self, deck):
        card = deck.deal()
        self.hand.add_card(card)
        print(f"{self.name} hits and receives a card.")
        self.hand.display_hand()

    def stand(self):
        pass

