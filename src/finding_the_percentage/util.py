def finding_the_percentage(student_data, query_name):
    student_marks = dict(student_data)
    if query_name not in student_marks:
        return 0.0
    return round(sum(student_marks[query_name]) / len(student_marks[query_name]), 2)
