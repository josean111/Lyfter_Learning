import menu
import actions
import data

def export_current_data(student_list, csv_data_imported):
    latest_csv_data, csv_file_exists, error_message = data.load_csv_student_data()

    if csv_file_exists and error_message:
        return False, error_message, []

    if csv_data_imported:
        students_to_export = []

        for student in student_list:
            students_to_export.append(student.copy())

    else:
        students_to_export = actions.combine_student_data(student_list,latest_csv_data,False)

    export_successful, error_message = data.export_students(students_to_export)
    return export_successful, error_message, students_to_export


def main():
    student_list = []
    csv_student_data, csv_file_exists, error_message = data.load_csv_student_data()

    if csv_file_exists and error_message:
        print("\n" + error_message)
        print("The existing CSV file could not be read safely.")
        print("The program will close to prevent accidental data loss.")
        return

    csv_data_imported = False
    has_unsaved_changes = False

    if not csv_file_exists:
        print("\n" + error_message)
        print("You can start adding students and export them when ready.\n")

    else:
        print("\nWARNING: An existing CSV file was found.")
        print("You can add new students without importing the existing data.")
        print("Importing will combine the CSV data with your current students.\n")

    while True:
        option = menu.student_main_menu()
        if option == 1:
            number_of_students = menu.student_add_menu()
            new_students_added = 0

            while new_students_added < number_of_students:
                print(f"\nStudent {new_students_added + 1} of {number_of_students}")
                student_information = menu.student_information_menu()
                csv_student_data, csv_file_exists, error_message = data.load_csv_student_data()

                if csv_file_exists and error_message:
                    print("\n" + error_message)
                    print("Adding a student cannot continue until the CSV file is corrected.")
                    continue

                name = student_information["full_name"]
                section = student_information["class_num"]

                if actions.student_exists(student_list, name, section):
                    print("Cannot add student. A student with the same name and section already exists.")
                    continue

                if actions.student_exists_in_csv(csv_student_data, name, section):
                    print("Cannot add student. A student with the same name and section already exists in the CSV file. Import the CSV data before continuing.")
                    continue

                student_grades = menu.student_grades_menu()
                student_information.update(student_grades)
                student_list, student_added, error_message = actions.add_student(student_list, student_information, csv_student_data)
                print(error_message)

                if student_added:
                    new_students_added = new_students_added + 1
                    has_unsaved_changes = True

        elif option == 2:
            if len(student_list) == 0:
                print("There are no students available to modify.\n")
                continue

            name, section = menu.student_identity_menu()
            if not actions.student_exists(student_list, name, section):
                print("Student not found. No information was modified.\n")
                continue

            csv_student_data, csv_file_exists, error_message = data.load_csv_student_data()
            if csv_file_exists and error_message:
                print("\n" + error_message)
                print("Student modification cannot continue until the CSV file is corrected.")
                continue

            modify_option = menu.student_modify_menu()
            if modify_option == 0:
                print("Student modification cancelled.\n")
                continue

            new_information = {}
            if modify_option == 1 or modify_option == 3:
                new_information = menu.student_information_menu()

            if modify_option == 2 or modify_option == 3:
                new_grades = menu.student_grades_menu()
                new_information.update(new_grades)

            student_list, student_modified, error_message = actions.modify_student(student_list,name,section,new_information,modify_option,csv_student_data)
            print(error_message)
            if student_modified:
                has_unsaved_changes = True

        elif option == 3:
            if len(student_list) == 0:
                print("There are no students available to remove.\n")
                continue

            name, section = menu.student_identity_menu()
            if not actions.student_exists(student_list, name, section):
                print("Student not found. No student was removed.\n")
                continue

            confirmation = menu.remove_student_menu()
            if not confirmation:
                print("Student removal cancelled.\n")
                continue

            student_list, student_removed, error_message = actions.remove_student(student_list,name,section)
            print(error_message)
            if student_removed:
                has_unsaved_changes = True

        elif option == 4:
            actions.show_student(student_list)

        elif option == 5:
            actions.top_three_students(student_list)

        elif option == 6:
            actions.show_average_grades(student_list)

        elif option == 7:
            export_successful, error_message, students_to_export = export_current_data(student_list,csv_data_imported)
            print(error_message)

            if export_successful:
                student_list = students_to_export
                csv_student_data = []

                for student in student_list:
                    csv_student_data.append(student.copy())

                csv_file_exists = True
                csv_data_imported = True
                has_unsaved_changes = False

        elif option == 8:
            imported_students, import_successful, error_message = data.import_students()

            if not import_successful:
                print("\n" + error_message)
                continue

            if has_unsaved_changes:
                confirmation = menu.confirm_import_menu()

                if not confirmation:
                    print("Import cancelled. Your current student information was preserved.\n")
                    continue

            student_list = actions.combine_student_data(student_list,imported_students,True)
            csv_student_data = []
            for student in imported_students:
                csv_student_data.append(student.copy())

            csv_file_exists = True
            csv_data_imported = True
            has_unsaved_changes = False

            for student in student_list:
                if not actions.student_exists(imported_students,student["full_name"],student["class_num"]):
                    has_unsaved_changes = True
                    break

            print(error_message)
            print("CSV information was combined with your current student list.")
            print("Existing matching students were updated using the CSV information.")
            print("Students that existed only in memory were preserved.\n")

        elif option == 9:
            actions.show_failed_students(student_list)

        elif option == 0:
            if has_unsaved_changes:
                exit_option = menu.confirm_exit_menu(True)

                if exit_option == "export":
                    export_successful, error_message, students_to_export = export_current_data(student_list,csv_data_imported)
                    print(error_message)

                    if export_successful:
                        print("All student information was saved successfully.")
                        print("Goodbye!")
                        break

                    print("Your changes are still in memory.")
                    print("Returning to the main menu.\n")
                    continue

                elif exit_option == "discard":
                    print("\nUnsaved changes were discarded.")
                    print("Goodbye!")
                    break

                else:
                    print("\nReturning to the main menu.\n")
                    continue
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
