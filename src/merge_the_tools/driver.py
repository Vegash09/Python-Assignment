from src.merge_the_tools.util import merge_the_tools
'''
Eg input:
AABCAAADA
3
'''
string = input()
k = int(input())

output = merge_the_tools(string, k)
for line in output:
    print(line)
