# 2. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
# Lea el archivo JSON de Pokémon
# Pida al usuario un tipo de Pokémon
# Muestre todos los Pokémon que sean de ese tipo
# Ejemplo:
# Entrada:
# "Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): " 
# "Fuego"
# Salida:
# "Los pokemos que existen de ese tipo son: "
# Charmander
# Growlithe
# Victini


import json

def search_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)
        pokemon_type = input("Enter the type of Pokemon you want to search: ")
        print("The Pokemon of that type are:")
        for pokemon in pokemon_list:
            if pokemon['type'].lower() == pokemon_type.lower():
                print(pokemon['name'])

search_pokemon('pokemon_list.json')
