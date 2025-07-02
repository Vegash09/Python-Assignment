def count_unique_words(words):
    unique = []
    count = {}

    for word in words:
        if word not in unique:
            unique.append(word)
        count[word] = count.get(word, 0) + 1

    return len(unique), [count[word] for word in unique]
