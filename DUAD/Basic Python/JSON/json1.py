# Investigue cómo leer y escribir archivos JSON en Python aquí.
# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
# Debe leer el archivo para importar los Pokémones existentes.
# Luego debe pedir la información del Pokémon a agregar.
# Finalmente debe guardar el nuevo Pokémon en el archivo.

import json
JSON_FILE = "pokemon_list.json"

def read_pokemon(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pokemon_list = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
        return []

    for pokemon in pokemon_list:
        print(pokemon)

    return pokemon_list


def add_pokemon(file_path):
    pokemon_list = read_pokemon(file_path)
    if not pokemon_list:
        return

    print("\nAdd a new Pokemon")

    name = input("Name: ")
    typing = input("Type: ")
    level = int(input("Level: "))
    weight = float(input("Weight in kg: "))

    shiny = input("Is it shiny? (yes/no): ")
    if shiny == "yes":
        shiny = True
    else:
        shiny = False

    item = input("Held item (leave empty if none): ")
    if item == "":
        item = None

    skills = input("Skills (separated by commas): ").split(",")

    print("\nEnter Pokemon stats")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Special attack: "))
    sp_defense = int(input("Special defense: "))
    speed = int(input("Speed: "))

    pokemon = {
        "name": name,
        "type": typing,
        "level": level,
        "weight_kg": weight,
        "is_shiny": shiny,
        "held_item": item,
        "skills": skills,
        "stats": {
            "hp": hp,
            "attack": attack,
            "defense": defense,
            "sp_attack": sp_attack,
            "sp_defense": sp_defense,
            "speed": speed
        }
    }

    pokemon_list.append(pokemon)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(pokemon_list, file, indent=4)

    print("\nUpdated Pokemon list:")
    read_pokemon(file_path)


def main():
    add_pokemon(JSON_FILE)


if __name__ == "__main__":
    main()
