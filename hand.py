from card import Card

class Hand():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        
    def display_hand(self):
        for card in self.cards:
            card.display()

    def hand_value(self):
        total = 0
        aces = 0
        for card in self.cards:
            val = card.value()
            total += val
            if card.name == "A":
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total
    
    def detect_blackjack(self):
        return len(self.cards) == 2 and self.hand_value() == 21
    
    def detect_bust(self):
        return self.hand_value() > 21
