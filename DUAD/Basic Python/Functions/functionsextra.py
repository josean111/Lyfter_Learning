# 1. Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
# Ejemplo:  Entrada:  "programacion"
# "Ingrese el carácter que desea buscar:" "o"
# Salida: # "Se ha encontrado 2 veces el carácter"
def text_count_chars(text,character):
    counter = 0
    for char in text:
        if char == character:
            counter += 1
    return f"Se ha encontrado {counter} veces el caracter"

if __name__ == '__main__':
    print(text_count_chars(input("Escribe un texto: "),input("Escribe un caracter a buscar: ")))