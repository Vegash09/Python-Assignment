def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        unique = ''.join(dict.fromkeys(substring))
        result.append(unique)
    return result
