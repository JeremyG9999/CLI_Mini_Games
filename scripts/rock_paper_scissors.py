from abc import ABC, abstractmethod
import os
import time
import random
class Strategy(ABC):
    @abstractmethod
    def game(self):
        pass
class Rock(Strategy):
    def game(self):
        return "Rock"
class Paper(Strategy):
    def game(self):
        return "Paper"
class Scissors(Strategy):
    def game(self):
        return "Scissors"
class Rock_paper_scissors:
    def __init__(self):
        self.AI_option = None #AI pick from list
        self.AI_decision = None #AI final choice
        self.choice = None #your decision
        self.list = ["0", "1", "2"]
    def artificial_intelligence(self):
        self.AI_option = random.choice(self.list)
        if self.AI_option == "0":
            self.AI_decision = Rock().game()
        elif self.AI_option == "1":
            self.AI_decision = Paper().game()
        elif self.AI_option == "2":
            self.AI_decision = Scissors().game()
        return self.AI_decision
    def play_game(self):
        while True:
            print("Select an Option: ")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Clear Terminal")
            print("5. End Game ")
            self.choice = input("Pick something to make: ")
            self.artificial_intelligence()
            if self.choice == "1":
                self.cls()
                print(f"You made {Rock().game()} and AI made {self.AI_decision}")
                if self.AI_option == "0":
                    print("It's a tie!")
                elif self.AI_option == "1":
                    print("AI WINS!")
                elif self.AI_option == "2":
                    print("You win!")
            elif self.choice == "2":
                self.cls()
                print(f"You made {Paper().game()} and AI made {self.AI_decision}")
                if self.AI_option == "0":
                    print("You win!")
                elif self.AI_option == "1":
                    print("It's a tie!")
                elif self.AI_option == "2":
                    print("AI WINS!")
            elif self.choice == "3":
                self.cls()
                print(f"You made {Scissors().game()} and AI made {self.AI_decision}")
                if self.AI_option == "0":
                    print("AI WINS!")
                elif self.AI_option == "1":
                    print("You win!")
                elif self.AI_option == "2":
                    print("It's a tie!")
            elif self.choice == "4":
                self.cls()
            elif self.choice == "5":
                break
            else:
                self.cls()
                print("Pick a valid option")
    def cls(self):
        os.system('cls')
        time.sleep(0.1)
def main():
    run = Rock_paper_scissors()
    run.play_game()