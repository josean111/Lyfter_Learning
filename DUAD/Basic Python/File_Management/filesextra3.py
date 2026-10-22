
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
INPUT_FILE = "quijote.txt"
OUTPUT_FILE = "UPPER_quijote.txt"

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        new_text = ""
        while True:
            line = file.readline()
            if not line:
                break
            new_text += line.upper()

    return new_text


def write_file(file_path, new_text):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_text)

def main():
    new_text = read_file(INPUT_FILE)
    write_file(OUTPUT_FILE, new_text)

if __name__ == "__main__":
    main()
