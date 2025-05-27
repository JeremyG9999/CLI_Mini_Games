import random
class Stack:  
    def __init__(self):
        self.dealer = []
        self.player_1 = []  
    def push(self):
        if len(self.dealer) > 0:
            dealer_card = self.dealer.pop(0)
            self.player_1.insert(0, dealer_card)
            print(f"\n{dealer_card} was added to the top of the player_1's deck from the dealer's deck.\n")
        else:
            print("\nAll of the dealer deck cards are gone!!!!\n")
    def pop(self):
        if len(self.player_1) > 0:
            player_1_card = self.player_1.pop(0)
            self.dealer.insert(0, player_1_card)
            print(f"\n{player_1_card} was added to the top of the dealer's deck from player_1's deck.\n")
        else:
            print("\nYou have no cards to give.\n")
    def is_empty(self):
        if len(self.dealer) == 0:
            print("\nThe dealer's deck is empty")
        else:
            print(f"\nDealer Deck: {self.dealer}")
        if len(self.player_1) == 0:
            print("\nPayer_1's deck is empty\n")
        else:
            print(f"\nPlayer_1: {self.player_1}\n")
    def deck(self):
        suits = ['d', 'c', 'h', 's']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']    
        self.dealer = []    
        for suit in suits:
            for rank in ranks:
                card = (rank, suit)
                self.dealer.append(card)
        random.shuffle(self.dealer)
        return self.dealer
    def shuffle_deck(self):
        self.deck()
        while True:
            print("Welcome to the Main Menu: ")
            print("1. Take a card from the top of the dealer deck and put it on the top of your deck")
            print("2. Return a card from the top of your deck and put it back on the top of the dealer's deck")
            print("3. Show dealer deck and player_1 deck")
            print("4. Exit")
            choice = input("Select a choice: ")
            if choice == "1":
                self.push()
            elif choice == "2":
                self.pop()
            elif choice == "3":
                self.is_empty()
            elif choice == "4":
                break
            else:
                print("Please enter a number between 1 and 4")
def main():
    run = Stack()
    run.shuffle_deck()