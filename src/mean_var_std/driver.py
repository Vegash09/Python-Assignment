from src.mean_var_std.util import compute_statistics
'''
eg Input
3 3
1 2 3
4 5 6
7 8 9
'''
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

mean, var, std = compute_statistics(arr)

print(mean)
print(var)
print(std)
