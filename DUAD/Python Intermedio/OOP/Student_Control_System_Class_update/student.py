class Student:
    def __init__(self, full_name, class_num):
        self.full_name = full_name
        self.class_num = class_num

    def set_grades(self, spanish_grade, english_grade, socials_grade, science_grade):
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade