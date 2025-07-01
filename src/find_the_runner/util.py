def second_highest_number(numbers):
    unique_sorted = sorted(set(numbers))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[-2]
