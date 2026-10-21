# Cree un programa que muestre el valor más pequeño de una lista sin usar min().
# Use una variable para comparar uno a uno
# Ejemplo: Entrada: my_list = [9, 4, 7, 1, 5]
# Salida: "El menor valor es 1"

print("---- Cree un programa que muestre el valor más pequeño de una lista sin usar min() ----")
#v1
print("---- v1 ----")
my_list = [9, 4, 7, 1, 5]
minimum = my_list[0]
for x in my_list:
    if minimum > x:
        minimum = x
print(f"El valor mínimo es {minimum}")

#v2
print("---- v2 ----")
minimum2 = None
for y in my_list:
    if minimum2 is None:
        minimum2 = y
    elif y < minimum2:
        minimum2 = y
print(f"El valor mínimo es {minimum2}")