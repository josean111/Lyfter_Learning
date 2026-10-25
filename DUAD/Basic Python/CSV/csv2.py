# Lea sobre el resto de métodos del módulo csv aqui y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
# Ejemplo de archivo final:
# nombre	genero	desarrollador	clasificacion
# Grand Theft Auto IV	Accion	Rockstar Games	M
# The Elder Scrolls IV: Oblivion	RPG	Bethesda	M
# Tony Hawk's Pro Skater 2	Deportes	Activision	T

import csv

INPUT_FILE = "new_videogames_ranking.csv"
OUTPUT_FILE = "new_videogames_ranking_by_tabs.csv"

def read_videogames_ranking(file_path):
    video_games = []

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            video_games.append(row)

    return video_games

def save_videogames_ranking(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers,  delimiter="\t") # here we add the delimiter
        writer.writeheader()
        writer.writerows(data)

def main():
    video_games = read_videogames_ranking(INPUT_FILE)
    save_videogames_ranking(OUTPUT_FILE, video_games)

if __name__ == "__main__":
    main()