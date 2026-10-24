#Convertidor de unidades de temperatura
# Pida al usuario ingresar una temperatura en Celsius
# Conviértala a Fahrenheit y Kelvin
# Muestre los tres valores
print("---- Convertidor de unidades de temperatura ----")
print("---- Pida al usuario ingresar una temperatura en Celsius ----")
print("---- PConviértala a Fahrenheit y Kelvin ----")
print("---- Muestre los tres valores ----")
temp = int(input("Ingrese temperatura en Celsius: "))
print(f"Celsius: {temp}")
#F = (°C × 1,8) + 32
#K = °C + 273,15
print(f"Fahrenheit: {temp * 1.8 + 32}")
print(f"Kelvin: {temp + 273.15}")