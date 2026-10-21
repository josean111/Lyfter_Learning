# 4. Cree un programa que le pida tres números al usuario y muestre el mayor.

print("---- Cree un programa que le pida tres números al usuario y muestre el mayor. ----")
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
num3 = int(input("Ingresa el ultimo numero: "))
if num1 > num2:
    if num1 > num3:
        print(f"{num1} es el numero mayor")
elif num2 > num3:
    print(f"{num2} es el numero mayor")
else:
    print(f"{num3} es el numero mayor")

#v2
numbers = [num1, num2, num3]

highest_number = numbers[0]
position = 1

while position < len(numbers):

    if numbers[position] > highest_number:
        highest_number = numbers[position]
        
    position = position + 1

print(f"{highest_number} es el numero mayor")
