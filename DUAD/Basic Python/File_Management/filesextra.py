# 1. Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo
# Ejemplo:
# Entrada:
# Hola
# mundo
# esto
# es
# Python
# Salida:
# "Hola mundo esto es Python"

# with open("quijote.txt", 'r', encoding='utf-8') as file:
#     one_line = ""
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         one_line += line.strip()
#         print(line.strip())
#     print(one_line)

# with open("one_line_quijote.txt", 'w', encoding='utf-8') as file:
#     file.write(one_line)
# To avoid creating new file :)

# 2. Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)
# Ejemplo:
# Salida:
# "Este archivo contiene " 123 "palabras"

with open("quijote.txt", 'r', encoding='utf-8') as file:
    word_count = 0
    while True:
        line = file.readline()
        if not line:
            break
        word_count += len(line.split())
    print(f"Este archivo contiene {word_count} palabras")

# 3. Cree un programa que:
# Lea un archivo línea por línea
# Convierta cada línea a mayúsculas
# Escriba el contenido en un nuevo archivo
# Ejemplo:
# Entrada:
# # archivo original:

# hola mundo
# esto es python
# Salida:
# # archivo nuevo:

# HOLA MUNDO
# ESTO ES PYTHON

with open("quijote.txt", 'r', encoding='utf-8') as file:
    new_text = ""
    while True:
        line = file.readline()
        if not line:
            break
        new_text += line.upper()

# with open("UPPER_quijote.txt", 'w', encoding='utf-8') as file:
#     file.write(new_text)
# To avoid creating new file :)


# 4. Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente
# Ejemplo:
# Entrada:
# "Este es un nuevo registro"
# Salida:
# "El texto se agrega al final del archivo sin borrar lo anterior"

text = input("Dame una línea de texto: ")
with open("line_at_the_end.txt", 'a', encoding='utf-8') as file:     
    file.write(text+"\n")