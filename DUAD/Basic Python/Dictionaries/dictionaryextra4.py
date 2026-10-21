"""
Ejercicios de práctica: Diccionarios y Listas
Estructura: antología de poesía por géneros, autores y poemas.

Nota: los autores, poemas y versos son ficticios, creados solo
para tener datos con los que practicar.
"""

antologia = {
    "Poesía amorosa": {
        "Elena Duarte": {
            "nacionalidad": "México",
            "nacimiento": 1978,
            "movimiento": "Neorromanticismo",
            "poemas": {
                "Manos de otoño": {
                    "año": 2005,
                    "versos": [
                        "Tus manos guardan el color de octubre",
                        "y en ellas duerme un jardín pequeño",
                        "que solo florece cuando tú lo nombras",
                        "y calla cuando el silencio te habita",
                    ],
                },
                "Carta sin destino": {
                    "año": 2010,
                    "versos": [
                        "Escribo tu nombre en el vapor del café",
                        "se borra antes de que el día empiece",
                        "así también se borran las promesas",
                    ],
                },
            },
        },
        "Rodrigo Fontán": {
            "nacionalidad": "Argentina",
            "nacimiento": 1985,
            "movimiento": "Posmodernismo",
            "poemas": {
                "Distancias": {
                    "año": 2012,
                    "versos": [
                        "Entre tu ciudad y la mía hay un mar de números",
                        "que ninguna llamada logra cruzar del todo",
                        "y aun así insistimos en marcar",
                    ],
                },
            },
        },
    },
    "Poesía social": {
        "Marcos Iriarte": {
            "nacionalidad": "Chile",
            "nacimiento": 1960,
            "movimiento": "Realismo social",
            "poemas": {
                "Los que no tienen nombre": {
                    "año": 1988,
                    "versos": [
                        "En la fila del hambre nadie pregunta apellidos",
                        "el frío no distingue entre obreros y patrones",
                        "pero el pan sí, y eso lo sabe la calle",
                        "eso lo sabe el niño que no fue a la escuela",
                    ],
                },
            },
        },
        "Andrea Solís": {
            "nacionalidad": "Colombia",
            "nacimiento": 1972,
            "movimiento": "Poesía comprometida",
            "poemas": {
                "Barrio alto, barrio bajo": {
                    "año": 1995,
                    "versos": [
                        "Aquí las escaleras suben pero el futuro no",
                        "aquí se aprende a esperar el bus y la suerte",
                        "aquí también hay quien sueña con salir en los libros",
                    ],
                },
            },
        },
    },
    "Haiku": {
        "Kenji Aramaki": {
            "nacionalidad": "Japón",
            "nacimiento": 1950,
            "movimiento": "Haiku contemporáneo",
            "poemas": {
                "Estaciones": {
                    "año": 2001,
                    "versos": [
                        "hoja que cae",
                        "el estanque la espera",
                        "sin hacer ruido",
                    ],
                },
                "Invierno breve": {
                    "año": 2003,
                    "versos": [
                        "nieve en la puerta",
                        "un gato deja huellas",
                        "hacia ninguna parte",
                    ],
                },
            },
        },
    },
}


# ============================================================
# EJERCICIO 1 — Estadísticas por género
# ============================================================
# Para cada género, calcula:
#   a) el número total de versos escritos (sumando TODOS los poemas
#      de TODOS los autores de ese género)
#   b) cuál es el poema más largo del género (el que tiene más
#      versos), indicando autor y título.
#
# Devuelve un nuevo diccionario con esta forma:
# {
#     "Poesía amorosa": {
#         "total_versos": 7,
#         "poema_mas_largo": ("Elena Duarte", "Manos de otoño", 4)
#     },
#     ...
# }


# ============================================================
# EJERCICIO 2 — Buscador de palabras
# ============================================================
# Escribe una función que reciba una palabra clave y recorra TODA
# la antología (género -> autor -> poema -> versos) buscando esa
# palabra dentro de cada verso (sin usar regex; usa .lower() y el
# operador "in" o .split()).
#
# Debe devolver una lista de tuplas:
#   (genero, autor, titulo_poema, numero_de_verso, verso_completo)
# por cada coincidencia encontrada. numero_de_verso empieza en 1.


# ============================================================
# EJERCICIO 3 — Ranking de autores por productividad
# ============================================================
# Construye una lista de tuplas (autor, genero, total_versos) donde
# total_versos es la suma de versos de TODOS los poemas de ese autor.
# Ordena la lista de mayor a menor cantidad de versos usando sorted()
# y una función/lambda como key (sin usar collections.Counter).
#
# Pista: en esta antología cada autor aparece en un solo género,
# pero tu solución debería funcionar igual aunque apareciera en varios.


