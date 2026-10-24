# 4. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON
# Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
# Calcule y muestre el promedio de nivel para cada tipo:
# Ejemplo:
# Salida:
# Tipo: Agua → Promedio de nivel: 42.6
# Tipo: Fuego → Promedio de nivel: 37.2
# Tipo: Planta → Promedio de nivel: 30.4

import json

def average_level(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)
        total_levels = {}
        pokemon_count = {}
        for pokemon in pokemon_list:
            pokemon_type = pokemon['type']
            level = pokemon['level']
            if pokemon_type in total_levels:
                total_levels[pokemon_type] += level
                pokemon_count[pokemon_type] += 1
            else:
                total_levels[pokemon_type] = level
                pokemon_count[pokemon_type] = 1

        for pokemon_type in total_levels:
            average = total_levels[pokemon_type] / pokemon_count[pokemon_type]
            print(f"Type: {pokemon_type} - Average level: {average}")

average_level('pokemon_list.json')
    