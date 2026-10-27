# Student data: Nombre completo
# Sección (ejemplo: 11B)
# Nota de español
# Nota de inglés
# Nota de sociales
# Nota de ciencias
# Nota Promedio

import csv

CSV_FILE = "students.csv"
HEADERS =  [
        "full_name", 
        "class_num", 
        "spanish_grade",
        "english_grade",
        "socials_grade",
        "science_grade",
        ]
student_list = []

def export_students():
    try:
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(student_list)

        print("Students exported successfully.")

    except OSError as error: 
        print(f"Error exporting students: {error}")

def import_students():
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            header = next(reader, None)

            if header is None:
                print("The file is empty.")
                return []

            imported_students = []

            for row in reader:
                student = {
                    "full_name": row["full_name"],
                    "class_num": row["class_num"],
                    "spanish_grade": float(row["spanish_grade"]),
                    "english_grade": float(row["english_grade"]),
                    "socials_grade": float(row["socials_grade"]),
                    "science_grade": float(row["science_grade"]),
                }
                imported_students.append(student)

            student_list.append(imported_students) 

        print("Students imported successfully.")

    except (OSError, ValueError, KeyError, csv.Error) as error:
        print(f"Error importing students: {error}")
        return None