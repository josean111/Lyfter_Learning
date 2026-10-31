# 1. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)


import json
JSON_FILE = "pokemon_list.json"

def read_pokemon(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pokemon_list = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return

def read_pokemon(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)

    for pokemon in pokemon_list:
        print(f"Name: {pokemon['name']}")
        print(f"Type: {pokemon['type']}")
        print(f"Level: {pokemon['level']}")
        print()

def main():
    read_pokemon(JSON_FILE)


if __name__ == "__main__":
    main()
read_pokemon('pokemon_list.json')
