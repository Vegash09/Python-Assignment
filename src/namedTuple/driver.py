from src.namedTuple.util import calculate_average_mark
''''
3
ID MARKS NAME CLASS
1 97 Raymond 7
2 50 Steven 4
3 91 Adrian 9
'''
n = int(input())
columns = input().split()
student_data = [input() for _ in range(n)]

result = calculate_average_mark(n, columns, student_data)
print(result)
