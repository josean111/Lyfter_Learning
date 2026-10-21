# Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar
# Ejemplo:
# Entrada:
# my_list = [4, 2, 7, 2, 8, 2, 1]
# numero_a_buscar = 2
# Salida
# "El número 2 aparece 3 veces"

print("---- Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar  ----")
my_list = [4, 2, 7, 2, 8, 2, 1]
dictionary_counter = {}

for num in my_list:
    if num in dictionary_counter:
        dictionary_counter[num] += 1
    else:
        dictionary_counter[num] = 1
print(f"Lista de números: {my_list}")
num_search = int(input("Dame un numero a buscar en lista: "))
print(f"El número {num_search} aparece {dictionary_counter.get(num_search, 0)} veces")
print(f"Diccionario de conteo: {dictionary_counter}")

#v2
print("---- v2 ----")
list1 = []
dictionary_counter2 = {}
continue_nums = True
while continue_nums:
    num = int(input("Dame un número, para finalizar usa -1: "))
    if num == -1:
        continue_nums = False
        break
    else:
        list1.append(num)
        if list1[-1] in dictionary_counter2:
            dictionary_counter2[list1[-1]] += 1
        else:
            dictionary_counter2[list1[-1]] = 1
print(f"Lista de números: {list1}")
num_search2 = int(input("Cual numero buscamos en lista: "))
print(f"El número {num_search2} aparece {dictionary_counter2.get(num_search2, 0)} veces")
print(f"Función count: {list1.count(num_search2)}")
print(f"Diccionario de conteo: {dictionary_counter2}")

#v3
print("---- v3 ----")
counter_num = 0
num_search3 = int(input("Cual numero buscamos en lista anterior: "))
for num in list1:
    if num == num_search3:
        counter_num += 1
print(f"El número {num_search3} aparece {counter_num} veces")

#v4 Ya esta es la version mas pro :)
# dictionary_counter4 = {}
# while True:
#     num = int(input("Dame un número, para finalizar usa -1: "))
#     if num == -1:
#         break
#     else:
#         dictionary_counter4[num] = dictionary_counter4.get(num, 0) + 1
# print(f"Lista de números: {dictionary_counter4.keys()}")
# num_search4 = int(input("Cual numero buscamos en el diccionario: "))
# print(f"El número {num_search4} aparece {dictionary_counter4.get(num_search4, 0)} veces")
