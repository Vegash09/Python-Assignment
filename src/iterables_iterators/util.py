from itertools import combinations

def probability_with_a(lst, pick):
    total = list(combinations(lst, pick))
    with_a = [c for c in total if 'a' in c]
    return round(len(with_a) / len(total), 4)
