import menu
import actions
import data
from student import Student

def main():
    student_list = []
    has_unsaved_changes = False

    while True:
        option = menu.student_main_menu()
        if option == 1:
            number_of_students = menu.student_add_menu()
            new_students_added = 0

            while new_students_added < number_of_students:
                print(f"\nStudent {new_students_added + 1} of {number_of_students}")
                student = menu.student_information_menu()

                if actions.student_exists(student_list, student):
                    print("Cannot add student. A student with the same name and section already exists.")
                    continue

                student = menu.student_grades_menu(student)
                student_list, student_added, error_message = actions.add_student(student_list, student)
                print(error_message)

                if student_added:
                    new_students_added += 1
                    has_unsaved_changes = True

        elif option == 2:
            if len(student_list) == 0:
                print("There are no students available to modify.\n")
                continue

            student = menu.student_information_menu()
            if not actions.student_exists(student_list, student):
                print("Student not found. No information was modified.\n")
                continue

            modify_option = menu.student_modify_menu()
            if modify_option == 0:
                print("Student modification cancelled.\n")
                continue

            if modify_option == 1 or modify_option == 3:
                new_student = menu.student_information_menu()

            else:
                current_student = actions.find_student(student_list, student)
                new_student = Student(current_student.full_name, current_student.class_num)

            if modify_option == 2 or modify_option == 3:
                new_student = menu.student_grades_menu(new_student)

            student_list, student_modified, error_message = actions.modify_student(student_list, student, new_student, modify_option)
            print(error_message)
            if student_modified:
                has_unsaved_changes = True

        elif option == 3:
            if len(student_list) == 0:
                print("There are no students available to remove.\n")
                continue

            student = menu.student_information_menu()
            if not actions.student_exists(student_list, student):
                print("Student not found. No student was removed.\n")
                continue

            confirmation = menu.remove_student_menu()
            if not confirmation:
                print("Student removal cancelled.\n")
                continue

            student_list, student_removed, error_message = actions.remove_student(student_list, student)
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
            export_successful, error_message = data.export_students(student_list)
            print(error_message)

            if export_successful:
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

            student_list = actions.combine_student_data(student_list, imported_students, True)
            has_unsaved_changes = actions.has_memory_only_students(student_list, imported_students)

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
                    export_successful, error_message = data.export_students(student_list)
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