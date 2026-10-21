# 1. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)


import json

def read_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)

    for pokemon in pokemon_list:
        print(f"Name: {pokemon['name']}")
        print(f"Type: {pokemon['type']}")
        print(f"Level: {pokemon['level']}")
        print()

read_pokemon('pokemon_list.json')
