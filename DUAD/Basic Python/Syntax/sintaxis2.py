# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, pre-adolescente, adolescente, adulto joven, adulto, o adulto mayor.

print("---- Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, pre-adolescente, adolescente, adulto joven, adulto, o adulto mayor. ----")
name = input("Ingresa tu nombre: ")
last_name = input("Ingresa tu apellido: ")
age = int(input("Ingresa tu edad: "))


print("---- Usando match ----")

match age:
    case age if age <= 1:
        print("Eres un bebé")
    case age if age <= 9:
        print("Eres un niño")
    case age if age <= 12:
        print("Eres un pre-adolescente")
    case age if age <= 17:
        print("Eres un adolescente")
    case age if age <= 29:
        print("Eres un adulto joven")
    case age if age <= 59:
        print("Eres un adulto")
    case _:
        print("Eres un adulto mayor")

# 3. Solo if

print("---- Usando solo if ----")

if age <= 1:
    print("Eres un bebé")
elif age <= 9:
    print("Eres un niño")
elif age <= 12:
    print("Eres un pre-adolescente")
elif age <= 17:
    print("Eres un adolescente")
elif age <= 29:
    print("Eres un adulto joven")
elif age <= 59:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")