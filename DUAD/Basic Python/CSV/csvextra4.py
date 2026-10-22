# 4. Cree un programa que abra un archivo .csv con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo .csv con videojuegos
# Pida al usuario ingresar el nombre de un desarrollador (ej. "Ubisoft")
# Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
# Ejemplo:
# Salida:
# Videojuegos desarrollados por Ubisoft:
# - Assassin's Creed II (Clasificación: M, Género: Aventura)
# - Rayman Legends (Clasificación: E, Género: Plataforma)

import csv
INPUT_FILE = "new_videogames_ranking.csv"

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        developer = input("Give me the name of a videogame developer: ")

        print(f"Games developed by {developer}:")

        for line in reader:
            if line[2].lower() == developer.lower():
                print(f"- {line[0]} (Rating: {line[3]}, Genre: {line[1]})")

def main():
    read_games(INPUT_FILE)

if __name__ == "__main__":
    main()