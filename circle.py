import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius * self.radius * math.pi, 2)

    def perimeter(self):
        return round(self.radius * 2 * math.pi, 2)


circle1 = Circle(radius=1)
print(circle1.area())
print(circle1.perimeter())

circle3 = Circle(radius=3)
print(circle3.area())
print(circle3.perimeter())
