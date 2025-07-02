from src.piling_up.util import can_stack_blocks
'''
2
6
4 3 2 1 3 4
3
1 3 2
'''
T = int(input())
for _ in range(T):
    _ = int(input())  # n is not needed
    blocks = list(map(int, input().split()))
    print(can_stack_blocks(blocks))
