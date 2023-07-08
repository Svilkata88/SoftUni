class Class:
    students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, student_name: str, grade: float):
        if len(self.students) < Class.students_count:
            self.students.append(student_name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.students)

    def __repr__(self):
        return_string = f'The students in {self.name}: '
        return_string += f"{', '.join(self.students)}. Average grade: {Class.get_average_grade(self):.2f}"
        return return_string

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)


