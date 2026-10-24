# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.
# Debe incluir:
# Nombre
# Género
# Desarrollador
# Clasificación ESRB
# Ejemplo de archivo final:
# nombre,genero,desarrollador,clasificacion
# Grand Theft Auto IV,Accion,Rockstar Games,M
# The Elder Scrolls IV: Oblivion,RPG,Bethesda,M
# Tony Hawk's Pro Skater 2,Deportes,Activision,T

import csv

def save_videogames_ranking(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

video_games = [
    {
        "Name": "Grand Theft Auto IV",
        "Genre": "Action",
        "Developer": "Rockstar Games",
        "Rating": "M",
    },
    {
        "Name": "The Elder Scrolls IV: Oblivion",
        "Genre": "RPG",
        "Developer": "Bethesda Game Studios",
        "Rating": "M",
    },
    {
        "Name": "Tony Hawk's Pro Skater 2",
        "Genre": "Sports",
        "Developer": "Neversoft",
        "Rating": "T",
    },
    {
        "Name": "Minecraft",
        "Genre": "Sandbox",
        "Developer": "Mojang Studios",
        "Rating": "E10+",
    },
    {
        "Name": "The Legend of Zelda: Breath of the Wild",
        "Genre": "Adventure",
        "Developer": "Nintendo EPD",
        "Rating": "E10+",
    },
    {
        "Name": "God of War",
        "Genre": "Action",
        "Developer": "Santa Monica Studio",
        "Rating": "M",
    },
    {
        "Name": "Super Mario Odyssey",
        "Genre": "Platformer",
        "Developer": "Nintendo EPD",
        "Rating": "E10+",
    },
    {
        "Name": "The Sims 4",
        "Genre": "Simulation",
        "Developer": "Maxis",
        "Rating": "T",
    },
    {
        "Name": "Overwatch 2",
        "Genre": "Shooter",
        "Developer": "Blizzard Entertainment",
        "Rating": "T",
    },
    {
        "Name": "Red Dead Redemption 2",
        "Genre": "Action-adventure",
        "Developer": "Rockstar Games",
        "Rating": "M",
    },
]

save_videogames_ranking('new_videogames_ranking.csv', video_games)