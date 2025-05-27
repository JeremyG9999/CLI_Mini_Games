import os
import time

from scripts.card_stack import Stack
from scripts.sandwhich_factory import Sandwhich
from scripts.grocery_simulation import grocery_simulation
from scripts.rock_paper_scissors import Rock_paper_scissors
from scripts.roll_dice import dice_roll
from scripts.Animal_Game.animal_game import AnimalGame
from scripts.Singleton_Game.singleton_shapes_DB import Singleton_Shape_DB
from scripts.Singleton_Game.database import setup_database
from scripts.singleton_shapes import Singleton_Shape
from scripts.sandwhich_order import Checkout
from scripts.car_shop import augmented_reality

class Menu:
    def main_menu(self):
        while True:
            print("\nSelect a program:")
            print("1. Stack Game")
            print("2. Sandwhich Factory")
            print("3. Grocery Simulation")
            print("4. Rock Paper Scissors")
            print("5. Roll Dice")
            print("6. Animal Game")
            print("7. Singleton Shapes Game DB")
            print("8. Singleton Shapes Game")
            print("9. Sandwhich Order")
            print("10. Car Shop")
            print("11. Clear Terminal")
            print("12. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.cls()
                Stack().shuffle_deck()
            elif choice == "2":
                self.cls()
                Sandwhich().main_menu()
            elif choice == "3":
                self.cls()
                grocery_simulation().simulation()
            elif choice == "4":
                self.cls()
                Rock_paper_scissors().play_game()
            elif choice == "5":
                self.cls()
                dice_roll().main_menu()
            elif choice == "6":
                self.cls()
                AnimalGame().play_game()
            elif choice == "7":
                setup_database()
                self.cls()
                Singleton_Shape_DB().main_menu()
            elif choice == "8":
                self.cls()
                Singleton_Shape().main_menu()
            elif choice == "9":
                self.cls()
                Checkout().main_menu()
            elif choice == "10":
                self.cls()
                augmented_reality().main_menu()
            elif choice == "11":
                self.cls()
            elif choice == "12":
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 12.")

    def cls(self):
        time.sleep(0.2)
        os.system("cls" if os.name == "nt" else "clear")

if __name__ == "__main__":
    Menu().main_menu()