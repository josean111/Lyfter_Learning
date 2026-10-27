# funciones
# is_valid_name, is_valid_section y student_exists.

def add_student():
	full_name_of_student_string = "What is the full name of the student? \n"
	class_of_student_string = "What is the class the student belongs to? \n"
	spanish_note_string = "What is the spanish note for the student? \n"
	english_note_string = "What is the english note for the student? \n"
	socials_note_string = "What is the socials note for the student? \n"
	science_note_string = "What is the science note for the student? \n"

	try:
		name_of_student_string = input(name_of_student_string)
		if name_of_student_string[0].isdigit():
			raise ValueError("The name of the student cannot begin with a number\nPlease try again with a valid letter")
	except ValueError:
		print("Option is not a valid number\nPlease try again with a valid number of students\n\n")
		return None

	return None

def modify_student():
	print("Add ")

	return None

def remove_student():
	print("Add ")

	return None

def show_student():
	print("Add ")

	return None

def show_average_grades():
	print("Add ")

	return None

def top_three_students():
	print("Add ")

	return None

def show_failed_students():
	print("Add ")

	return None

def student_exists():
	try:
		name_of_student_string = "What is the name of the student? \n"
		class_of_student_string = "What is the class the student belongs to? \n"

		try:
			name_of_student_string = input(name_of_student_string)
			if name_of_student_string[0].isdigit():
				raise ValueError("The name of the student cannot begin with a number\nPlease try again with a valid letter")
		except ValueError:
			print("Option is not a valid number\nPlease try again with a valid number of students\n\n")
			return None

		try:
			class_of_student_string = int(input(class_of_student_string))
		except ValueError:
			print("Option is not a valid number\nPlease try again with a valid number of students\n\n")
			return None

	except ValueError as ex:
		print(ex)
		print("Please try again with valid input of students\n\n")
		return None

	return name_of_student_string, class_of_student_string

def is_valid_number(menu_string):
	try: 
		option = int(input(menu_string)) 
	except ValueError:
			print("Option is not a valid number\nPlease try again with a valid number\n\n") 
			return None
	if option < 1 or option > 8:
		raise ValueError("Option is not available yet")
	return option

def is_valid_name(menu_string):
	try: 
		option = input(menu_string)
	except ValueError:
			print("Option is not a valid number\nPlease try again with a valid number\n\n") 
			return None
	if option < 1 or option > 8:
		raise ValueError("Option is not available yet")
	return option

def is_valid_class(menu_string):
	try: 
		option = int(input(menu_string)) 
	except ValueError:
			print("Option is not a valid number\nPlease try again with a valid number\n\n") 
			return None
	if option < 1 or option > 8:
		raise ValueError("Option is not available yet")
	return option

def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the {subject} grade in a scale of 0 to 100: "))

            if 0 <= grade <= 100:
                return grade

            print("The grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")
