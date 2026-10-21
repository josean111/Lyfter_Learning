# 3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
# Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.

import random
print("---- Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero. ----")
print("---- Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute. ----")
num = int(input("Ingresa un numero: "))
secret = random.randint(1,10)
print(f"Tu numero es {num} y el numero secreto es {secret}")
while secret != num:
    num = int(input("Ingresa un numero: "))
    secret = random.randint(1,10)
    print(f"Tu numero es {num} y el numero secreto es {secret}")

    #v2
    import random

# version 2
print("---- Adivina un numero del 1 al 10 ----")
num2 = int(input("Ingresa un numero: "))
secret2 = random.randint(1,10)
while secret2 != num2:

    if num2 < secret2:
        print("¡Muy bajo! Intenta con un número más grande.")
    else:
        print("¡Muy alto! Intenta con un número más pequeño.")

    num2 = int(input("Ingresa otro numero: "))

if num2 == secret2:
    print("🎉 ¡Felicidades! Adivinaste el número secreto.")
    print(f"El número secreto era {secret2}.")
