# Tabla de multiplicar personalizada
# Pida al usuario un número del 1 al 10
# Muestre su tabla de multiplicar del 1 al 12

print("---- Tabla de multiplicar personalizada ----")
print("---- Pida al usuario un número del 1 al 10 ----")
print("---- Muestre su tabla de multiplicar del 1 al 12 ----")
num = int(input("Ingrese un número: "))
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")