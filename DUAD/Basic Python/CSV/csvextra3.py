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

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        genres = {}
        
        for line in reader:
            genre = line[1]
            if genre in genres:
                genres[genre] += 1
            else:
                genres[genre] = 1
    print("Genre Totals:")
    for genre in sorted(genres):
        print(f"{genre}: {genres[genre]}")

read_games('new_videogames_ranking.csv')