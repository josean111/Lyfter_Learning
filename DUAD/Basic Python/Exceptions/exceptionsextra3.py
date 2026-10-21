# 3. Cree una función sumar_valores(lista) que:
# Reciba una lista de elementos (strings, enteros, flotantes mezclados)
# Intente convertir cada elemento a tipo float
# Si puede, sume el valor y muestre: "<valor> sumado correctamente"
# Si no puede, muestre: "Elemento inválido: <valor>"
# Al final, imprima la suma total
# Ejemplo: Entrada: my_list = ['10', 'manzana', '5.5', '3', 'n/a']
# Salida 10.0 "sumado correctamente"
# "Elemento inválido: manzana"
# 5.5 "sumado correctamente"
# 3.0 "sumado correctamente"
# "Elemento inválido: n/a"
# "Total de la suma:" 18.5
my_list2 = ['10', 'manzana', '5.5', '3', 'n/a']
def sum_vals(list):
    new_list = ""
    total = 0
    for element in list:
        try:
            float_number = float(element)
        except ValueError:
            new_list += '"Elemento inválido: '+element+'"\n'
            continue

        total += float_number
        new_list += str(float_number)+' "sumado correctamente"\n'

    new_list += '"Total de la suma:" '+str(total)
    return new_list

if __name__ == '__main__':
	print(sum_vals(my_list2))