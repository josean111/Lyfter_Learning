
# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
# Una clase puede adoptar varios metodos y atributos de otras clases en uno solo, tipico un superheroe con muchos poderes.
# Los mixins permiten agregar funcionalidades independientes a diferentes clases sin tener que repetir codigo.
class Name:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class WalkerMixin:
    def walk(self):
        print("I am walking!")

class SwimmerMixin:
    def swim(self):
        print("I am swimming!")

class FlyerMixin:
    def fly(self):
        print("I am flying!")

class Human(Name, WalkerMixin):
    def __init__(self, name):
        super().__init__(name) # Reutilizo el constructor de Name para no repetir el atributo - DRY!
        print(f"I am a human named {name}")

class Fish(Name, SwimmerMixin):
    def __init__(self, name):
        super().__init__(name)
        print(f"I am a fish named {name}")

class Bird(Name, FlyerMixin, WalkerMixin):
    def __init__(self, name):
        super().__init__(name)
        print(f"I am a bird named {name}")

#v2 cambie el orden de las clases porque si no me da este TypeError: Cannot create a consistent method resolution order (MRO) for bases FlyerMixin, WalkerMixin
#class SuperHero(Name, WalkerMixin, SwimmerMixin, FlyerMixin):
class SuperHero(Name, FlyerMixin, WalkerMixin, SwimmerMixin):
    def __init__(self, name):
        super().__init__(name)
        print(f"I am a superhero named {name}")

class FlyingCharacter(Bird, SuperHero):
    def __init__(self, name):
        super().__init__(name) #Aqui Python como ya resolvio su MRO puede usar super sin llamarlo 2 veces
        print(f"I am a flying character named {name}") # Bird y SuperHero comparten Name como clase base, creando el problema del diamante

def main():
    human = Human("Juan")
    print(f"{human.get_name()}:")
    human.walk()
    print()

    fish = Fish("Dory")
    print(f"{fish.get_name()}:")
    fish.swim()
    print()

    bird = Bird("Big Bird")
    print(f"{bird.get_name()}:")
    bird.walk()
    bird.fly()
    print()

    superhero = SuperHero("Superman")
    print(f"{superhero.get_name()}:")
    superhero.walk()
    superhero.swim()
    superhero.fly()

def test_mro_and_diamond():
    print("\nTesting SuperHero MRO:")
    print(SuperHero.__mro__) # Muestra el orden en que Python busca los métodos de la clase

    print("\nTesting FlyingCharacter MRO:")
    print(FlyingCharacter.__mro__) # Demuestra como Python combina las clases y coloca Name una sola vez en el orden de busqueda, no lo repite

    print("\nTesting Diamond Inheritance:")
    character = FlyingCharacter("Superman")
    print(f"Character name: {character.get_name()}") # Demuestra que el nombre se inicializa una sola vez mediante Name
    character.walk()
    character.fly()
    character.swim()

    # El problema del diamante ocurre cuando dos clases heredan de una misma clase padre y la tercera clase hereda de ambas
    # En este ejemplo Bird y SuperHero heredan de Name, y luego FlyingCharacter hereda de ambas
    # El MRO determina el orden en que Python busca los metodos y evita que Name aparezca varias veces en la cadena de resolucion
    # Python utiliza el algoritmo C3 para establecer un orden consistente respetando las prioridades de herencia, resolviendo el problema de diamante

    # Y tal como mi v1 del codigo si las clases heredadas no estan en el mismo orden en diferentes clases
    # Python no sabe como resolverlo y da un TypeError: Cannot create a consistent method resolution order (MRO) for bases FlyerMixin, WalkerMixin

if __name__ == "__main__":
    main()
    test_mro_and_diamond()
