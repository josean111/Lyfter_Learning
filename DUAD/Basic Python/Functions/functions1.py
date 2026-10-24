#1
# 1. Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
def first_print():
    print("I'm First")
    second_print()

def second_print():
    print("I'm Second")
#1


if __name__ == '__main__':
    first_print()