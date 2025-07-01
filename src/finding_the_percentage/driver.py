from src.finding_the_percentage.util import finding_the_percentage

'''
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0
56.00
'''


n = int(input())
student_data = []

for _ in range(n):
    entry = input().split()
    name = entry[0]
    scores = list(map(float, entry[1:]))
    student_data.append((name, scores))

query_name = input()
result = finding_the_percentage(student_data, query_name)
print("{:.2f}".format(result))

