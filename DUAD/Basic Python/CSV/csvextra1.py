# 1. Cree un programa que abra un archivo .csv con la información de videojuegos (el que fue generado en el ejercicio 1) y:
# Lea cada línea usando csv.reader()
# Muestre el contenido en pantalla de forma legible, línea por línea
# Ejemplo: Salida:
# Nombre: Grand Theft Auto IV
# Género: Accion
# Desarrollador: Rockstar Games
# Clasificación: M

import csv

def read_games(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)
        for line in reader:
            # if line[0].startswith("Name"): #v1
            #     continue #v1
            print(f"Name: {line[0]}")
            print(f"Genre: {line[1]}") 
            print(f"Developer: {line[2]}") 
            print(f"Rating: {line[3]}") 
            print()
read_games('new_videogames_ranking.csv')