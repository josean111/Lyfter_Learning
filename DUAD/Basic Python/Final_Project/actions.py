def add_student(student_list, student_information):
    required_fields = ["full_name", "class_num", "spanish_grade", "english_grade", "socials_grade", "science_grade"]

    for field in required_fields:
        if field not in student_information:
            print(f"Missing required student information: {field}.")
            return False

    name = student_information["full_name"]
    is_valid, error_message = is_valid_name(name)

    if not is_valid:
        print(error_message)
        return False

    section = student_information["class_num"]
    is_valid, error_message = is_valid_section(section)

    if not is_valid:
        print(error_message)
        return False

    name = name.strip()
    section = section.strip().upper()

    if student_exists(student_list, name, section):
        print("Cannot add student. A student with the same name and section already exists.")
        return False

    grade_fields = ["spanish_grade", "english_grade", "socials_grade", "science_grade"]

    for grade_field in grade_fields:
        try:
            grade = float(student_information[grade_field])

        except ValueError:
            print(f"Invalid {grade_field}. The grade must be numeric.")
            return False

        except TypeError:
            print(f"Invalid {grade_field}. The grade must be a number.")
            return False

        except OverflowError:
            print(f"Invalid {grade_field}. The number is too large.")
            return False

        if not is_valid_grade(grade):
            print(f"Invalid {grade_field}. The grade must be a number between 0 and 100.")
            return False

        student_information[grade_field] = grade

    student_information["full_name"] = name
    student_information["class_num"] = section
    student_list.append(student_information)

    print(f"\nStudent {name} added successfully!\n")
    return True

def modify_student(student_list, name, section, new_grades):
    if not student_exists(student_list, name, section):
        print("Student not found. No information was modified.")
        return False

    required_grades = ["spanish_grade", "english_grade", "socials_grade", "science_grade"]
    validated_grades = {}

    for grade_field in required_grades:
        if grade_field not in new_grades:
            print(f"Missing grade information: {grade_field}.")
            return False

        try:
            grade = float(new_grades[grade_field])

        except ValueError:
            print(f"Invalid {grade_field}. The grade must be numeric.")
            return False

        except TypeError:
            print(f"Invalid {grade_field}. The grade must be a number.")
            return False

        except OverflowError:
            print(f"Invalid {grade_field}. The number is too large.")
            return False

        if not is_valid_grade(grade):
            print(f"Invalid {grade_field}. The grade must be a number between 0 and 100.")
            return False

        validated_grades[grade_field] = grade
        
    for student in student_list:
        if student["full_name"].strip().lower() == name.strip().lower() and student["class_num"].strip().upper() == section.strip().upper():
            student["spanish_grade"] = validated_grades["spanish_grade"]
            student["english_grade"] = validated_grades["english_grade"]
            student["socials_grade"] = validated_grades["socials_grade"]
            student["science_grade"] = validated_grades["science_grade"]

            print("\nStudent grades updated successfully!\n")
            return True

    return False

def remove_student(student_list, name, section):
    if not student_exists(student_list, name, section):
        print("Student not found. No student was removed.")
        return False

    for student in student_list:
        if student["full_name"].strip().lower() == name.strip().lower() and student["class_num"].strip().upper() == section.strip().upper():
            student_list.remove(student)
            print("\nStudent removed successfully!\n")
            return True

    return False

def show_student(student_list):
    if len(student_list) == 0:
        print("There are no students registered.\n")
        return

    print("\n--- Registered Students ---")
    for student in student_list:
        print("\nName: ", student["full_name"])
        print("Section: ", student["class_num"])
        print("Spanish: ", student["spanish_grade"])
        print("English: ", student["english_grade"])
        print("Social Studies: ", student["socials_grade"])
        print("Science: ", student["science_grade"])
        print("Average: ", round(calculate_student_average(student), 2))

def calculate_student_average(student):
    total_grades = student["spanish_grade"] + student["english_grade"] + student["socials_grade"] + student["science_grade"]
    average = total_grades / 4
    return average

def show_average_grades(student_list):
    if len(student_list) == 0:
        print("There are no students registered.\n")
        return

    total_average = 0
    for student in student_list:
        student_average = calculate_student_average(student)
        total_average = total_average + student_average

    general_average = total_average / len(student_list)
    print("\n--- Average Grades ---")
    print("The average grade of all students is: ", round(general_average, 2))


def top_three_students(student_list):
    if len(student_list) == 0:
        print("There are no students registered.\n")
        return

    students_temp = []
    for student in student_list:
        students_temp.append(student)

    for i in range(len(students_temp)):
        for j in range(i + 1, len(students_temp)):
            first_average = calculate_student_average(students_temp[i])
            second_average = calculate_student_average(students_temp[j])

            if second_average > first_average:
                temporary_student = students_temp[i]
                students_temp[i] = students_temp[j]
                students_temp[j] = temporary_student

    print("\n--- Top Three Students ---")
    number_of_students = len(students_temp)
    if number_of_students > 3:
        number_of_students = 3

    for i in range(number_of_students):
        student = students_temp[i]

        print("\nPosition: ", i + 1)
        print("Name: ", student["full_name"])
        print("Section: ", student["class_num"])
        print("Average: ", round(calculate_student_average(student), 2))


def show_failed_students(student_list):
    if len(student_list) == 0:
        print("There are no students registered.\n")
        return

    failed_students_found = False

    for student in student_list:
        failed_subjects = []

        if student["spanish_grade"] < 60:
            failed_subjects.append("Spanish: " + str(student["spanish_grade"]))

        if student["english_grade"] < 60:
            failed_subjects.append("English: " + str(student["english_grade"]))

        if student["socials_grade"] < 60:
            failed_subjects.append("Social Studies: " + str(student["socials_grade"]))

        if student["science_grade"] < 60:
            failed_subjects.append("Science: " + str(student["science_grade"]))

        if len(failed_subjects) > 0:
            failed_students_found = True
            print("\n--- Failed Students ---")
            print("\nName: ", student["full_name"])
            print("Section: ", student["class_num"])
            print("Failed subjects: ")

            for subject in failed_subjects:
                print("-", subject)

    if not failed_students_found:
        print("There are no students with failed grades.\n")

def student_exists(student_list, name, section):
    for student in student_list:
        if student["full_name"].strip().lower() == name.strip().lower() and student["class_num"].strip().upper() == section.strip().upper():
            return True
    return False

def is_valid_name(name):
    if name.strip() == "":
        return False, "Student name cannot be empty."

    for character in name:
        if character.isdigit():
            return False, "Invalid name. Numbers are not allowed in the student's name."

    return True, ""

def is_valid_section(class_num):
    if class_num.strip() == "":
        return False, "Student section cannot be empty."

    section = class_num.strip()

    if len(section) != 3:
        return False, "Invalid section, a valid section has 3 characters total. Format is two digits followed by one letter, for example 11B."

    counter = 0
    for character in section:
        if counter < 2:
            if not character.isdigit() or not character.isascii():
                return False, "Invalid section. Format is two digits followed by one letter, for example 11B."
        else:
            if not character.isalpha() or not character.isascii():
                return False, "Invalid section, a number is not part of a valid section. Format is two digits followed by one letter, for example 11B."
        counter = counter + 1

    return True, ""

def is_valid_grade(grade):
    if grade < 0 or grade > 100:
        return False
    return True