import random
class augmented_reality:
    def __init__(self):
        self.choice = None
        self.car = None
    def main_menu(self):
        while True:
            print("Welcome to the main menu!")
            print("1. Identify Car")
            print("2. Manual Input")
            print("3. Exit")
            self.choice = input("Select a choice: ")
            if self.choice == "1":
                self.identify_car()
            elif self.choice == "2":
                self.manual_input()
            elif self.choice == "3":
                print("Goodbye!")
                break
            else:
                print("Please enter a valid option 1-3")
    def identify_car(self):
        make_list = ["toyota", "ford", "chevy"]
        model_lists = {
            "toyota": ["camry", "corolla", "prius"],
            "ford": ["escape", "focus", "fusion"],
            "chevy": ["cruze", "malibu", "equinox"]
        }
        years = ["2021", "2022", "2023", "2024"]        
        random_make = random.choice(make_list)
        random_model = random.choice(model_lists[random_make])
        random_year = random.choice(years)
        self.car = [random_make, random_model, random_year]
        self.repair_menu()
    def manual_input(self):
        while True:
            make = input("Enter the make being toyota, ford, chevy: ").lower()
            if make not in ["toyota", "ford", "chevy"]:
                print("\nInvalid choice, we only operate on toyota, chevy, or ford")
                continue
            model = input("Enter the model: ").lower()
            if make == "toyota" and model not in ["camry", "corolla", "prius"]:
                print("\nInvalid toyota model, we only do camry, corolla, or prius")
                continue
            elif make == "ford" and model not in ["escape", "focus", "fusion"]:
                print("\nInvalid ford model, we only do escape, focus, or fusion")
                continue
            elif make == "chevy" and model not in ["cruze", "malibu", "equinox"]:
                print("\nInvalid chevy model, we only do cruze, malibu, or equinox")
                continue
            year = input("Enter the year: ")
            if year not in ["2021", "2022", "2023", "2024"]:
                print("\nInvalid year we only do 2021, 2022, 2023, or 2024")
                continue
            self.car = [make, model, year]
            self.repair_menu()
            break
    def repair_menu(self):            
        while True:
            print(f"\nThe car identified is a {self.car[0]}, {self.car[1]} made in {self.car[2]}.\n")
            print("Please select an option from the repair menu: ")
            print("1. Run Car Diagnostic: ")
            print("2. Return to main menu: ")
            print("3. Reenter car info manually: ")
            self.choice = input("\nEnter an option: ")
            if self.choice == "1":
                self.car_diagnostic()
                break
            elif self.choice == "2":
                break
            elif self.choice == "3":
                self.manual_input()
                break
            else:
                print("Please enter a valid option 1-3! \n")
            continue
    def car_diagnostic(self):
        diagnostics = {
            "Oil change": random.choice(["Yes", "No"]),
            "Tire pressure": random.randint(20, 40),
            "Battery health": random.choice(["Good", "Fair", "Poor", "Critical"]),
            "Brake fluid": random.choice(["Full", "Fair", "Low"]),
            "Transmission fluid": random.choice(["Full", "Fair", "Low"]),
        }
        print("Car Diagnostic Report: \n")
        for key, value in diagnostics.items():
            print(f"{key}: {value}")
        print()
        if diagnostics["Oil change"] == "Yes":
            print("\nYou will need an Oil Change.")
        if diagnostics["Tire pressure"] < 30:
            print("You will need air in your tires.")
        if diagnostics["Battery health"] in ["Poor", "Critical"]:
            print("You will need a new battery")
        if diagnostics["Brake fluid"] == "Low":
            print("You will need a refill on brake fluid")
        if diagnostics["Transmission fluid"] == "Low":
            print("You will need a refill on transmission fluid.")
        print()
def main():
    run = augmented_reality()
    run.main_menu()