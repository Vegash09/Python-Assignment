from collections import namedtuple

def calculate_average_mark(n, columns, student_data):
    Student = namedtuple('Student', columns)
    students = [Student(*line.split()) for line in student_data]
    total = sum(int(s.MARKS) for s in students)
    return round(total / n, 2)
