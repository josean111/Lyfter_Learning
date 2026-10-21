# Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
print("---- Cree un programa que pida 3 números al usuario. Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”. ----")
num = [0,0,0]
for i in range(3):
    num[i] = int(input("Ingrese un numero: "))
if(num[0] == 30 or num[1] == 30 or num[2] == 30 or sum(num) == 30):
    print("Correcto")
else:
    print("Incorrecto")