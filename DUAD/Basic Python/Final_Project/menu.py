import actions

def student_main_menu():
    menu_string = (
        "\nWelcome to the Student Control System\n"
        "1. Add Student\n"
        "2. Modify Student\n"
        "3. Remove Student\n"
        "4. Show Students\n"
        "5. Top three students\n"
        "6. Show Average grades per student\n"
        "7. Export data to a CSV file\n"
        "8. Import data from a CSV file\n"
        "9. Show failed students\n"
        "0. Exit\n"
        "Select the option: "
    )

    while True:
        user_input = input(menu_string).strip()

        try:
            if user_input == "":
                raise ValueError("Invalid menu option. Menu selection cannot be empty.")

            option = int(user_input)

            if option < 0 or option > 9:
                raise ValueError("Invalid menu option. Please select a number from 0 to 9.")

            return option

        except ValueError as error:
            error_message = str(error)

            if error_message.startswith("Invalid menu option"):
                print(error)

            elif user_input.isalpha():
                print("Invalid menu selection. Letters are not allowed. Please enter a number from 0 to 9.")

            else:
                print("Invalid characters in menu selection. Please enter a valid number from 0 to 9.")

def student_add_menu():
    while True:
        user_input = input("\nHow many students would you like to add? ").strip()

        try:
            if user_input == "":
                raise ValueError("The number of students cannot be empty.")

            number_of_students = int(user_input)

            if number_of_students == 0:
                raise ValueError("The number of students must be at least 1. Zero is not allowed.")

            if number_of_students < 0:
                raise ValueError("The number of students cannot be negative.")

            return number_of_students

        except ValueError as error:
            error_message = str(error)

            if error_message.startswith("The number of students"):
                print(error)

            elif user_input.replace(".", "", 1).isdigit():
                print("Invalid input. Decimal numbers are not allowed. Please enter a valid number.")

            elif user_input.isalpha():
                print("Invalid input. Letters are not allowed. Please enter a number of students.")

            else:
                print("Invalid input. Please enter a valid number without special characters.")

def student_name_menu():
    while True:
        name = input("\nEnter the student's full name: ").strip()

        is_valid, error_message = actions.is_valid_name(name)

        if is_valid:
            return name

        print(error_message)

def student_section_menu():
    while True:
        section = input("\nEnter the student's section (Example: 11B): ").strip()

        is_valid, error_message = actions.is_valid_section(section)

        if is_valid:
            return section.upper()

        print(error_message)

def student_information_menu():
    print("\n--- Student Information ---")

    student_information = {
        "full_name": student_name_menu(),
        "class_num": student_section_menu()
    }

    return student_information


def student_identity_menu():
    print("\n--- Student Identification ---")

    name = student_name_menu()
    section = student_section_menu()

    return name, section

def get_grade(subject):
    while True:
        user_input = input(f"Enter the {subject} grade (0-100): ").strip()

        if user_input == "":
            print(f"{subject} grade cannot be empty.")
            continue

        try:
            grade = float(user_input)

        except ValueError:
            if user_input.isalpha():
                print(f"Invalid {subject} grade. Letters are not allowed. Please enter a numeric value.")
            else:
                print(f"Invalid {subject} grade. Please enter a valid number, such as 85 or 92.5.")
            continue

        except TypeError:
            print(f"Invalid {subject} grade. The grade must be numeric.")
            continue

        except OverflowError:
            print(f"Invalid {subject} grade. The number is too large.")
            continue

        if grade < 0:
            print(f"{subject} grade cannot be negative. Minimum grade is 0.")
            continue

        elif grade > 100:
            print(f"{subject} grade cannot be greater than 100.")
            continue

        return grade

def student_grades_menu():
    print("\n--- Student Grades ---")

    grades = {}
    grades["spanish_grade"] = get_grade("Spanish")
    grades["english_grade"] = get_grade("English")
    grades["socials_grade"] = get_grade("Social Studies")
    grades["science_grade"] = get_grade("Science")

    return grades

def remove_student_menu():
    print("\nAre you sure you want to delete this student?")

    while True:
        confirmation = input("Enter yes or no: ").strip().lower()

        try:
            if confirmation == "":
                raise ValueError("Confirmation cannot be empty. Please enter yes or no.")

            if confirmation not in ["yes", "no"]:
                raise ValueError("Invalid confirmation. Please enter exactly 'yes' or 'no'.")

        except ValueError as error:
            print(error)
            continue

        if confirmation == "yes":
            return True

        return False