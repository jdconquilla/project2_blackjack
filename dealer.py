from player import Player
from hand import Hand

class Dealer(Player):
    def __init__(self):
        super().__init__(name="Dealer", balance=0)
    
    def play_turn(self, deck):
        while self.hand.hand_value() < 17:
            card = deck.deal()
            self.hand.add_card(card)
            print("Dealer hits:")
            self.hand.display_hand()
        if self.hand.detect_bust():
            print("Dealer busts!")
        else:
            print("Dealer stands.")

    def reveal_initial_card(self):
        if self.hand.cards:
            print("Dealer's visible card:")
            self.hand.cards[0].display()

    def reveal_hand(self):
        print("Dealer reveals hand:")
        self.hand.display_hand()