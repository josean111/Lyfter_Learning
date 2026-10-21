# Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio
# Ejemplo: Entrada my_list = [10, 20, 30, 40, 50]
# Salida :"Promedio:" 30
# Nueva lista: [40, 50]

print("---- Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio ----")
print("---- v1 ----")
average = 0
list_num = []
list_above = []
while True:
    num = int(input("Dame un número, para finalizar usa -1: "))
    if num == -1:
        break
    else: # v2 seria eliminar el else porque no se ocupa por el break, interesante
        list_num.append(num)
for x in list_num:
    average += x
average = average  / (len(list_num) )
for x in list_num:
    if x > average:
        list_above.append(x)
print(f"El promedio es {average}")
print(f"La lista original es: {list_num}")
print(f"La lista con solo valores mayores es: {list_above}")

#v2
print("---- v2 ----")
list_above = []
average2 = sum(list_num) / len(list_num)
list_above2 = [x for x in list_num if x > average2]

print(f"El promedio es {average2}")
print(f"La lista original es: {list_num}")
print(f"La lista con solo valores mayores es: {list_above2}")
