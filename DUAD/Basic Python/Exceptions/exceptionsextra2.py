# 2. Cree una función convertir_a_entero(lista) que:
# Reciba una lista de strings
# Intente convertir cada elemento a entero usando int()
# Use try-except para atrapar los errores ValueError
# Si algún elemento no puede convertirse, mostrar "No se pudo convertir el elemento: <valor>" y continuar con los demás
# Ejemplo: my_list = ['4', 'hola', '10', '5.2']
# Salida: "Resultado:"
# "4" "convertido a" 4
# "No se pudo convertir el elemento: hola"
# "10" "convertido a" 10
# "No se pudo convertir el elemento: 5.2"

my_list = ['004', 'hola', '10', '5.2']
def int_to_list(string_list):
    new_list = "Resultado:\n"
    for element in string_list:
        try:
            int_number = int(element)
        except ValueError:
            new_list += f"No se pudo convertir el elemento: {element}\n"
            continue
        new_list += f'"{element}" "convertido a" {int_number}\n'
    return new_list

if __name__ == '__main__':
	print(int_to_list(my_list))