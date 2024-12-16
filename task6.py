class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"the area of the circle is {self.radius * self.radius * 3.14}")


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"the area of the square is {self.side * self.side}")

square1 = Square(3)
square1.area()
circle1 = Circle(3)
circle1.area()