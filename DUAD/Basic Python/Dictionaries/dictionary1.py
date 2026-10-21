# Cree un diccionario que guarde la siguiente información sobre un hotel:
# nombre
# numero_de_estrellas
# habitaciones
# El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
# numero
# piso
# precio_por_noche

print("---- Cree un diccionario que guarde la siguiente información sobre un hotel: ----")
hotel = {
    "name": "Hotel Primero",
    "stars": 3,
    "rooms": [
        {
            "numero": 1,
            "piso": 1,
            "precio_por_noche": 150
        }
        ,{
            "numero": 2,
            "piso": 1,
            "precio_por_noche": 175
        }
    ]
}
print(hotel)