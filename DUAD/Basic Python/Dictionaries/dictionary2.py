# Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
# Ejemplos:
# list_a = ["first_name", "last_name", "role"]
# list_b = ["Alek", "Castillo", "Software Engineer"]
# → {"first_name": "Alek", "last_name": "Castillo", "role": "Software Engineer"}

print("---- Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values. ----")
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

#v1 
print("---- v1 ----")
dictionary = {}
for count in range(len(list_a)):
    dictionary[list_a[count]] = list_b[count]
print(dictionary)

#v2
print("---- v2 ----")
dictionary2 = {}
for index, key in enumerate(list_a):
    dictionary2[key] = list_b[index]
print(dictionary2)