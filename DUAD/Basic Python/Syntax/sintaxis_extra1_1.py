# Pasa los Ejercicios de Pseudocódigo previamente creados a código:
# Cree un programa que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
# Si el precio es menor a 100, el descuento es del 2%.
# Si el precio es mayor o igual a 100, el descuento es del 10%.
# Ejemplos:
# 120 → 108
# 40 → 39.2

print("---- Cree un programa que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que: ----")
print("---- Si el precio es menor a 100, el descuento es del 2%. ----")
print("---- Si el precio es mayor o igual a 100, el descuento es del 10%. ----")

price = float(input("Ingrese el precio del producto: "))
if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10
final_price = price - discount
print("El precio final es de", final_price)
