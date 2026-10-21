
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

