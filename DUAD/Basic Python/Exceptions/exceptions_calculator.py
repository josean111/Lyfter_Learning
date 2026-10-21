# Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
# 1. Suma
# 2. Resta
# 3. Multiplicación
# 4. División
# 5. Borrar resultado
# Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
# Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

def show_menu(current_num):
	try:
		menu_string = (
			f"1. Suma\n"
			f"2. Resta\n"
			f"3. Multiplicación\n"
			f"4. División\n"
			f"5. Borrar resultado\n"
			f"Número actual: {current_num}\n"
			f"Selecciona una opción: "
		)
		try: 
			option = int(input(menu_string)) 
		except ValueError:
			print("La opción no es un número válido\nIntente nuevamente\n\n") #v1
			return None
		if option < 1:
			raise ValueError('El numero es muy bajo')
		if option > 5:
			raise ValueError('El numero es muy alto')
	
	except ValueError as ex:
		print(ex)
		print("Intente nuevamente\n\n")
		return None
	return option


def do_math(operation,current_num):
	if operation == 5:
		return 0
	elif operation is None:
		return current_num
	
		# if operation == 5: #v1
		# 	current_num = 0 #v1
		# else: #v1
	try:
		input_num = float(input("Ingrese un número: "))
	except ValueError:
		print("Ingrese un número válido\nIntente nuevamente\n\n")
		return current_num
	try:
		match operation:
			case 1:
				current_num += input_num
			case 2:
				current_num -= input_num
			case 3:
				current_num *= input_num
			case 4:
				current_num /= input_num
	# except ValueError as ex: #v1
	# 	print(ex) #v1
	# 	print() #v1
	# 	return  #v1
	except ZeroDivisionError:
		print("No se puede dividir por cero.\nIntente nuevamente\n\n")
		return current_num
	return current_num

def main():
	current_num = 0
	while True:
		option = show_menu(current_num)
		current_num = do_math(option, current_num)
	
if __name__ == '__main__':
	main()