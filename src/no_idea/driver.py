from src.no_idea.util import calculate_happiness
'''
3 2
1 5 3
3 1
5 7
'''
n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = calculate_happiness(arr, A, B)
print(result)
