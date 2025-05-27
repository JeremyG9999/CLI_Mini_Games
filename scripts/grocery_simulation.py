import random 
class grocery_simulation():
    def __init__(self):
        self.count = 1
        self.express = []
        self.normal = []
        self.time = int(input("Enter a number: "))
    def simulation(self):
        for arrival in range (1, self.time + 1):
            if random.randint(1, 5)==1:
                processing = random.randint(3, 8)
                self.normal.append([self.count, arrival, processing])
                data = self.normal.pop()
                self.count += 1
                print(f"Customer {data[0]} arrived in the normal lane at {data[1]} minutes and left at {data[1] + data[2]} minutes.")
            if random.randint(1, 5)==1:
                processing = random.randint(1, 5)
                self.express.append([self.count, arrival, processing])
                data = self.express.pop()
                self.count += 1
                print(f"Customer {data[0]} arrived in the express lane at {data[1]} minutes and left at {data[1] + data[2]} minutes.")          
def main():
    run = grocery_simulation()
    run.simulation()