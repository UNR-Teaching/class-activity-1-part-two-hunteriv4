from engine import Engine
from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color, nickName, owner):
        super().__init__(color, nickName, owner)
        self.engine = Engine()
        self.started = False
        self.throttle = 0
        self.direction = 0

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()

    def throttle(self, pressure=0):
        if self.started:
            self.throttle += pressure
        else:
            print("You might want to turn the car on...")

    def turn(self, turn_degrees=0):
        if self.started:
            self.direction += turn_degrees
            if self.direction >= 360:
                self.direction -= 360
            elif self.direction < 0:
                self.direction += 360


def main():
    print("Creating car object...")
    car = Car("Yellow", "Pinto", "Wayne")
    print(f"Car's color is {car.color}")
    print(f"Car's nickname is {car.nickName}")
    print(f"Car's owner is {car.owner}")
    print(f"Car's direction is {car.direction} degrees")
    print(f"Car's throttle is {car.throttle}")


main()