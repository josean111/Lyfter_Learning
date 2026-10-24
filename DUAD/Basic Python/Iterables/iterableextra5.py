# Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
# Ejemplo: Entrada: ['sol', 'estrella', 'luz', 'planeta', 'roca']
# Salida: ['estrella', 'planeta']

print("---- Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras ----")
print("---- v1 ----")

words = []
words_bigger4 = []
for i in range(5):
    words.append(input("Dame una palabra: "))
words_bigger4 = [y for y in words if len(y) > 4]
print(f"La lista de palabras es: {words}")
print(f"La lista de palabras mayores a 4 letras es: {words_bigger4}")

#v2
words2 = [input("Dame una palabra: ") for _ in range(5)] #we don't need counter use _
words_bigger4v2 = [y for y in words2 if len(y) > 4]
print(f"La lista de palabras es: {words2}")
print(f"La lista de palabras mayores a 4 letras es: {words_bigger4v2}")