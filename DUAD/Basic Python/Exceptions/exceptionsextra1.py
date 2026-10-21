# 1. Cree un programa que:
# Pida al usuario su nombre
# Si el nombre es numérico (isdigit()), haga raise ValueError("El nombre no puede ser un número")
# Ejemplo:
# Entrada: "Ingrese su nombre: " 5
# Salida "El nombre no puede ser un número"
# Luego pida su edad
# Si no es un número válido, capture el ValueError y muestre un mensaje
# Ejemplo:
# Entrada: "Ingrese su edad: " cinco
# SAlida: "Número no valido"

# Si todo sale bien, imprima un mensaje: "Hola <nombre>, su edad es <edad>"
# Ejemplo:
# Entrada:"Ingrese su nombre: " "Jean Carlo"
# "Ingrese su edad: " 27
# SAlida Hola Jean Carlo, su edad es 27


def check_name_age():
    name = input("Ingrese su nombre: ")
    try:
        if name.isdigit():
            raise ValueError("El nombre no puede ser un número")
    except ValueError as error:
        print(error)
        return

    try:
        age = int(input("Ingrese su edad: "))
    except ValueError:
        print("Número no valido")
        return

    print(f"Hola {name}, su edad es {age}")

if __name__ == '__main__':
	check_name_age()