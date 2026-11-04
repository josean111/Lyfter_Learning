def find_student(student_list, name, section, excluded_student=None):
    for student in student_list:
        if student is not excluded_student:
            if student["full_name"].strip().lower() == name.strip().lower() and student["class_num"].strip().upper() == section.strip().upper():
                return student

    return None

def student_exists(student_list, name, section):
    if find_student(student_list, name, section) is not None:
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
                return False, "First two characters need to be numbers. Format is two digits followed by one letter, for example 11B. Try again."
        else:
            if not character.isalpha() or not character.isascii():
                return False, "The last character must be a valid letter. Format is two digits followed by one letter, for example 11B. Try again."
        counter = counter + 1

    return True, ""

def is_valid_grade(grade):
    if grade != grade:
        return False
    if grade < 0 or grade > 100:
        return False

    return True



def validate_grades(grade_information):
    grade_fields = ["spanish_grade", "english_grade", "socials_grade", "science_grade"]
    validated_grades = {}
    for grade_field in grade_fields:
        if grade_field not in grade_information:
            return False, {}, f"Missing grade information: {grade_field}."

        try:
            grade = float(grade_information[grade_field])

        except ValueError:
            return False, {}, f"Invalid {grade_field}. The grade must be numeric."

        except TypeError:
            return False, {}, f"Invalid {grade_field}. The grade must be a number."

        except OverflowError:
            return False, {}, f"Invalid {grade_field}. The number is too large."

        if not is_valid_grade(grade):
            return False, {}, f"Invalid {grade_field}. The grade must be between 0 and 100."

        validated_grades[grade_field] = grade

    return True, validated_grades, ""

def add_student(student_list, student_information):
    required_fields = ["full_name","class_num","spanish_grade","english_grade","socials_grade","science_grade"]

    for field in required_fields:
        if field not in student_information:
            return student_list, False, f"Missing required student information: {field}."

    name = student_information["full_name"].strip()
    is_valid, error_message = is_valid_name(name)
    if not is_valid:
        return student_list, False, error_message

    section = student_information["class_num"].strip().upper()
    is_valid, error_message = is_valid_section(section)
    if not is_valid:
        return student_list, False, error_message

    if student_exists(student_list, name, section):
        return student_list, False, "Cannot add student. A student with the same name and section already exists."

    is_valid, validated_grades, error_message = validate_grades(student_information)
    if not is_valid:
        return student_list, False, error_message

    student = {"full_name": name,"class_num": section,"spanish_grade": validated_grades["spanish_grade"],"english_grade": validated_grades["english_grade"],"socials_grade": validated_grades["socials_grade"],"science_grade": validated_grades["science_grade"]}
    student_list.append(student)
    return student_list, True, f"Student '{name}' added successfully."

def modify_student(student_list, name, section, new_information, modify_option):
    current_student = find_student(student_list, name, section)

    if current_student is None:
        return student_list, False, "Student not found. No information was modified."

    validated_information = {}
    validated_grades = {}
    if modify_option == 1 or modify_option == 3:
        if "full_name" not in new_information or "class_num" not in new_information:
            return student_list, False, "Missing required student information."

        new_name = new_information["full_name"].strip()
        is_valid, error_message = is_valid_name(new_name)
        if not is_valid:
            return student_list, False, error_message

        new_section = new_information["class_num"].strip().upper()
        is_valid, error_message = is_valid_section(new_section)
        if not is_valid:
            return student_list, False, error_message

        identity_changed = (new_name.lower() != current_student["full_name"].strip().lower()or new_section != current_student["class_num"].strip().upper())

        if identity_changed:
            if find_student(student_list, new_name, new_section, current_student) is not None:
                return student_list, False, "Cannot modify student. Another student with the same name and section already exists in memory."

        validated_information["full_name"] = new_name
        validated_information["class_num"] = new_section

    if modify_option == 2 or modify_option == 3:
        is_valid, validated_grades, error_message = validate_grades(new_information)

        if not is_valid:
            return student_list, False, error_message

    for field in validated_information:
        current_student[field] = validated_information[field]

    for field in validated_grades:
        current_student[field] = validated_grades[field]

    if modify_option == 1:
        return student_list, True, "Student information updated successfully."

    elif modify_option == 2:
        return student_list, True, "Student grades updated successfully."

    return student_list, True, "Student information and grades updated successfully."

def remove_student(student_list, name, section):
    student = find_student(student_list, name, section)

    if student is None:
        return student_list, False, "Student not found. No student was removed."

    student_list.remove(student)
    return student_list, True, "Student removed successfully."

def combine_student_data(student_list, csv_student_data, csv_overwrite):
    combine_students = []

    for student in student_list:
        combine_students.append(student.copy())

    for csv_student in csv_student_data:
        existing_student = find_student(combine_students,csv_student["full_name"],csv_student["class_num"])
        if existing_student is None:
            combine_students.append(csv_student.copy())
        elif csv_overwrite:
            existing_student.update(csv_student)

    return combine_students

def has_memory_only_students(student_list, imported_students):
    for student in student_list:
        if not student_exists(imported_students,student["full_name"],student["class_num"]):
            return True

    return False

def show_student(student_list):
    if len(student_list) == 0:
        print("There are no students to display.\n")
        return

    print("\n--- Students List ---")
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
        print("There are no students yet.\n")
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
        print("There are no students yet.\n")
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
        print("There are no students yet.\n")
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
            if not failed_students_found:
                print("\n--- Failed Students ---")
            failed_students_found = True

            print("\nName: ", student["full_name"])
            print("Section: ", student["class_num"])
            print("Failed subjects: ")
            for subject in failed_subjects:
                print("-", subject)

    if not failed_students_found:
        print("There are no students with failed grades.\n")
