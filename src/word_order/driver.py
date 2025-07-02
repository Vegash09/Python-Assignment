from src.word_order.util import count_unique_words

N = int(input())
words = [input() for _ in range(N)]

unique_count, word_counts = count_unique_words(words)
print(unique_count)
print(' '.join(map(str, word_counts)))
