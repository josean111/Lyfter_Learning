# Cree un programa que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos.
# Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos.
# Si es mayor, muestre “Mayor”.
# Si es exactamente igual, muestre “Igual”.
# Ejemplos:
# 1040 → Mayor
# 140 → 460
# 600 → Igual
# 599 → 1

print("---- Cree un programa que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. ----")
print("---- Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. ----")
print("---- Si es mayor, muestre 'Mayor'. ----")
print("---- Si es exactamente igual, muestre 'Igual'. ----")

seconds = int(input("Ingrese el tiempo en segundos: "))

if seconds < 600:
    seconds_remaining = 600 - seconds
    print(seconds_remaining)
elif seconds > 600:
    print("Mayor")
else:
    print("Igual")