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