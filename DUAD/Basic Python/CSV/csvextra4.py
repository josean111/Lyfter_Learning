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


def ask_developer():
    developer = input("Give me the name of a videogame developer: ")
    return developer


def filter_games_by_developer(games, developer):
    matching_games = []

    for line in games:
        if line[2].lower() == developer.lower():
            matching_games.append(line)

    return matching_games


def show_games_by_developer(games, developer):
    if not games:
        print("No games found.")
        return
    
    print(f"Games developed by {developer}:")
    for line in games:
        print(f"- {line[0]} (Rating: {line[3]}, Genre: {line[1]})")


def main():
    games = read_games(INPUT_FILE)

    if games is None:
        return

    developer = ask_developer()
    matching_games = filter_games_by_developer(games, developer)
    show_games_by_developer(matching_games, developer)


if __name__ == "__main__":
    main()
import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)

        developer = input("Give me the name of a videogame developer: ")

        print(f"Games developed by {developer}:")

        for line in reader:
            if line[2].lower() == developer.lower():
                print(f"- {line[0]} (Rating: {line[3]}, Genre: {line[1]})")

read_games('new_videogames_ranking.csv')
