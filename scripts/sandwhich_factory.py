from abc import ABC, abstractmethod
import os
import time
class Sandwhich_Factory(ABC):
    @abstractmethod
    def factory(self):
        pass
class Ham_Creator(Sandwhich_Factory):
    def factory(self):
        return Ham_Product()
    def prices(self):
        return Ham_Price()
class Turkey_Creator(Sandwhich_Factory):
    def factory(self):
        return Turkey_Product()
class Chicken_Creator(Sandwhich_Factory):
    def factory(self):
        return Chicken_Product()
class Sandwhich_Product(ABC):
    @abstractmethod
    def interface(self):
        pass
class Ham_Product(Sandwhich_Product):
    def interface(self):
        print("\nYou made a ham sandwhich\n")
class Turkey_Product(Sandwhich_Product):
    def interface(self):
        print("\nYou made a turkey sandwhich\n")
class Chicken_Product(Sandwhich_Product):
    def interface(self):
        print("\nYou made a chicken sandwhich\n")
class Sandwhich_Price(ABC):
    @abstractmethod
    def price(self):
        pass
class Ham_Price(Sandwhich_Price):
    def price(self):
        print("The Ham Sandwhich costs $5")
class Sandwhich:
    def __init__(self):
        self.option = None
    def make_sandwhich(self):
        self.cls()
        while True:
            print("\nSelect a sandwhich:")
            print("1. Ham")
            print("2. Turkey")
            print("3. Chicken")
            print("4. Clear Space")
            print("5. Return to Main Menu")
            self.option = input("Select a menu option: ")
            if self.option == "1":
                self.cls()
                Ham_Creator().factory().interface()
                Ham_Creator().prices().price()
            elif self.option == "2":
                Turkey_Creator().factory().interface()
            elif self.option == "3":
                Chicken_Creator().factory().interface()
            elif self.option == "4":
                self.cls()
            elif self.option == "5":
                break
            else:
                print("Not a valid option: ")
    def cls(self):
        os.system('cls')
        time.sleep(0.1)
    def main_menu(self):
        while True:
            self.cls()
            print("\nSelect a choice:")
            print("1. Make Sandwhich")
            print("2. Exit")
            option = input("Select a menu option: ")
            if option == "1":
                self.make_sandwhich()
            elif option == "2":
                break
            else:
                print("Invalid input")
def main():
    run = Sandwhich()
    run.main_menu()