# 3. Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
# Ejemplo:
# Salida:
# Nombre: Pikachu
# Ataque: 55
# Defensa: 40
# Velocidad: 90

# Nombre: Bulbasaur
# Ataque: 49
# Defensa: 49
# Velocidad: 45
# ...


import json
JSON_FILE = "pokemon_list.json"

def show_stats(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            pokemon_list = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' does not exist.")
        return
    
    for pokemon in pokemon_list:
        print(f"Name: {pokemon['name']}")
        stats = pokemon['stats']

        # best_stats = []
        # for i in range(3):
        #     highest_value = -1
        #     for stat in stats:
        #         if stat not in best_stats and stats[stat] > highest_value:
        #             highest_value = stats[stat]
        #             highest_stat = stat
        #     best_stats.append(highest_stat)
        # for stat in stats:
        #     if stat in best_stats:
        #         print(f"{stat}: {stats[stat]}")

        if 'attack' in stats:
            print(f"Attack: {stats['attack']}")
        else:
            print("Error: Attack stat not found.")

        if 'defense' in stats:
            print(f"Defense: {stats['defense']}")
        else:
            print("Error: Defense stat not found.")

        if 'speed' in stats:
            print(f"Speed: {stats['speed']}")
        else:
            print("Error: Speed stat not found.")

        print()

def main():
    show_stats(JSON_FILE)


if __name__ == "__main__":
    main()

def show_stats(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        pokemon_list = json.load(file)
        for pokemon in pokemon_list:
            print(f"Name: {pokemon['name']}")
            stats = pokemon['stats']
            best_stats = []
            for i in range(3):
                highest_value = -1
                for stat in stats:
                    if stat not in best_stats and stats[stat] > highest_value:
                        highest_value = stats[stat]
                        highest_stat = stat
                best_stats.append(highest_stat)
            for stat in stats:
                if stat in best_stats:
                    print(f"{stat}: {stats[stat]}")
            print()

show_stats('pokemon_list.json')
