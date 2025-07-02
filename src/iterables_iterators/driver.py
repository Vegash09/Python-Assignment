from src.iterables_iterators.util import probability_with_a

N = int(input())
lst = input().split()
pick = int(input())

result = probability_with_a(lst, pick)
print(f"{result:.4f}")
