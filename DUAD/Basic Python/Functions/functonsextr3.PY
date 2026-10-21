# 3. Cree una función que reciba un string y retorne cuántas vocales contiene
# Ejemplo: Entrada:  "Hola mundo"
# Salida:  4rf3
def count_vocals(string):
    counter = 0
    for letter in string:
        if letter in ['a','e','i','o','u']:
            counter += 1
    return f"Su texto tiene {counter} vocales"


if __name__ == '__main__':
    print(count_vocals(input("Dame una palabra y te dire cuantas vocales tiene: ")))