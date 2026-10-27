# 2. Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación


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


def ask_rating():
    rating = input("Give me a videogame rating: ")
    return rating


def filter_games_by_rating(games, rating):
    matching_games = []

    for line in games:
        if line[3].lower() == rating.lower():
            matching_games.append(line)

    return matching_games


def show_games(games):
    if not games:
        print("No games found matching the rating provided.")
        return

    for line in games:
        print(f"Name: {line[0]}")
        print(f"Genre: {line[1]}")
        print(f"Developer: {line[2]}")
        print(f"Rating: {line[3]}")
        print()


def main():
    games = read_games(INPUT_FILE)

    if games is None:
        return

    if not games:
        show_games(games)
        return

    rating = ask_rating()
    matching_games = filter_games_by_rating(games, rating)
    show_games(matching_games)


if __name__ == "__main__":
    main()
