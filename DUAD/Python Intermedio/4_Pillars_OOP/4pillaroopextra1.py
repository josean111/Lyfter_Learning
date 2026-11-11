# Cree una clase Employee con los siguientes requisitos:
# Atributos privados: _name, _salary
# Use @property y @<atributo>.setter para:
# - Mostrar el nombre y el salario.
# - Validar que el salario nunca sea negativo.
# Cree un método promote que aumente el salario un porcentaje definido.
#
# Ejemplo:
# Entrada:
# employee = Employee("Ana", 1000)
# employee.promote(0.1)  # +10%
# Salida:
# print(employee.salary)  # 1100
class Employee:
    def __init__(self, name, salary):
        #v1 self._name = name
        self.name = name  #v2 para evitar que el constructor se brinque el setter
        #v1 self._salary = salary
        self.salary = salary  #v2 para evitar que el constructor se brinque la validacion del setter al asignar salario

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = salary

    def promote(self, percentage):
        if percentage < 0:
            raise ValueError("Promotion percentage cannot be negative")
        self.salary += self.salary * percentage

def main():
    # Este ejercicio me gusto por lo del properties y setter entonces quise validar todos los escenarios para entenderlos uno a uno
    try:
        employee = Employee("Ana", 1000)
        print(f"Employee: {employee.name}")
        print(f"Salary: {employee.salary}")

        employee.promote(0.1)
        print(f"New salary: {employee.salary}")

    except ValueError as error:
        print(f"Error: {error}")

    try:
        employee2 = Employee("Laura", 2000)
        print(f"\nEmployee: {employee2.name}")
        print(f"Salary: {employee2.salary}")

        employee2.salary = -1500
        print(f"Updated salary: {employee2.salary}")

    except ValueError as error:
        print(f"Error: {error}")

    try:
        employee3 = Employee("Pedro", 3000)
        print(f"\nEmployee: {employee3.name}")
        print(f"Salary: {employee3.salary}")

        employee3.promote(-0.1)
        print(f"New salary: {employee3.salary}")

    except ValueError as error:
        print(f"Error: {error}")

    try:
        print("\nThis employee can't be created due to salary being incorrect")
        # este nunca se va a mostrar por el slario negativo que el constructor revisa con la validacion, por eso el cambio de la v1
        employee4 = Employee("Carlos", -500)
        print(f"\nEmployee: {employee4.name}")
        print(f"Salary: {employee4.salary}")

    except ValueError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()