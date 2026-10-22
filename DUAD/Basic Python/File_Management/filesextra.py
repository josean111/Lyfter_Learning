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

INPUT_FILE = "quijote.txt"
OUTPUT_FILE = "one_line_quijote.txt"

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        one_line = ""
        while True:
            line = file.readline()
            if not line:
                break
            one_line += line.strip() + " "
    return one_line.strip()

def write_file(file_path, one_line):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(one_line)

def main():        
    one_line = read_file(INPUT_FILE)
    write_file(OUTPUT_FILE, one_line)

if __name__ == '__main__':
    main()