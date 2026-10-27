
import menu
import actions
import data


def main():
    while True:
        option = menu.student_main_menu()

        if option == 1:
            actions.add_student()
        elif option == 2:
            actions.modify_student()
        elif option == 3:
            actions.remove_student()
        elif option == 4:
            actions.show_student()
        elif option == 5:
            actions.top_three_students()
        elif option == 6:
            actions.show_average_grades()
        elif option == 7:
            data.export_students()
        elif option == 8:
            data.import_students()
        elif option == 9:
            actions.show_failed_students()
        elif option == 0:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
