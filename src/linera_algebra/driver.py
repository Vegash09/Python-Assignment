from src.linera_algebra.util import calculate_determinant
'''
eg
Input
3
6 1 1
4 -2 5
2 8 7
'''
n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]

result = calculate_determinant(matrix)
print(result)
