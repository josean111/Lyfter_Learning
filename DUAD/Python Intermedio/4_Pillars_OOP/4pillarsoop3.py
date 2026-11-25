# Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.
# Una clase puede adoptar varios metodos y atributos de otras clases en uno solo, tipico un superheroe con muchos poderes
class WalkerMixin:
    def walk(self):
        print("I am walking!")

class SwimmerMixin:
    def swim(self):
        print("I am swimming!")

class FlyerMixin:
    def fly(self):
        print("I am flying!")

class Human(WalkerMixin):
    def __init__(self, name):
        self.__name = name
        print(f"I am a human named {name}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class Fish(SwimmerMixin):
    def __init__(self, name):
        self.__name = name
        print(f"I am a fish named {name}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class Bird(WalkerMixin, FlyerMixin):
    def __init__(self, name):
        self.__name = name
        print(f"I am a bird named {name}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

class SuperHero(WalkerMixin, SwimmerMixin, FlyerMixin):
    def __init__(self, name):
        self.__name = name
        print(f"I am a superhero named {name}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

def main():
    human = Human("Juan")
    print(f"{human.get_name()}: {human.walk()}\n")    

    fish = Fish("Dory")
    print(f"{fish.get_name()}: ")
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

if __name__ == "__main__":
    main()