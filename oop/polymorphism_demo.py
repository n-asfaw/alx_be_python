import math

class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width  # Area formula for rectangle

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)  # Area formula for circle
