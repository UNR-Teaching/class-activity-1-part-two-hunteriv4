class Car:
    def __init__(self, color=None, nickName=None, owner=None):
        self.color = color
        self.nickName = nickName
        self.owner = owner
        self.started = False
        self.throttle = 0
        self.direction = 0

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

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