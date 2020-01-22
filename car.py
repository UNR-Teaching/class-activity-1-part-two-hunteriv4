from engine import Engine
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, nickName, owner):
        super().__init__(color, nickName, owner)
        self.engine = Engine()
        self.throttle = 0
    
    def start(self):
        self.engine.start()
    
    def stop(self):
        self.engine.stop()
    
    def faster(self, amount):
        if self.started:
            self.throttle += pressure
        else:
            print("You might want to turn the car on...")
    
    def slower(self, amount):
        self.throttle -= amount
        if self.throttle < 0:
            self.throttle = 0


def main():
    print("Creating car object...")
    car = Car("Yellow", "Pinto", "Wayne")
    print(f"Car's color is {car.color}")
    print(f"Car's nickname is {car.nickName}")
    print(f"Car's owner is {car.owner}")
    print(f"Car's direction is {car.direction} degrees")
    print(f"Car's throttle is {car.throttle}")

main()