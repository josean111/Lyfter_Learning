# Options
# Add Student
# Modify Student
# Remove Student
# check notes
# check failed grades
# Importar
# exportar
import actions

def student_main_menu():
	try:
		menu_string = (
			f"Welcome to the Student Control System\n"
			f"1. Add Student\n"
			f"2. Modify Student\n"
			f"3. Remove Student\n"
			f"4. Show Students\n"
			f"5. Top three students\n"
			f"6. Show Average grades per student\n"
			f"7. Export data to a CSV file\n"
			f"8. Import data from a CSV file\n"
			f"Select the option: "
		)
		option = actions.is_valid_number(menu_string)
	except ValueError as ex:
		print(ex)
		print("Please try again with a valid option\n\n")
		return None
	
	return option

def student_add_menu():
	try:
		number_of_students_string = "How many students would you like to add? \n"
		try: 
			number_of_students = int(input(number_of_students_string)) 
		except ValueError:
			print("Option is not a valid number\nPlease try again with a valid number of students\n\n") 
			return None
		
		if number_of_students < 1:
			raise ValueError("You need to add at least 1 student\nPlease try again with a valid number")
	
	except ValueError as ex:
		print(ex)
		print("Please try again with a valid number of students\n\n")
		return None
	return number_of_students


