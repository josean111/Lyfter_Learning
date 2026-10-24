# Cree un programa que elimine todos los números impares de una lista.
# Ejemplos:
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]

print("---- Cree un programa que elimine todos los números impares de una lista. ----")
list = [1,2,3,4,5,6,7,8,9,10]
#v1
print("---- v1 ----")
counter = 0
for i in list:
    if not int(i) % 2 == 0:
        list.pop(counter)
    counter += 1
print(f"Lista sin Impares: {list}")
#v2
print("---- v2 ----")
list2 = [1,2,3,4,5,6,7,8,9,10]
for i,j in enumerate(list2):
    if not int(j) % 2 == 0:
        list2.pop(i)
print(f"Lista sin Impares: {list2}")
#v3
print("---- v3 ----")
even_list = []
list3 = [1,2,3,4,5,6,7,8,9,10]
for num in list3:
    if num % 2 == 0:
        even_list.append(num)
print(f"Lista sin Impares: {even_list}")
#v4
print("---- v4 ----")
list4 = [1,2,3,4,5,6,7,8,9,10,11]
counter = 0
while counter < len(list4) :
    if not list4[counter] % 2 == 0:
        list4.pop(counter)
    else:
        counter += 1
print(f"Lista sin Impares: {list4}")