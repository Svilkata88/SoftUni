number_rows = int(input())
students_data = {}

for _ in range(0, number_rows):
    student_name = input()
    grade = float(input())
    if student_name not in students_data:
        students_data[student_name] = grade
    average_grade = (students_data[student_name] + grade) / 2
    students_data[student_name] = average_grade

for k, v in students_data.items():
    if v >= 4.5:
        print(f'{k} -> {v:.2f}')
