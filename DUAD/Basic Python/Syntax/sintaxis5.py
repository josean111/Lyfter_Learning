
# 5. Dada n cantidad de notas de un estudiante, calcular:
# Cuantas notas tiene aprobadas (mayor a 70).
# Cuantas notas tiene desaprobadas (menor a 70).
# El promedio de todas.
# El promedio de las aprobadas.
# El promedio de las desaprobadas.

print("---- Dada n cantidad de notas de un estudiante, calcular:. ----")
print("---- Cuantas notas tiene aprobadas (mayor a 70) ----")
print("---- Cuantas notas tiene desaprobadas (menor a 70). ----")
print("---- El promedio de todas. ----")
print("---- El promedio de las aprobadas. ----")
print("---- El promedio de las desaprobadas. ----")
print(" Me gusto ese if de una linea para validar division en 0, lo hice sin revisarla resolucion ")

total_notas = int(input("Cuantas notas vamos a revisar? "))
notas = []
calculo = [0,0,0,0,0] # Pos0 # aprobadas, Pos1 # desaprobadas, Pos2 promedio total, Pos3 promedio aprobadas, pos4 promedio desaprobadas
for i in range(total_notas):
    notas.append(int(input(f"Nota {i+1}: ")))
    if notas[i] >= 70: # >= para no dejar el 70 afuera
        calculo[0] += 1
        calculo[3] += notas[i]
    else:
        calculo[1] += 1
        calculo[4] += notas[i]
    calculo[2] += notas[i]
print(f"\nNotas Aprobadas {calculo[0]}")
print(f"Notas DESaprobadas {calculo[1]}")
print(f"Promedio Total Notas {calculo[2]/total_notas}" if total_notas > 0 else "No hay notas para promedio")
print(f"Promedio Notas Aprobadas {calculo[3]/calculo[0]}" if calculo[0] > 0 else "No hay notas aprobadas para promedio")
print(f"Promedio Notas DesAprobadas {calculo[4]/calculo[1]}" if calculo[1] > 0 else "No hay notas DESaprobadas para promedio")