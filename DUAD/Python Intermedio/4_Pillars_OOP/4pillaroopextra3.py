
# Cree una clase base Vehicle con los atributos:
# - _brand
# - _year
#
# Agregue un método get_info() que devuelva una descripción del vehículo.
#
# Luego cree dos clases hijas:
# - Car
# - Motorcycle
#
# Cada una debe agregar su propio atributo (doors o type)
# y sobrescribir el método get_info() para incluir esta información adicional.
#
# Ejemplo:
# Entrada
# vehicle1 = Car("Toyota", 2020, 4)
# vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")
# Salida
# print(vehicle1.get_info()) # Toyota (2020) - 4 puertas
# print(vehicle2.get_info()) # Yamaha (2022) - Tipo: Deportiva

class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year

    def get_info(self):
        return f"{self._brand} ({self._year})"

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.__doors = doors

    def get_doors(self):
        return self.__doors

    def set_doors(self, doors):
        self.__doors = doors

    def get_info(self):
        return f"{super().get_info()} - {self.__doors} puertas"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, motorcycle_type):
        super().__init__(brand, year)
        self.__type = motorcycle_type

    def get_type(self):
        return self.__type

    def set_type(self, motorcycle_type):
        self.__type = motorcycle_type

    def get_info(self):
        return f"{super().get_info()} - Tipo: {self.__type}"

def main():
    vehicle1 = Car("Toyota", 2020, 4)
    vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva")

    print(vehicle1.get_info())
    print(vehicle2.get_info())
    print()
    
    vehicle1.set_doors(2)
    print(vehicle1.get_info())
    vehicle2.set_year(2025)
    print(vehicle2.get_info())

if __name__ == "__main__":
    main()
