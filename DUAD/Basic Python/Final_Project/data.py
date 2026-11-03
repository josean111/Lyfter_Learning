import csv
import actions


CSV_FILE = "students.csv"

HEADERS = ["full_name", "class_num", "spanish_grade", "english_grade", "socials_grade", "science_grade"]


def load_csv_student_data():
    csv_student_data = []

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                return [], True, "CSV file is empty or does not contain headers."

            if reader.fieldnames != HEADERS:
                return [], True, "CSV file headers do not match the expected format."

            row_number = 1

            for row in reader:
                row_number = row_number + 1

                if None in row:
                    return [], True, f"CSV file row {row_number} contains extra columns without corresponding headers."

                for field in HEADERS:
                    if row[field] is None:
                        return [], True, f"CSV file row {row_number} is missing information for '{field}'."

                    if row[field].strip() == "":
                        return [], True, f"CSV file row {row_number} contains empty information for '{field}'."

                name = row["full_name"].strip()
                is_valid, error_message = actions.is_valid_name(name)

                if not is_valid:
                    return [], True, f"CSV file row {row_number}: {error_message}"

                section = row["class_num"].strip().upper()
                is_valid, error_message = actions.is_valid_section(section)

                if not is_valid:
                    return [], True, f"CSV file row {row_number}: {error_message}"

                if actions.student_exists(csv_student_data, name, section):
                    return [], True, f"CSV file contains a duplicate student at row {row_number}: {name}, section {section}."

                student = {
                    "full_name": name,
                    "class_num": section
                }

                grade_fields = ["spanish_grade", "english_grade", "socials_grade", "science_grade"]

                for grade_field in grade_fields:
                    try:
                        grade = float(row[grade_field])

                    except ValueError:
                        return [], True, f"CSV file row {row_number}: Invalid numeric value for '{grade_field}'."

                    except TypeError:
                        return [], True, f"CSV file row {row_number}: Invalid data type for '{grade_field}'."

                    if not actions.is_valid_grade(grade):
                        return [], True, f"CSV file row {row_number}: Grade for '{grade_field}' must be between 0 and 100."

                    student[grade_field] = grade

                csv_student_data.append(student)

    except FileNotFoundError:
        return [], False, "No students.csv file was found. There is no previously saved student information."

    except PermissionError:
        return [], True, "CSV file could not be read because permission was denied. Check the file permissions and try again."

    except UnicodeDecodeError:
        return [], True, "CSV file could not be read because it contains an unsupported text encoding."

    except csv.Error:
        return [], True, "CSV file contains invalid formatting."

    return csv_student_data, True, ""


def import_students():
    imported_students, file_exists, error_message = load_csv_student_data()

    if not file_exists:
        return [], False, "Import failed: The students.csv file does not exist. There is no CSV data available to import."

    if error_message:
        return [], False, f"Import failed: {error_message}"

    if len(imported_students) == 0:
        return [], False, f"There were no students to import from CSV."
    else:
        return imported_students, True, f"Successfully imported {len(imported_students)} students from CSV."



def export_students(student_list):
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(student_list)

    except PermissionError:
        return False, "Export failed: Permission denied. You do not have permission to write to the CSV file."

    except FileNotFoundError:
        return False, "Export failed: The destination directory does not exist."

    except csv.Error:
        return False, "Export failed: An error occurred while creating the CSV file."

    except ValueError as error:
        return False, f"Export failed: Invalid student data. {error}"

    except TypeError:
        return False, "Export failed: Student information contains an invalid data type."

    if len(student_list) == 0:
        return True, "Successfully created an empty CSV file with headers."

    return True, f"Successfully exported {len(student_list)} student records to CSV file."
