
import csv
import actions


CSV_FILE = "students.csv"

HEADERS = ["full_name", "class_num", "spanish_grade", "english_grade", "socials_grade", "science_grade"]

student_list = []


def export_students():
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(student_list)

    except PermissionError:
        print("Export failed: Permission denied. You do not have permission to write to the CSV file.")
        return False

    except IsADirectoryError:
        print("Export failed: The CSV path refers to a directory, not a file.")
        return False

    except FileNotFoundError:
        print("Export failed: The destination directory does not exist.")
        return False

    except csv.Error:
        print("Export failed: An error occurred while creating the CSV file.")
        return False

    except ValueError as error:
        print(f"Export failed: Invalid student data. {error}")
        return False

    except TypeError:
        print("Export failed: Student information contains an invalid data type.")
        return False

    except OSError:
        print("Export failed: An unexpected file system error occurred.")
        return False

    print(f"Successfully exported {len(student_list)} students to CSV file.")
    return True


def import_students():
    imported_students = []

    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                print("Import failed: The CSV file is empty or does not contain headers.")
                return False

            if reader.fieldnames != HEADERS:
                print("Import failed: The CSV headers do not match the expected format.")
                return False

            row_number = 1

            for row in reader:
                row_number = row_number + 1

                if None in row:
                    print(f"Import failed: Extra columns found at row {row_number}.")
                    return False

                for field in HEADERS:
                    if row[field] is None:
                        print(f"Import failed: Missing information for '{field}' at row {row_number}.")
                        return False

                    if row[field].strip() == "":
                        print(f"Import failed: Empty information for '{field}' at row {row_number}.")
                        return False

                name = row["full_name"].strip()
                is_valid, error_message = actions.is_valid_name(name)

                if not is_valid:
                    print(f"Import failed: {error_message} Row {row_number}.")
                    return False

                section = row["class_num"].strip().upper()
                is_valid, error_message = actions.is_valid_section(section)

                if not is_valid:
                    print(f"Import failed: {error_message} Row {row_number}.")
                    return False

                if actions.student_exists(imported_students, name, section):
                    print(f"Import failed: Duplicate student found at row {row_number}.")
                    return False

                grade_fields = ["spanish_grade", "english_grade", "socials_grade", "science_grade"]
                validated_grades = {}

                for grade_field in grade_fields:
                    try:
                        grade = float(row[grade_field])

                    except ValueError:
                        print(f"Import failed: Invalid numeric value for '{grade_field}' at row {row_number}.")
                        return False

                    except TypeError:
                        print(f"Import failed: Invalid data type for '{grade_field}' at row {row_number}.")
                        return False

                    except OverflowError:
                        print(f"Import failed: The number is too large for '{grade_field}' at row {row_number}.")
                        return False

                    if not actions.is_valid_grade(grade):
                        print(f"Import failed: Grade for '{grade_field}' must be between 0 and 100 at row {row_number}.")
                        return False

                    validated_grades[grade_field] = grade

                student = {
                    "full_name": name,
                    "class_num": section,
                    "spanish_grade": validated_grades["spanish_grade"],
                    "english_grade": validated_grades["english_grade"],
                    "socials_grade": validated_grades["socials_grade"],
                    "science_grade": validated_grades["science_grade"]
                }

                imported_students.append(student)

    except FileNotFoundError:
        print("Import failed: No previously exported CSV file was found.")
        print("Please export student information before attempting to import.")
        return False

    except PermissionError:
        print("Import failed: Permission denied. You do not have permission to read the CSV file.")
        return False

    except IsADirectoryError:
        print("Import failed: The CSV path refers to a directory, not a file.")
        return False

    except UnicodeDecodeError:
        print("Import failed: The CSV file contains an unsupported text encoding.")
        return False

    except csv.Error:
        print("Import failed: The CSV file contains invalid formatting.")
        return False

    except OSError:
        print("Import failed: An error occurred while reading the CSV file.")
        return False

    student_list.clear()

    for student in imported_students:
        student_list.append(student)

    print(f"Successfully imported {len(student_list)} students from CSV.")
    return True
