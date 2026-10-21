# 3. Cree un programa que use una lista para eliminar keys de un diccionario.
# Ejemplos:
# list_of_keys = ["access_level", "age"]
# employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
# → {"name": "John", 'email": "john@ecorp.com"}

print("---- Cree un programa que use una lista para eliminar keys de un diccionario. ----")
print("---- v1 ----")
list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
for key in list_of_keys:
    employee.pop(key)
print(f"La lista sin los key de la lista es: {employee}")

#v2
print("---- v2 ----")
list_of_keys2 = ["access_level", "age"]
employee2 = {
    "name": "John",
    "email": "john@ecorp.com",
    "access_level": 5,
    "age": 28
}

new_employee = {
    key: value
    for key, value in employee2.items()
    if key not in list_of_keys
}
print(f"La lista sin los key de la lista es: {new_employee}")
