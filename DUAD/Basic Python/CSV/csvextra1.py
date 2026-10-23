# 1. Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea
# Ejemplo: Salida:
# Nombre: Grand Theft Auto IV
# Género: Accion
# Desarrollador: Rockstar Games
# Clasificación: M


import csv

INPUT_FILE = "new_videogames_ranking.csv"


def read_games(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)

            if header is None:
                print("The file is empty.")
                return []

            games = []

            for line in reader:
                games.append(line)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
        return None

    return games


def show_games(games):
    if not games:
        print("No games found.")
        return

    for line in games:
        print(f"Name: {line[0]}")
        print(f"Genre: {line[1]}")
        print(f"Developer: {line[2]}")
        print(f"Rating: {line[3]}")
        print()


def main():
    games = read_games(INPUT_FILE)

    if games is not None:
        show_games(games)


if __name__ == "__main__":
    main()
