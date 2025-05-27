import random
class dice_roll:
    def __init__(self):
        self.choice = None            
    def roll_dice(self):
        roll_dice = random.choice([1, 2, 3, 4, 5, 6])
        print(f"\nYou rolled a {roll_dice}\n")
    def custom_size(self):
        while True:
            dice_amount = int(input("\nHow many sides to the dice: "))
            if dice_amount <= 1 or dice_amount >= 20:
                print("\nDice can only be between 2-19")
                continue
            else:
                roll_custom_dice = random.randint(1, dice_amount)
            print(f"\nYou rolled a {roll_custom_dice} with a {dice_amount} sided dice\n")
            break
    def main_menu(self):
        while True:
            print("Welcome to the main menu!")
            print("1. Roll 6 sided dice")
            print("2. Enter a custom size dice")
            print("3. Exit")
            self.choice = input("Select a choice: ")
            if self.choice == "1":
                self.roll_dice()
            elif self.choice == "2":
                self.custom_size()
            elif self.choice == "3":
                print("Goodbye!")
                break
            else:
                print("Please enter a valid option 1-3")
def main():
    run = dice_roll()
    run.main_menu()