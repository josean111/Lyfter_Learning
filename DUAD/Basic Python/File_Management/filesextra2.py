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