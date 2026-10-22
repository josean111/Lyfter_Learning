# 2. Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.
# (Considere que las palabras están separadas por espacios y/o saltos de línea)
# Ejemplo:
# Salida:
# "Este archivo contiene " 123 "palabras"
INPUT_FILE = "quijote.txt"

def count_words(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        word_count = 0
        while True:
            line = file.readline()
            if not line:
                break
            word_count += len(line.split())

    return word_count

def main():    
    word_count = count_words(INPUT_FILE)
    print(f"Este archivo contiene {word_count} palabras")

if __name__ == "__main__":
    main()