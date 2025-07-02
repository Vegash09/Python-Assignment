from src.min_max.util import max_of_row_mins
'''
Eg Input:
3 3
1 2 3
4 5 6
7 8 9
'''
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = max_of_row_mins(matrix)
print(result)
