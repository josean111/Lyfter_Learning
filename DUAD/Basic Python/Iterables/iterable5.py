# Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
# Ejemplos:
# 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

print("---- Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto. -----")

#v1
list1 = []
big3 = None
counter = 0
for i in range(10):
    # list1.append = (int(input("Dame un numero: "))) Esto me sirvio pero fue mi v1
    list1.append(int(input("Dame un numero: ")))

    if counter == 0:
        big2 = list1[len(list1) - 1]
    elif list1[len(list1) - 1] > big2:
        big2 = list1[len(list1) - 1]

    if big3 is None or big3 < list1[len(list1) - 1]:
        big3 = list1[len(list1) - 1]
    counter += 1
big = list1[0]
print("---- v1 ----")
for j in list1:
    if big < j:
        big = j
print(f"{list1}. El más alto fue {big}")
#v2
print("---- v2 ----")
print(f"{list1}. El más alto fue {big2}")
#v3
print("---- v3 ----")
print(f"{list1}. El más alto fue {big3}")
#v3
print("---- v3 ----")
print(f"{list1}. El más alto fue {max(list1)}")
