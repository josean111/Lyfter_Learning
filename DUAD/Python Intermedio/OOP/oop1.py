# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.
PI = 3.14

class Circle:
    radius = 0

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        PI * (self.radius * self.radius)

def main():
    circle_1 = Circle(5)
    print(f"The area of the circle is {circle_1.get_area()}")
    circle_2 = Circle(10)
    print(f"The area of the circle is {circle_2.get_area()}")

if __name__ == "__main__":
    main()