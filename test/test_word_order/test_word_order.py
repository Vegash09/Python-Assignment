import unittest

from src.word_order.util import count_unique_words


class TestWordCounter(unittest.TestCase):

    def test_basic(self):
        words = ["a", "b", "a", "a", "b", "c"]
        expected_count = 3
        expected_freqs = [3, 2, 1]
        self.assertEqual(count_unique_words(words), (expected_count, expected_freqs))