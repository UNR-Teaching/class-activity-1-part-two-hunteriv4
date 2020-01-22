from abc import ABC, abstractmethod
from horn import Horn
from light import Light
from wheel import Wheel

class Vehicle(ABC):
    def __init__(self, color=None, nickName=None, owner=None):
        self.wheels = []
        self.light = Light()
        self.color = color
        self.nickName = nickName
        self.owner = owner
        self.direction = 0

    def add_wheels(self, number):
        for count in range(number):
            self.wheels.append(Wheel())

    def remove_wheels(self, number):
        for count in range(number):
            if self.wheels:
                self.wheels.pop()

    def turn(self, turn_degrees=0):
        if not self.on_ground:
            self.direction += turn_degrees
            if self.direction >= 360:
                self.direction -= 360
            elif self.direction < 0:
                self.direction += 360
    
    @abstractmethod
    def faster(self, amount):
        pass

    @abstractmethod
    def slower(self, amount):
        pass