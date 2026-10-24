# Cree un programa que verifique si todos los elementos de una lista son positivos
# Restricciones: No use funciones como all()
# Ejemplo:
# Entrada: my_list = [3, 6, 0, -2, 4]
# Salida: "Hay al menos un número negativo o cero"

print("---- Cree un programa que verifique si todos los elementos de una lista son positivos ----")
not_pos = False
my_list = [3, 6, 8, -2, 4]
for x in my_list:
    if x <= 0:
        not_pos = True
        break
if not_pos:
    print("Hay al menos un número negativo o cero")

#v2
print("---- v2 ----")
for y in my_list:
    if y <= 0:
        print("Hay al menos un número negativo o cero")
        break
else: # when break is not used
    print("Todos los números son positivos")

#v3 any or all super facil entiendo porque no usarlos
print("---- v3 ----")
if any(x <= 0 for x in my_list):
    print("Hay al menos un número negativo o cero")
else:
    print("Todos los números son positivos")

print(f"\n{all(y > 0 for x in my_list)}") #igual que any 