# ============================================================
# EJERCICIO 4 — Clasificación por longitud de poema
# ============================================================
# Crea un nuevo diccionario "invertido" con esta forma:
# {
#     "corto":   [(genero, autor, titulo), ...],   # <= 3 versos
#     "mediano": [(genero, autor, titulo), ...],   # 4 a 6 versos
#     "largo":   [(genero, autor, titulo), ...],   # 7 versos o más
# }
# recorriendo toda la antología y clasificando cada poema según
# su número de versos.


# ============================================================
# EJERCICIO 5 — Palabra más repetida por movimiento literario
# ============================================================
# Agrupa a los autores según su atributo "movimiento" (sin importar
# el género al que pertenezcan) y, para cada movimiento, calcula
# cuál es la palabra que más se repite entre TODOS los versos de
# TODOS los poemas de los autores de ese movimiento.
#
# Reglas:
#   - No uses collections.Counter: construye tú mismo un diccionario
#     contador con .get() o comprobando "if palabra in dict".
#   - Pasa cada verso a minúsculas y sepáralo con .split() para
#     obtener las palabras (no te preocupes por signos de puntuación).
#
# Devuelve un diccionario:
# {
#     "Neorromanticismo": ("palabra_mas_comun", cantidad_de_veces),
#     ...
# }

# antologia diccionario
# generos diccionario dentro de antologia
# autor diccionario dentro de los generos
# poemas diccionario dentro del autor
# versos lista de versos dentro del poema


# print("Géneros disponibles:", list(antologia.keys()))
# print("Géneros disponibles:", antologia.keys())


# ============================================================
# EJERCICIO 1 — Estadísticas por género
# ============================================================
# Para cada género, calcula:
#   a) el número total de versos escritos (sumando TODOS los poemas
#      de TODOS los autores de ese género)
#   b) cuál es el poema más largo del género (el que tiene más
#      versos), indicando autor y título.
#
# Devuelve un nuevo diccionario con esta forma:
# {
#     "Poesía amorosa": {
#         "total_versos": 7,
#         "poema_mas_largo": ("Elena Duarte", "Manos de otoño", 4)
#     },
#     ...
# }

#v1
# print(antologia["Poesía amorosa"]["Elena Duarte"]["poemas"]["Manos de otoño"]["versos"])
# for poema in antologia["Poesía amorosa"]["Elena Duarte"]["poemas"]["Manos de otoño"]["versos"]:
#     print(poema)
statistics = {}
longest = {}
# for gender in antologia:
#     for author in antologia[gender]:
#         for poem in antologia[gender][author]["poemas"]:
#             biggest_poem =  len(antologia[gender][author]["poemas"][poem]["versos"])
#             # if gender not in longest:
#             #     longest["longest_poem"] = author,poem,size
#             # elif size > longest["longest_poem"][2] and gender == longest["longest_poem"]    :
#             #     longest = {"longest_poem":[author,poem,size]}
#             for verse in antologia[gender][author]["poemas"][poem]["versos"]:
#                 #print(author["poemas"])
# #               #print(gender in statistics)
#                 #print(longest["longest_poem"])
#                 # if size > longest["longest_poem"][2]:
#                 #     print("bigger")
#                 if gender not in statistics:
#                     statistics[gender] = {"total_verses" : 1}
#                     longest["longest_poem"] = author,poem,biggest_poem
#                 else:
#                     statistics[gender] = {"total_verses" : (statistics[gender]["total_verses"] + 1)}
#                     if biggest_poem > longest["longest_poem"][2]:
#                         longest = {"longest_poem":[author,poem,biggest_poem]}
#                 #statistics[gender] = statistics.get(gender, 0) + 1 #v2
#                 #statistics[gender] =  statistics.get(gender, {"total_verses" : (statistics[gender]["total_verses"] + 1), "longest_poem":[author,poem,verse]})
#             statistics[gender].update(longest)
# # for each gender
# #     for each author inside that gender
# #         for each poem-key inside ["poemas"]
# #             for each verse inside that poem's ["versos"]
# #                 print the verse

#v2
# for gender in antologia:
#     for author in antologia[gender]:
#         for poem in antologia[gender][author]["poemas"]:
#             biggest_poem = len(antologia[gender][author]["poemas"][poem]["versos"])
#             statistics[gender] = statistics.get(gender, {"total_verses" : 0, "longest_poem": [author,poem,biggest_poem]})
#             statistics[gender]["total_verses"] += (biggest_poem)
            
#             # longest["longest_poem"] = longest.get("longest_poem", [author,poem,biggest_poem])
#             if biggest_poem > statistics[gender]["longest_poem"][2]:
#                 statistics[gender]["longest_poem"] = [author,poem,biggest_poem]
#         # statistics[gender].update(longest)
#         # longest = {}

