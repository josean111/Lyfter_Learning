import menu
import actions
import data

def main():
    while True:
        option = menu.student_main_menu()

        if option == 1:
            number_of_students = menu.student_add_menu()
            new_students_added = 0
            while new_students_added < number_of_students:
                print(f"\nStudent {new_students_added + 1} of {number_of_students}")

                student_information = menu.student_information_menu()
                if actions.student_exists(data.student_list, student_information["full_name"], student_information["class_num"]):
                    print("Duplicate student detected. A student with this name and section already exists.")
                    print("Please enter different student information.\n")
                    continue

                student_grades = menu.student_grades_menu()
                student_information.update(student_grades)
                student_added = actions.add_student(data.student_list, student_information)

                if student_added:
                    new_students_added = new_students_added + 1

            print(f"\nSuccessfully added {new_students_added} students.\n")

        elif option == 2:
            if len(data.student_list) == 0:
                print("There are no students available to modify.\n")
                continue

            name, section = menu.student_identity_menu()
            if actions.student_exists(data.student_list, name, section):
                new_grades = menu.student_grades_menu()
                actions.modify_student(data.student_list, name, section, new_grades)
            else:
                print("Student not found. No information was modified.\n")

        elif option == 3:
            if len(data.student_list) == 0:
                print("There are no students available to remove.\n")
                continue

            name, section = menu.student_identity_menu()
            if actions.student_exists(data.student_list, name, section):
                confirmation = menu.remove_student_menu()
                if confirmation:
                    actions.remove_student(data.student_list, name, section)
                else:
                    print("Student removal cancelled.\n")
            else:
                print("Student not found. No student was removed.\n")

        elif option == 4:
            actions.show_student(data.student_list)

        elif option == 5:
            actions.top_three_students(data.student_list)

        elif option == 6:
            actions.show_average_grades(data.student_list)

        elif option == 7:
            data.export_students()

        elif option == 8:
            data.import_students()

        elif option == 9:
            actions.show_failed_students(data.student_list)

        elif option == 0:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
