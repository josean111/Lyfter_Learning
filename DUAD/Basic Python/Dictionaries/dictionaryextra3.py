# 3. Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.
# Ejemplo: Entrada:
# products = [
#     {"name": "Monitor", "category": "Electrónica", "price": 200},
#     {"name": "Teclado", "category": "Electrónica", "price": 50},
#     {"name": "Silla", "category": "Muebles", "price": 120},
#     {"name": "Mesa", "category": "Muebles", "price": 180},
#     {"name": "Mouse", "category": "Electrónica", "price": 25},
# ]

print("---- Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría. ----")
print("---- v1 ----")
cumulated = {}
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
for product in products:
    category = product["category"]
    price = product["price"]
    if category not in cumulated:
        cumulated[category] = price
    else:
        cumulated[category] += price
    #cumulated.setdefault(category,[])
    #cumulated[category].append({product["name"],product["price"]})
print(cumulated)
