# # 3. Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# # Lea el archivo .csv con videojuegos
# # Cuente cuántos videojuegos hay de cada género
# # Muestre el resultado de forma ordenada
# # Ejemplo:
# # Salida:
# Géneros encontrados:
# Acción: 5
# Aventura: 3
# Deportes: 4
# ...


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


def count_genres(games):
    genres = {}

    for line in games:
        genre = line[1]

        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1

    return genres


def show_genres(genres):
    if not genres:
        print("No games found.")
        return

    print("Genre Totals:")

    for genre in sorted(genres, key=genres.get, reverse=True):
        print(f"{genre}: {genres[genre]}")


def main():
    games = read_games(INPUT_FILE)

    if games is None:
        return

    genres = count_genres(games)
    show_genres(genres)


if __name__ == "__main__":
    main()