#v3
for gender in antologia:
    statistics[gender] = statistics.get(gender, {"total_verses" : 0, "longest_poem": ["","",0]})
    for author in antologia[gender]:
        for poem in antologia[gender][author]["poemas"]:
            biggest_poem = len(antologia[gender][author]["poemas"][poem]["versos"])
            statistics[gender]["total_verses"] += (biggest_poem)
            if biggest_poem > statistics[gender]["longest_poem"][2]:
                statistics[gender]["longest_poem"] = [author,poem,biggest_poem]

print("---- EJERCICIO 1 — Estadísticas por género Para cada género, calcula:   ----")
print("---- a) el número total de versos escritos (sumando TODOS los poemas de TODOS los autores de ese género) ----")
print("---- b) cuál es el poema más largo del género (el que tiene más versos), indicando autor y título. ----")
# {
#     "Poesía amorosa": {
#         "total_versos": 7,
#         "poema_mas_largo": ("Elena Duarte", "Manos de otoño", 4)
#     },
# }
print("Statistics ",statistics)


# ============================================================
# EJERCICIO 2 — Buscador de palabras
# ============================================================
# Escribe una función que reciba una palabra clave y recorra TODA
# la antología (género -> autor -> poema -> versos) buscando esa
# palabra dentro de cada verso (sin usar regex; usa .lower() y el
# operador "in" o .split()).
#
# Debe devolver una lista de tuplas:
#   (genero, autor, titulo_poema, numero_de_verso, verso_completo)
# por cada coincidencia encontrada. numero_de_verso empieza en 1.


print("---- EJERCICIO 2 — Buscador de palabras  ----")
print("---- Escribe una función que reciba una palabra clave y recorra TODA # la antología (género -> autor -> poema -> versos) buscando esa palabra dentro de cada verso  ----")

#v1
# wordy = input("Escribe una palabra y revisamos si esta en alguno de los versos: ")
# counter = 1
# searcher = []
# for gender in antologia:
#     for author in antologia[gender]:
#         for poem in antologia[gender][author]["poemas"]:
#             for verse in antologia[gender][author]["poemas"][poem]["versos"]:
#                 if verse.lower().find(wordy.lower()) > -1:
#                     searcher.append([gender, author, poem, counter, verse])
#                 counter += 1

#v2
# wordy = input("Escribe una palabra y revisamos si esta en alguno de los versos: ").lower()
# searcher = []
# counter = 0
# for gender in antologia:
#     for author in antologia[gender]:
#         for poem in antologia[gender][author]["poemas"]:
#             counter = 1
#             for verse in antologia[gender][author]["poemas"][poem]["versos"]:
#                 if wordy in verse.lower().split():
#                     searcher.append((gender, author, poem, counter, verse))
#                 counter += 1

# print(searcher)

# ============================================================
# EJERCICIO 3 — Ranking de autores por productividad
# ============================================================
# Construye una lista de tuplas (autor, genero, total_versos) donde
# total_versos es la suma de versos de TODOS los poemas de ese autor.
# Ordena la lista de mayor a menor cantidad de versos usando sorted()
# y una función/lambda como key (sin usar collections.Counter).
#
# Pista: en esta antología cada autor aparece en un solo género,
# pero tu solución debería funcionar igual aunque apareciera en varios.

#v1
print("---- EJERCICIO 3 — Ranking de autores por productividad  ----")
print("---- Construye una lista de tuplas (autor, genero, total_versos) donde # total_versos es la suma de versos de TODOS los poemas de ese autor. ----")
print("---- Ordena la lista de mayor a menor cantidad de versos usando sorted()  y una función/lambda como key (sin usar collections.Counter). ----")
#  ----")
authors = []
for gender in antologia:
    for author in antologia[gender]:
        length = 0
        authors.append((author, gender, length))
        for poem in antologia[gender][author]["poemas"]:
            length += len(antologia[gender][author]["poemas"][poem]["versos"])
            # print(author not in authors)
            # print(f" author {author} y authors tiene {authors}")
            # #print(f" authors[2] {authors[0]} y authors tiene {authors}")
        if authors[-1].index(author) > -1:
            authors.remove(author)
            authors.append((author, gender, length))
        else:
            authors[authors.index(author)][2] =  authors[authors.index(author)][2] + length
            #print(biggest_poem)
            # statistics[gender]["total_verses"] += (biggest_poem)
            # if biggest_poem > statistics[gender]["longest_poem"][2]:
            #     statistics[gender]["longest_poem"] = [author,poem,biggest_poem]
print(sorted(authors, key= lambda verses_length : verses_length[2], reverse=True))