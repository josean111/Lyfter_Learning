# Cree una clase base Animal y dos clases hijas Dog y Cat:
# Animal debe tener nombre y método speak() que retorne "Hace un sonido"
# Dog debe sobrescribir speak() para decir "Guau"
# Cat debe sobrescribir speak() para decir "Miau"
# Ejemplo:
# Entrada:
# dog = Dog("Firulais")
# Salida
# print(dog.speak())  # Guau
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Se ha creado un nuevo animal {self.name}")

    def speak(self):
        return f"{self.name} Hace un sonido"

class Dog(Animal):
    def speak(self):
        return f"Guau hace mi perro {self.name}"

class Cat(Animal):
    def speak(self):
        return f"Miau es como hace mi gato {self.name}"

def main():
    animal = Animal("Soy un Animal :)")
    dog = Dog("Firulais")
    cat = Cat("Michi")

    print(animal.speak())
    print(dog.speak())
    print(cat.speak())

if __name__ == "__main__":
    main()
