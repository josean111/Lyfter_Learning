# 4. Cree un programa que:
# Pida al usuario una línea de texto
# Agregue esa línea al final de un archivo existente
# Si el archivo no existe, lo crea automáticamente
# Ejemplo:
# Entrada:
# "Este es un nuevo registro"
# Salida:
# "El texto se agrega al final del archivo sin borrar lo anterior"

APPEND_FILE = "line_at_the_end.txt"

def append_to_file(file_path):
    text = input("Dame una línea de texto: ")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

def main():
    append_to_file(APPEND_FILE)

if __name__ == "__main__":
    main()