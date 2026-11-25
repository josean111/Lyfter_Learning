# Cree una clase Rectangle que:
# Tenga atributos width y height
# Tenga un método get_area() que retorne el área
# Tenga un método get_perimeter() que retorne el perímetro
# Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado
# Ejemplo 1:
# Entrada:
# "Ingrese la altura: " 250
# "Ingrese el ancho: " 300
# Salida:
# print(rectangle.get_area()) #75000
# print(rectangle.get_perimeter()) #1100
# Ejemplo 2:
# Entrada
# "Ingrese la altura: " -250
# "Ingrese el ancho: " 300
# Salida
# "Existe un valor negativo, los valores deben ser positivos"

# Cree una clase de Circle con:
# Un atributo de radius (radio).
# Un método de get_area que retorne su área.
class Rectangle:

    def __init__(self):
        self.validate_input

    def validate_input(self):
        try:
            print("Creado un rectangulo nuevo!")
            self.height = float(input("Ingrese la altura: "))
            self.width = float(input("Ingrese el ancho: "))

            if self.width < 0 or self.height < 0:
                raise ValueError("Existe un valor negativo, los valores deben ser positivos")

        except ValueError as error:
            print(error)
            return False
        return True

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

def main():
    rectangle = Rectangle()

    if rectangle.validate_input():
        print(f"El area del rectangulo es {rectangle.get_area()}")
        print(f"El perimetro del rectangulo es {rectangle.get_perimeter()}")

if __name__ == "__main__":
    main()