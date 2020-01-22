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
        pass


class Bicycle:
    def __init__(self, color=None, nickName=None, owner=None):
        self.color = color
        self.nickName = nickName
        self.owner = owner
        self.rpm = 0
        self.direction = 0
        self.kickstand_down = True
        self.on_ground = False

    def kickstand(self):
        self.kickstand_down = not self.kickstand_down
    
    def pedal(self, rpm):
        if self.kickstand_down and rpm > 0:
            print("You fall over!")
            self.on_ground = True
        else:
            self.rpm = rpm

    def pick_up(self):
        self.on_ground = False

    def turn(self, turn_degrees=0):
        if not self.on_ground:
            self.direction += turn_degrees
            if self.direction >= 360:
                self.direction -= 360
            elif self.direction < 0:
                self.direction += 360

    def main():
        pass