print("---- Clasificador de Nivel Gamer ----")

name = input("Ingresa tu nombre: ")
hours = int(input("¿Cuántas horas llevas jugando? "))
is_competitive = input("¿Juegas competitivo? (si/no): ")

if hours < 10:
    category = "Novato 🟢"
    message = "¡Bienvenido al mundo gamer!"
elif hours < 50:
    category = "Casual 🔵"
    message = "Ya le estás agarrando el ritmo."
elif hours < 200:
    category = "Gamer 🟣"
    message = "Definitivamente sabes lo que haces."
elif hours >= 200 and is_competitive == "si":
    category = "Pro 🔴"
    message = "Eres una leyenda viviente."
else:
    category = "Gamer 🟣"
    message = "Tienes la experiencia, pero aún no entras al competitivo."

print(f"{name}, tu categoría es: {category}")
print(message)

print("---- Simulador de Ahorro ----")

name = input("Ingresa tu nombre: ")
monthly_savings = float(input("¿Cuántos dólares ahorras por mes? "))
months = int(input("¿Cuántos meses deseas simular? "))
total = 0

for month in range(1, months + 1):
    total += monthly_savings
    print(f"Mes {month}: total acumulado = {total}")

print(f"{name}, en {months} meses habrás ahorrado: {total}")