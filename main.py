from player import Player
from deck import Deck
from dealer import Dealer
from hand import Hand

class BlackjackGame:
    game_running = True

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.dealer = Dealer()

    def start(self):  
        print("Welcome! Let's play Blackjack!")
        print("------------------------------")
        self.reveal_rules()
        print("Setting up players...")
        self.setup_players()
        self.leader_board()
        while self.game_running:
            self.reset_hands()
            self.deck = Deck()
            self.deck.shuffle()
            print(f"Cards left in deck: {len(self.deck.cards)}")
            self.place_bets()
            self.initial_deal()
            self.dealer.reveal_initial_card()
            for player in self.players:
                print(f"{player.name}'s turn:")  
                player.hand.display_hand()
                while True: 
                    action = input(f"{player.name}, do you want to Hit (H) or Stand (S)? ").upper() 
                    if action == 'H':
                        player.hit(self.deck)
                        if player.hand.detect_bust():
                            print(f"{player.name} busts!")
                            break
                    elif action == 'S':
                        print(f"{player.name} stands with a hand value of {player.hand.hand_value()}.")
                        break
                    else:
                        print("Invalid input. Please enter H to Hit or S to Stand.")
            print("Dealer's turn:")
            if any(not player.hand.detect_bust() for player in self.players):
                self.dealer.reveal_hand()
                self.dealer.play_turn(self.deck)
            else:
                print("All players have busted. Dealer wins by default.")
            self.resolve_round()
            self.leader_board()
            self.eliminate_broke_players()
            self.ask_continue()
            
                
        
    def initial_deal(self):
        for player in self.players:
            player.hand.add_card(self.deck.deal())
            player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())

    def setup_players(self):
        self.players = []
        num_players = int(input("Enter number of players (1-4): "))
        for i in range(num_players):
            name = input(f"Enter name for Player {i+1}: ")
            balance = int(input(f"Enter starting balance for {name}: "))
            player = Player(name, balance)
            self.players.append(player)


    def place_bets(self):
        for player in self.players:
            while True:
                try:
                    bet = int(input(f"{player.name}, enter your bet amount: "))
                    if player.place_bet(bet):
                        break
                except ValueError:
                    print("Invalid input. Please enter numeric values for bets.")


    def leader_board(self):
        print("Leaderboard:")
        for player in self.players:
            print(f"- {player.name}: ${player.balance}")


    def reset_hands(self):
        for player in self.players:
            player.hand = Hand()
            player.bet = 0
        self.dealer.hand = Hand()


    def resolve_round(self):
        dealer_value = self.dealer.hand.hand_value()
        for player in self.players:
            player_value = player.hand.hand_value()
            if player.hand.detect_bust():
                print(f"{player.name} busts and loses their bet of ${player.bet}.")
            elif self.dealer.hand.detect_bust() or player_value > dealer_value:
                winnings = player.bet * 2
                player.balance += winnings
                print(f"{player.name} wins and now has a balance of ${player.balance}.")
            elif player_value == dealer_value:
                player.balance += player.bet
                print(f"{player.name} pushes and gets back their bet of ${player.bet}.")
            else:
                print(f"{player.name} loses their bet of ${player.bet}.")
 

    def eliminate_broke_players(self):
        eliminated = [player for player in self.players if player.balance <= 0]
        for player in eliminated:
            print(f"{player.name} has run out of balance and is eliminated from the game.")
        self.players = [player for player in self.players if player.balance > 0]
        if not self.players:
            print("All players have run out of balance. Game over!")
            self.game_running = False


    def ask_continue(self):
        remaining_players = []
        for player in self.players:
            while True:
                choice = input(f"{player.name}, do you want to continue playing? (Y/N): ").upper()
                if choice == 'Y':
                    remaining_players.append(player)
                    break
                elif choice == 'N':
                    print(f"{player.name} has left the game with a balance of ${player.balance}.")
                    break
                else:
                    print("Invalid input. Please enter Y to continue or N to quit.")
        self.players = remaining_players

        if not self.players:
            print("No players left. Ending game.")
            self.game_running = False
            return
        

    def reveal_rules(self):
        print("Blackjack Rules:")
        print("1. The goal is to have a hand value as close to 21 as possible without exceeding it.")
        print("2. Number cards are worth their face value, face cards are worth 10, and Aces can be worth 1 or 11.")
        print("3. Players can choose to 'Hit' to receive another card or 'Stand' to end their turn.")
        print("4. If a player's hand exceeds 21, they bust and lose the round.")
        print("5. The dealer must hit until their hand value is at least 17.")
        print("6. If the dealer busts, all remaining players win.")
        print("7. If neither busts, the higher hand value wins. Ties result in a push.")
        print("------------------------------")

if __name__ == "__main__":
    game = BlackjackGame([])
    game.start()


