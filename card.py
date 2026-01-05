class Card():
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit

    def display(self):
        symbols = {"S":"♠", "D":"♦", "H":"♥", "C":"♣"}
        print(f"{self.name}{symbols[self.suit]}")

    def value(self):
        if self.name in ["J", "Q", "K"]:
            return 10
        elif self.name == "A":
            return 11
        else:
            return int(self.name)