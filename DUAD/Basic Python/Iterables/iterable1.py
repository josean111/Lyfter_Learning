# Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
# Ejemplos:
# first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
# second_list = ["casos", 'los", "la", "por", "es", "util"] ->
# Hay casos
# en los
# que la
# iteracion por
# indice es
# muy util

print("---- Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo. ----")
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"] 
#v1
print("---- v1 ----")
for i, j in enumerate(first_list):
    for i2, j2 in enumerate(second_list):
        if i == i2:
            print(f"{j} {j2}" )
            break
print("---- v2 ----")
#v2
for i in range(len(first_list)):
    for i2 in range(len(second_list)):
        if i == i2:
            print(f"{first_list[i]} {second_list[i2]}" )
            break
#v3
print("---- v3 ----")
for i in range(len(first_list)):
    print(f"{first_list[i]} {second_list[i]}" )