# Cree una clase abstracta de Shape que:
# Tenga los métodos abstractos de calculate_perimeter y calculate_area.
# Ahora cree las siguientes clases que hereden de Shape e implementen esos métodos: Circle, Square y Rectangle.
# Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

from abc import ABC, abstractmethod
PI = 3.14

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
        print(f"I am a circle with a radius of {radius}")

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius < 0:
            print("Radius cannot be negative")
            return
        self.__radius = radius

    def calculate_perimeter(self):
        return (2 * (PI * self.__radius))

    def calculate_area(self):
        return (PI * (self.__radius ** 2))

class Square(Shape):
    def __init__(self, side):
        self.__side = side
        print(f"I am a square with a side of {side}")

    def get_side(self):
        return self.__side

    def set_side(self, side):
        if side < 0:
            print("Side cannot be negative")
            return
        self.__side = side

    def calculate_perimeter(self):
        return (4 * self.__side)

    def calculate_area(self):
        return (self.__side ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        print(f"I am a rectangle with a height of {height} and a width of {width}")

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width < 0:
            print("Width cannot be negative")
            return
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height < 0:
            print("Height cannot be negative")
            return
        self.__height = height

    def calculate_perimeter(self):
        return (2 * (self.__width + self.__height))

    def calculate_area(self):
        return (self.__width * self.__height)

def main():
    circle = Circle(5)
    print(f"Area: {circle.calculate_area()}")
    print(f"Perimeter: {circle.calculate_perimeter()}")
    circle.set_radius(10)
    print(f"New radius: {circle.get_radius()}")
    print(f"New Area: {circle.calculate_area()}")
    print(f"New Perimeter: {circle.calculate_perimeter()}\n")

    square = Square(4)
    print(f"Area: {square.calculate_area()}")
    print(f"Perimeter: {square.calculate_perimeter()}")
    square.set_side(8)
    print(f"New side: {square.get_side()}")
    print(f"New Area: {square.calculate_area()}")
    print(f"New Perimeter: {square.calculate_perimeter()}\n")

    rectangle = Rectangle(10, 5)
    print(f"Area: {rectangle.calculate_area()}")
    print(f"Perimeter: {rectangle.calculate_perimeter()}")
    rectangle.set_height(2)
    print(f"New height: {rectangle.get_height()}")
    rectangle.set_width(3)
    print(f"New width: {rectangle.get_width()}")
    print(f"New Area: {rectangle.calculate_area()}")
    print(f"New Perimeter: {rectangle.calculate_perimeter()}")

if __name__ == "__main__":
    main()