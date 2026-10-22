# 2. Cree un programa que abra un archivo .csv con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
# Lea el archivo CSV de videojuegos
# Pida al usuario una clasificación ESRB (por ejemplo: "T")
# Muestre todos los videojuegos que tengan esa clasificación

import csv
INPUT_FILE = "new_videogames_ranking.csv"

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        to_check = input("Give me a videogame Rating: ")
        for line in reader:
            if line[3].lower() == to_check.lower():
                print(f"Name: {line[0]}")
                print(f"Genre: {line[1]}") 
                print(f"Developer: {line[2]}") 
                print(f"Rating: {line[3]}") 
                print()

def main():
    read_games(INPUT_FILE)


if __name__ == "__main__":
    main()