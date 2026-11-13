# Cree una clase de Bus con:
# Un atributo de max_passengers.
# Un método para agregar pasajeros uno por uno (que acepte como parámetro una instancia de la clase Person vista en la lección). 
# Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.
# Un método para bajar pasajeros uno por uno (en cualquier orden).
class Person():
	def __init__(self, name):
		print(f"Ha nacido una persona llamada {name}!")
		self.name = name
		self.age = 0

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"We have added the passenger {person.name}")
        else:
            print(f"The Bus is full!!")

    def drop_passenger(self):
            if len(self.passengers) > 0:
                passenger = self.passengers.pop()
                print(f"We have dropped the passenger {passenger.name}")
            else:
                print(f"There are no passengers on the Bus!")

def main():
    person1 = Person("John")
    person2 = Person("Mary")
    person3 = Person("Peter")
    bus = Bus(2)

    bus.add_passenger(person1)
    bus.add_passenger(person2)
    bus.add_passenger(person3)  

    bus.drop_passenger()
    bus.add_passenger(person3) 

if __name__ == "__main__":
    main()