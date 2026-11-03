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
                raise ValueError("Invalid option: Selection cannot be empty.")

            option = int(user_input)
            if option < 0 or option > 9:
                raise ValueError("Invalid option. Please select a number from 0 to 9.")

            return option

        except ValueError as error:
            error_message = str(error)

            if error_message.startswith("Invalid option"):
                print(error)

            elif user_input.replace(".", "", 1).isdigit():
                print("Invalid input. Decimal numbers are not allowed. Please enter a valid number.")

            elif user_input.isalpha():
                print("Invalid input. Letters are not allowed. Please enter a number from 0 to 9.")

            else:
                print("Invalid input. Please enter a valid menu number.")

def student_add_menu():
    while True:
        user_input = input("\nHow many students would you like to add? ").strip()
        try:
            if user_input == "":
                raise ValueError("Invalid quantity: The number of students cannot be empty.")

            number_of_students = int(user_input)
            if number_of_students < 1:
                raise ValueError("Invalid quantity: The number of students must be at least 1.")

            return number_of_students

        except ValueError as error:
            error_message = str(error)

            if error_message.startswith("Invalid quantity"):
                print(error)

            elif user_input.replace(".", "", 1).isdigit():
                print("Invalid input. Decimal numbers are not allowed.")

            elif user_input.isalpha():
                print("Invalid input. Letters are not allowed.")

            else:
                print("Invalid input. Please enter a valid positive integer.")

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
    student_information = {"full_name": student_name_menu(),"class_num": student_section_menu()}
    return student_information

def student_identity_menu():
    print("\n--- Student Information ---")
    name = student_name_menu()
    section = student_section_menu()
    return name, section

def student_modify_menu():
    menu_string = (
        "\n--- Modify Student ---\n"
        "1. Modify student information\n"
        "2. Modify grades\n"
        "3. Modify all\n"
        "0. Cancel\n"
        "Select the option: "
    )

    while True:
        user_input = input(menu_string).strip()
        try:
            if user_input == "":
                raise ValueError("Invalid option: Selection cannot be empty.")

            option = int(user_input)
            if option < 0 or option > 3:
                raise ValueError("Invalid option. Please select a number from 0 to 3.")

            return option

        except ValueError as error:
            error_message = str(error)

            if error_message.startswith("Invalid option"):
                print(error)

            elif user_input.isalpha():
                print("Invalid input. Letters are not allowed.")

            else:
                print("Invalid input. Please enter a valid menu number.")


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
                print(f"Invalid {subject} grade. Please enter a valid number.")
            continue

        if not actions.is_valid_grade(grade):
            print(f"Invalid {subject} grade. Please enter a number between 0 and 100.")
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

def confirm_action_menu(prompt):
    while True:
        confirmation = input(prompt + " (Y)es/(N)o): ").strip().lower()
        try:
            if confirmation == "":
                raise ValueError("Invalid confirmation: Selection cannot be empty.")
            if confirmation not in ["yes", "y", "no", "n"]:
                raise ValueError("Invalid confirmation. Please enter yes (Y) or no (N).")

        except ValueError as error:
            print(error)
            continue

        if confirmation == "yes" or confirmation == "y":
            return True

        return False

def remove_student_menu():
    return confirm_action_menu("\nAre you sure you want to remove this student?")

def confirm_import_menu():
    print("\nWARNING: IMPORTING CSV DATA WILL UPDATE YOUR CURRENT STUDENT LIST.")
    print("Students already in memory that also exist in CSV will be overwritten.")
    print("This includes their student information and grades.")
    print("Students that exist only in memory will be preserved.")
    print("Your unsaved changes to matching students may be lost.")

    return confirm_action_menu("Do you want to continue with the import?")


def confirm_exit_menu(export_available):
    print("\nWARNING: You have unsaved student information.")

    if export_available:
        while True:
            print("\n1. Export and exit")
            print("2. Exit without saving")
            print("3. Return to menu")

            user_input = input("Select the option: ").strip()
            try:
                if user_input == "":
                    raise ValueError("Invalid option: Selection cannot be empty.")

                option = int(user_input)
                if option < 1 or option > 3:
                    raise ValueError("Invalid option. Please select a number from 1 to 3.")

                if option == 1:
                    return "export"

                elif option == 2:
                    return "discard"

                return "cancel"

            except ValueError as error:
                error_message = str(error)

                if error_message.startswith("Invalid option"):
                    print(error)

                else:
                    print("Invalid input. Please enter a valid menu number.")

    print("\nThe existing CSV file has not been imported.")
    print("Exporting now could overwrite its saved student information.")
    confirmation = confirm_action_menu("Are you sure you want to exit without saving?")
    if confirmation:
        return "discard"

    return "cancel"
