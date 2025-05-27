import os
class Ingredients:
    def __init__(self):
        self.bread = None
        self.cheese = None
        self.meat = None
        self.sauce = None
    def bread_flavor(self, option):
        if option == "1":
            self.bread = "Whole Wheat Bread"
        elif option == "2":
            self.bread = "Italian Bread"
        elif option == "3":
            self.bread = "Rye Bread"
        else:
            raise Exception("Please select a valid option")
    def cheese_flavor(self, option):
        if option == "1":
            self.cheese = "Swiss Cheese"
        elif option == "2":
            self.cheese = "Provolone Cheese"
        elif option == "3":
            self.cheese = "Pepperjack Cheese"
        else:
            raise Exception("Please select a valid option")
    def protein(self, option):
        if option == "1":
            self.meat = "Steak"
        elif option == "2":
            self.meat = "Chicken"
        elif option == "3":
            self.meat = "Turkey"
        else:
            raise Exception("Please select a valid option")
    def sauce_flavor(self, option):
        if option == "1":
            self.sauce = "Sour Cream"
        elif option == "2":
            self.sauce = "Salsa"
        elif option == "3":
            self.sauce = "Mayonaise"
        else:
            raise Exception("Please select a valid option")
class Menu(Ingredients):
    def __init__(self):
        super().__init__()
        self.IC = 0
        self.RS = 0
        self.WRT = 0
    def italian_chicken(self):
        self.bread_flavor("2")
        self.cheese_flavor("1")
        self.protein("2")
        self.sauce_flavor("1")
        self.IC += 1
    def rye_steak(self):
        self.bread_flavor("3")
        self.cheese_flavor("3")
        self.protein("1")
        self.sauce_flavor("3")
        self.RS += 1
    def whole_rare_turkey(self):
        self.bread_flavor("1")
        self.cheese_flavor("2")
        self.protein("3")
        self.sauce_flavor("2")
        self.WRT += 1
class Checkout(Menu):
    def __init__(self):
        super().__init__()
        self.order_name = None
        self.total = 0
        self.chicken_choice = 0
        self.steak_choice = 0
        self.turkey_choice = 0
    def cls(self):
        os.system('cls')
    def main_menu(self):
        while True:
            print("Welcome To My Sandwhich Shop")
            print("You may only order between 0 to 5 sandwhiches of each.")
            self.order_name = input("Please enter the order name: ")
            try:
                self.chicken_choice = int(input("How many italian chicken sandwhiches do you want: "))
                self.steak_choice = int(input("How many rye steak sandwhiches do you want: "))
                self.turkey_choice = int(input("How many whole rare turkey sandwhiches do you want: "))
                if 0 <= self.chicken_choice <= 5 and 0 <= self.steak_choice <= 5 and 0 <= self.turkey_choice <= 5:
                    break
                else:
                    print("All choices must be between 0 and 5.")
            except ValueError:
                print("Order failed, restarting...")
        self.cls()
        self.summary()
    def summary(self):
        for _ in range(self.chicken_choice):
            self.italian_chicken()
        for _ in range(self.steak_choice):
            self.rye_steak()
        for _ in range(self.turkey_choice):
            self.whole_rare_turkey()
        print(f"{self.order_name} ordered {self.IC} italian chickens, {self.RS} rye steaks, and {self.WRT} whole turkeys.")
def main():
    run = Checkout()
    run.main_menu()