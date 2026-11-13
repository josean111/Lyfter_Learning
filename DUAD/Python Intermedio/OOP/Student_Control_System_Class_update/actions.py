from student import Student

def find_student(student_list, student, excluded_student=None):
    for existing_student in student_list:
        if existing_student is not excluded_student:
            if existing_student.full_name.strip().lower() == student.full_name.strip().lower() and existing_student.class_num.strip().upper() == student.class_num.strip().upper():
                return existing_student

    return None

def student_exists(student_list, student):
    if find_student(student_list, student) is not None:
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
    try:
        grade = float(grade)
    except ValueError:
        return False, 0, "The grade must be numeric."

    except TypeError:
        return False, 0, "The grade must be a number."

    if grade < 0 or grade > 100:
        return False, 0, "The grade must be between 0 and 100."

    return True, grade, ""

def add_student(student_list, student):
    student_list.append(student)
    return student_list, True, f"Student '{student.full_name}' added successfully."

def modify_student(student_list, student, new_student, modify_option):
    current_student = find_student(student_list, student)

    if current_student is None:
        return student_list, False, "Student not found. No information was modified."

    if modify_option == 1 or modify_option == 3:
        identity_changed = (new_student.full_name.strip().lower() != current_student.full_name.strip().lower() or new_student.class_num.strip().upper() != current_student.class_num.strip().upper())

        if identity_changed:
            if find_student(student_list, new_student, current_student) is not None:
                return student_list, False, "Cannot modify student. Another student with the same name and section already exists in memory."

        current_student.full_name = new_student.full_name
        current_student.class_num = new_student.class_num

    if modify_option == 2 or modify_option == 3:
        current_student.set_grades(new_student.spanish_grade, new_student.english_grade, new_student.socials_grade, new_student.science_grade)

    if modify_option == 1:
        return student_list, True, "Student information updated successfully."

    elif modify_option == 2:
        return student_list, True, "Student grades updated successfully."

    return student_list, True, "Student information and grades updated successfully."

def remove_student(student_list, student):
    existing_student = find_student(student_list, student)

    if existing_student is None:
        return student_list, False, "Student not found. No student was removed."

    student_list.remove(existing_student)

    return student_list, True, "Student removed successfully."

def combine_student_data(student_list, csv_student_data, csv_overwrite):
    combine_students = []
    for student in student_list:
        new_student = Student(student.full_name, student.class_num)
        new_student.set_grades(student.spanish_grade, student.english_grade, student.socials_grade, student.science_grade)
        combine_students.append(new_student)

    for csv_student in csv_student_data:
        existing_student = find_student(combine_students, csv_student)
        if existing_student is None:
            new_student = Student(csv_student.full_name, csv_student.class_num)
            new_student.set_grades(csv_student.spanish_grade, csv_student.english_grade, csv_student.socials_grade, csv_student.science_grade)
            combine_students.append(new_student)
        elif csv_overwrite:
            existing_student.full_name = csv_student.full_name
            existing_student.class_num = csv_student.class_num
            existing_student.set_grades(csv_student.spanish_grade, csv_student.english_grade, csv_student.socials_grade, csv_student.science_grade)

    return combine_students

def has_memory_only_students(student_list, imported_students):
    for student in student_list:
        if not student_exists(imported_students, student):
            return True
    return False

def show_student(student_list):
    if len(student_list) == 0:
        print("There are no students to display.\n")
        return

    print("\n--- Students List ---")
    for student in student_list:
        print("\nName: ", student.full_name)
        print("Section: ", student.class_num)
        print("Spanish: ", student.spanish_grade)
        print("English: ", student.english_grade)
        print("Social Studies: ", student.socials_grade)
        print("Science: ", student.science_grade)
        print("Average: ", round(calculate_student_average(student), 2))

def calculate_student_average(student):
    total_grades = student.spanish_grade + student.english_grade + student.socials_grade + student.science_grade
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
        print("Name: ", student.full_name)
        print("Section: ", student.class_num)
        print("Average: ", round(calculate_student_average(student), 2))

def show_failed_students(student_list):
    if len(student_list) == 0:
        print("There are no students yet.\n")
        return
    failed_students_found = False
    for student in student_list:
        failed_subjects = []
        if student.spanish_grade < 60:
            failed_subjects.append("Spanish: " + str(student.spanish_grade))
        if student.english_grade < 60:
            failed_subjects.append("English: " + str(student.english_grade))
        if student.socials_grade < 60:
            failed_subjects.append("Social Studies: " + str(student.socials_grade))
        if student.science_grade < 60:
            failed_subjects.append("Science: " + str(student.science_grade))

        if len(failed_subjects) > 0:
            if not failed_students_found:
                print("\n--- Failed Students ---")
            failed_students_found = True
            print("\nName: ", student.full_name)
            print("Section: ", student.class_num)
            print("Failed subjects: ")
            for subject in failed_subjects:
                print("-", subject)

    if not failed_students_found:
        print("There are no students with failed grades.\n")