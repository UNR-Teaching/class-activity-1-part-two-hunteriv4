from vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, color, nickName, owner):
        super().__init__(color, nickName, owner)
        self.rpm = 0
        self.kickstand_down = True
        self.on_ground = False

    def kickstand(self):
        self.kickstand_down = not self.kickstand_down

    def pick_up(self):
        self.on_ground = False
    
    def faster(self, amount):
        if self.kickstand_down and amount > 0:
            print("You fall over!")
            self.on_ground = True
        else:
            self.rpm += amount

    def slower(self, amount):
        if self.rpm <= 0:
            print("You are stopped...")
        else:
            self.rpm -= amount

def main():
    print("Creating bicycle...")
    bike = Bicycle("red", "BMX", "Garth")
    print(f"Color is {bike.color}")
    print(f"Nickname is {bike.nickName}")
    print(f"Owner is {bike.owner}")

main()