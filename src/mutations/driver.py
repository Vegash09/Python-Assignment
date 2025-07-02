from src.mutations.util import mutate_string

string = input()
position, character = input().split()
position = int(position)

result = mutate_string(string, position, character)
print(result)
